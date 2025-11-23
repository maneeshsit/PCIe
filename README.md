# PCIe
This repository contains the Open Source Software (OSS) components of PCIe-based AI accelerators (support for PCIe-based AI accelerators such as GPUs, FPGAs, ASICs from NVIDIA, AMD, Xilinx, Intel, Huawei and more) for both inference and training. Democratizing access to multimodal large language models, proving that accessing high-performance LLM inference is achievable beyond centralized data centers and on the hardware people already own or plan to own thereby maximizing hardware efficiency and increasing accessibility. These open source software components are a subset of the General Availability (GA) release with some extensions and bug-fixes.

1. Set Up the PCIe AI Accelerator
Install the required drivers and SDKs for your PCIe accelerator. For example:
NVIDIA GPUs: Install CUDA and cuDNN.
Intel accelerators: Install OpenVINO Toolkit.
Xilinx FPGAs: Install Vitis AI runtime.
Ensure the PCIe device is visible via tools like lspci (Linux) or equivalent commands.

2. Modify Training Code
Use the appropriate deep learning framework and ensure device targeting is set to the PCIe accelerator. Examples:

3. and 4.  code files

5. Use Accelerator-Specific Optimizations
For NVIDIA GPUs: Use TensorRT for inference optimization.
For Intel FPGAs: Use OpenVINO's optimized inference engine.
For Xilinx FPGAs: Use Vitis AI tools for quantization and deployment.
For AMD GPUs: Use ROCm libraries and tools for machine learning, computer vision, and mathematical computations.


7. Monitor and Debug
Use monitoring tools to ensure efficient usage of the PCIe accelerator:
NVIDIA: nvidia-smi
Intel: OpenVINO Benchmark Tool
Xilinx: Vitis AI Profiler
AMD: ROCProfiler and ROCTrace

# AI hardware accelerator-agnostic AI Platform Factory
![AI Platform Factory](https://github.com/user-attachments/assets/423d5a85-9c8b-44dc-b47a-41ddce3c48d7)

