#4. Optimize Data Transfer (Critical for PCIe)
#Reduce latency by batching data efficiently and minimizing PCIe transfers.
#Use pinned memory for faster host-to-device transfers:

# PyTorch
dataloader = torch.utils.data.DataLoader(dataset, batch_size=64, pin_memory=True)
