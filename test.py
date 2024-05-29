import torch

# GPUが利用可能かどうかを確認する
if torch.cuda.is_available():
    print('GPUが利用可能です')
else:
    print('GPUは利用できません')

# デバイスを取得する
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('デバイス:', device)

# テンソルをGPUに転送する
x = torch.tensor([1, 2, 3])
x = x.to(device)
print(x.device)
