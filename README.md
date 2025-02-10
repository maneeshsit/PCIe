# PCIe
o modify your run.ai code for using a PCIe-based AI accelerator (such as a GPU, FPGA, or ASIC like NVIDIA, Xilinx, or Intel accelerators) for both inference and training
1. Set Up the PCIe AI Accelerator
Install the required drivers and SDKs for your PCIe accelerator. For example:
NVIDIA GPUs: Install CUDA and cuDNN.
Intel accelerators: Install OpenVINO Toolkit.
Xilinx FPGAs: Install Vitis AI runtime.
Ensure the PCIe device is visible via tools like lspci (Linux) or equivalent commands.

2. Modify Training Code
Use the appropriate deep learning framework and ensure device targeting is set to the PCIe accelerator. Examples:

