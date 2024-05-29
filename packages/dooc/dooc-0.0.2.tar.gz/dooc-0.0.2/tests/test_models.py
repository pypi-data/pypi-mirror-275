import torch
from dooc import models
import random


def test_MutSmiXAttention():
    smiles_src = torch.randint(0, 64, [2, 200])
    smiles_tgt = torch.randint(0, 64, [2, 200])
    mutations = [[random.choice([0, 1]) for _ in range(3008)],
                [random.choice([0, 1]) for _ in range(3008)]]
    mutations_src = torch.tensor(mutations, dtype=torch.float)
    model = models.MutSmiXAttention()
    out = model(smiles_src, smiles_tgt, mutations_src)
    assert out.shape == (2, 1)


def test_MutSmiFullConnection():
    smiles_src = torch.randint(0, 64, [2, 200])
    smiles_tgt = torch.randint(0, 64, [2, 200])
    mutations = [[random.choice([0, 1]) for _ in range(3008)],
                [random.choice([0, 1]) for _ in range(3008)]]
    mutations_src = torch.tensor(mutations, dtype=torch.float)
    model = models.MutSmiFullConnection()
    out = model(smiles_src, smiles_tgt, mutations_src)
    assert out.shape == (2, 1)
