# PCIe
Open Source code for using PCIe-based AI accelerators (support for PCIe-based AI accelerators such as a GPU, FPGA, or ASICs from NVIDIA, AMD, Xilinx, Intel, and more) for both inference and training. Democratizing access to multimodal large language models, proving that accessing, high-performance LLM inference is achievable beyond centralized data centers and on the hardware people already own or plan to own.
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
For AMD GPUs: Use ROCm libraries and tools like ROCProfiler and ROCTrace for machine learning, computer vision, and mathematical computations.


7. Monitor and Debug
Use monitoring tools to ensure efficient usage of the PCIe accelerator:
NVIDIA: nvidia-smi
Intel: OpenVINO Benchmark Tool
Xilinx: Vitis AI Profiler

# AI hardware accelerator-agnostic AI Platform Factory
![AI Platform Factory](https://github.com/user-attachments/assets/423d5a85-9c8b-44dc-b47a-41ddce3c48d7)

