import torch

# GPUが利用可能かどうかを確認する
if torch.cuda.is_available():
    print('GPUが利用可能です')
else:
    print('GPUは利用できません')
