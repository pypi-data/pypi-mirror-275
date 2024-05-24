import torch
import torch.nn as nn
import torch.nn.functional as F


class HadaWeight(torch.autograd.Function):
    @staticmethod
    def forward(ctx, w1d, w1u, w2d, w2u, scale=torch.tensor(1)):
        ctx.save_for_backward(w1d, w1u, w2d, w2u, scale)
        diff_weight = ((w1u @ w1d) * (w2u @ w2d)) * scale
        return diff_weight

    @staticmethod
    def backward(ctx, grad_out):
        (w1d, w1u, w2d, w2u, scale) = ctx.saved_tensors
        grad_out = grad_out * scale
        temp = grad_out * (w2u @ w2d)
        grad_w1u = temp @ w1d.T
        grad_w1d = w1u.T @ temp

        temp = grad_out * (w1u @ w1d)
        grad_w2u = temp @ w2d.T
        grad_w2d = w2u.T @ temp

        del temp
        return grad_w1d, grad_w1u, grad_w2d, grad_w2u, None


class HadaWeightTucker(torch.autograd.Function):
    @staticmethod
    def forward(ctx, t1, w1d, w1u, t2, w2d, w2u, scale=torch.tensor(1)):
        ctx.save_for_backward(t1, w1d, w1u, t2, w2d, w2u, scale)

        rebuild1 = torch.einsum("i j ..., j r, i p -> p r ...", t1, w1d, w1u)
        rebuild2 = torch.einsum("i j ..., j r, i p -> p r ...", t2, w2d, w2u)

        return rebuild1 * rebuild2 * scale

    @staticmethod
    def backward(ctx, grad_out):
        (t1, w1d, w1u, t2, w2d, w2u, scale) = ctx.saved_tensors
        grad_out = grad_out * scale

        temp = torch.einsum("i j ..., j r -> i r ...", t2, w2d)
        rebuild = torch.einsum("i j ..., i r -> r j ...", temp, w2u)

        grad_w = rebuild * grad_out
        del rebuild

        grad_w1u = torch.einsum("r j ..., i j ... -> r i", temp, grad_w)
        grad_temp = torch.einsum("i j ..., i r -> r j ...", grad_w, w1u.T)
        del grad_w, temp

        grad_w1d = torch.einsum("i r ..., i j ... -> r j", t1, grad_temp)
        grad_t1 = torch.einsum("i j ..., j r -> i r ...", grad_temp, w1d.T)
        del grad_temp

        temp = torch.einsum("i j ..., j r -> i r ...", t1, w1d)
        rebuild = torch.einsum("i j ..., i r -> r j ...", temp, w1u)

        grad_w = rebuild * grad_out
        del rebuild

        grad_w2u = torch.einsum("r j ..., i j ... -> r i", temp, grad_w)
        grad_temp = torch.einsum("i j ..., i r -> r j ...", grad_w, w2u.T)
        del grad_w, temp

        grad_w2d = torch.einsum("i r ..., i j ... -> r j", t2, grad_temp)
        grad_t2 = torch.einsum("i j ..., j r -> i r ...", grad_temp, w2d.T)
        del grad_temp
        return grad_t1, grad_w1d, grad_w1u, grad_t2, grad_w2d, grad_w2u, None


def make_weight(w1d, w1u, w2d, w2u, scale):
    return HadaWeight.apply(w1d, w1u, w2d, w2u, scale)


def make_weight_tucker(t1, w1d, w1u, t2, w2d, w2u, scale):
    return HadaWeightTucker.apply(t1, w1d, w1u, t2, w2d, w2u, scale)


def loha_diff_weight(w1d, w1u, w2d, w2u, t1=None, t2=None, gamma=1.0):
    """### loha_diff_weight

    Get ΔW = BA, where BA is low rank decomposition

    Args:
        w1d, w2d (torch.Tensor): weight of down proj linear/conv layer
        w1u, w2u (torch.Tensor): weight of up proj linear/conv layer
        gamma (float, optional): scale factor, normally alpha/rank here

    Returns:
        torch.Tensor: ΔW
    """
    if t1 is not None and t2 is not None:
        assert w1d.size(0) == t1.size(1)
        assert w1u.size(0) == t1.size(0)
        assert w2d.size(0) == t2.size(1)
        assert w2u.size(0) == t2.size(0)
        R, I = w1d.shape
        R, O = w1u.shape
        R, R, *k = t1.shape
        result = make_weight_tucker(t1, w1d, w1u, t2, w2d, w2u, gamma)
    else:
        assert w1d.size(0) == w1u.size(1)
        assert w2d.size(0) == w2u.size(1)
        R, I, *k = w1d.shape
        O, R, *_ = w1u.shape
        w1d = w1d.reshape(w1d.size(0), -1)
        w1u = w1u.reshape(-1, w1u.size(1))
        w2d = w2d.reshape(w2d.size(0), -1)
        w2u = w1u.reshape(-1, w2u.size(1))
        result = make_weight(w1d, w1u, w2d, w2u, gamma)

    result = result.reshape(O, I, *k)
    return result


FUNC_LIST = [None, None, F.linear, F.conv1d, F.conv2d, F.conv3d]


def loha_bypass_forward_diff(
    x, w1d, w1u, w2d, w2u, t1=None, t2=None, gamma=1.0, extra_args={}
):
    """### loha_bypass_forward_diff

    Args:
        x (torch.Tensor): input tensor
        w1d, w2d (torch.Tensor): weight of up proj linear/conv layer
        w1u, w2u (torch.Tensor): weight of down proj linear/conv layer
        gamma (float, optional): scale factor, normally alpha/rank here

    Returns:
        torch.Tensor: output tensor
    """
    diff_w = loha_diff_weight(w1d, w1u, w2d, w2u, t1, t2, gamma)
    return FUNC_LIST[w1d.dim() if t1 is None else t1.dim()](x, diff_w, **extra_args)


if __name__ == "__main__":
    w = torch.randn(128, 128, 3, 3, 3)
    a = torch.randn(16, 128) * 0.01
    b = torch.randn(16, 128) * 0.01
    m = torch.randn(16, 16, 3, 3, 3) * 0.01
    extra_args = {"padding": 1}

    x = torch.randn(1, 128, 8, 8, 8)
    y = FUNC_LIST[w.dim()](x, w, **extra_args)
    diff_w = loha_diff_weight(a, b, a, b, m, m, 1)
    diff_y = loha_bypass_forward_diff(x, a, b, a, b, m, m, 1, extra_args)

    print(F.mse_loss(y, y + diff_y))
    print(F.mse_loss(w, w + diff_w))
