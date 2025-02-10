# 3. Modify Inference Code
# Optimize your inference pipeline by loading pre-trained models onto # the PCIe accelerator and running all computations on it.

# PyTorch Inference:
model.eval()  # Set model to evaluation mode
model = model.to(device)  # Move model to accelerator

with torch.no_grad():  # Disable gradient calculations
    inputs = inputs.to(device)  # Move inputs to accelerator
    outputs = model(inputs)  # Perform inference
