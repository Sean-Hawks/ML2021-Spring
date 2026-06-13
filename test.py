import torch

print(f"PyTorch 版本: {torch.__version__}")
print(f"CUDA 是否可用: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"抓到的顯卡: {torch.cuda.get_device_name(0)}")
    print(f"目前 VRAM 分配: {torch.cuda.memory_allocated(0) / 1024**2:.2f} MB")