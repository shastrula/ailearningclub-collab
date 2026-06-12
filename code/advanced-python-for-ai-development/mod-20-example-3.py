import torch

# Quantization
quantized = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear},
    dtype=torch.qint8
)

# Pruning
from torch.nn.utils import prune
prune.global_unstructured(
    model.parameters(),
    pruning_method=prune.L1Unstructured,
    amount=0.3
)