import torch.nn as nn
from torch.nn import DataParallel

model = MyModel().cuda()
model = DataParallel(model)

# Data automatically split across GPUs
output = model(input_data)