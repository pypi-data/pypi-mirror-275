import tntorch as tn
import pytest
import numpy as np
import torch
torch.set_default_dtype(torch.float64)


torch.manual_seed(1)


def test_construction():
    m = torch.rand(11 * 3, 23 * 2)

    input_dims = [11, 3]
    output_dims = [23, 2]
    ranks = [50]

    ttm = tn.TTMatrix(m, input_dims=input_dims, output_dims=output_dims, ranks=ranks)
    assert torch.allclose(m, ttm.torch())

    cpm = tn.CPMatrix(m, input_dims=input_dims, output_dims=output_dims, rank=ranks[0])
    assert torch.allclose(m, cpm.torch())


def test_tt_multiply():
    m = torch.rand(11 * 3, 23 * 2)
    v = torch.rand(30, 11 * 3)  # Note: batch = 30, 11 * 3 features

    input_dims = [11, 3]
    output_dims = [23, 2]
    ranks = [50]

    ttm = tn.TTMatrix(m, input_dims=input_dims, output_dims=output_dims, ranks=ranks)
    assert torch.allclose(v @ m, tn.tt_multiply(ttm, v))

    cpm = tn.CPMatrix(m, input_dims=input_dims, output_dims=output_dims, rank=ranks[0])
    assert torch.allclose(v @ m, tn.cp_multiply(cpm, v))


def test_trace():
    input_dims = [11, 3]
    output_dims = input_dims
    m = torch.rand(np.prod(input_dims), np.prod(output_dims))
    ranks = [50]

    ttm = tn.TTMatrix(m, input_dims=input_dims, output_dims=output_dims, ranks=ranks)
    assert torch.allclose(torch.trace(m), ttm.trace())
