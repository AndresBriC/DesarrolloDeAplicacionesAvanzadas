# DesarrolloDeAplicacionesAvanzadas
> Repository for Sematic Segmentation Models

Andrés Briseño Celada | Salvador Federico Milanés Braniff | Juan Muniain Otero

Intro

## Prerequisites
- __Python Environment__: Python 3.10.x with CUDA toolkit v=11.8 or 12.1 is required. We recommend creating this environment using Miniconda. Follow these steps:

  1. [install miniconda](https://docs.anaconda.com/free/miniconda/). 
  2. Create a Python 3.10.x environment:
      ```bash
      conda create --name {env_name} python=3.10
      ```
  3. Activate the environment
      ```bash
      conda activate {env_name}
      ```
  4. If you have a GPU and wish to utilize it for training, install the CUDA toolkit:
     - Select version 11.8 or 12.1 from the [archive](https://developer.nvidia.com/cuda-toolkit-archive).
     - Install a CUDA-compatible version of Pytorch:
        ```bash
        pip install torch==2.3.0+cu{your_cuda_version} torchvision torchaudio
        ```
      Otherwise, install pytorch for CPU:
        ```bash
        pip install torch==2.3.0+cpu torchvision torchaudio -f https://download.pytorch.org/whl/torch_stable.html
        ```
  5. Install project dependencies
      ```cmd
      pip install -r requirements.txt
      ```
## Usage
To utilize the models provided in this repository:

- Follow the instructions provided in the respective model notebooks for loading pre-trained models, performing inference, or training on custom datasets.
- Ensure that the chosen environment is activated as the kernel when running the notebooks.
  
## Project Structure
```lua
DesarrolloDeAplicacionesAvanzadas/
└── Experiments/
    ├── version_123
    ├── version_125
    ├── version_126
    ├── version_134
    ├── version_135
    └── ! Missing
```
This structure represents the organization of experiments conducted within the project.

## References
- [(Canvas Activity)](README.md)
- [(Example .ipynb)](README.md)