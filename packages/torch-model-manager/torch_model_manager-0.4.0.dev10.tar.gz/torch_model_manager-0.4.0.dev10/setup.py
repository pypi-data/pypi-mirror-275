from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import subprocess


class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        subprocess.run(["bash", "init.sh"])
        install.run(self)



with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='torch-model-manager',
    version='0.4.0.dev10',
    description='A package for managing PyTorch models',
    author='Billal MOKHTARI',
    author_email='mokhtaribillal1@gmail.com',
    packages=find_packages(exclude=['tests', 
                                    'docs', 
                                    'build.sh', 
                                    'requirements.sh', 
                                    'resources.md',
                                    'torch_model_manager/src/run_ids.json',
                                    '.pypirc',
                                    'torch_model_manager/src/__pycache__',
                                    'torch_model_manager/src/.neptune',
                                    'upload.py']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Billal-MOKHTARI/torch-model-manager',
    keywords=['PyTorch', 'Deep Learning', 'Machine Learning', 'High Level Programming'],
    install_requires=[
        'torch',
        'numpy',
        'torchvision',
        'neptune',
        'torchviz',
        'torchcam',
        'colorama',
        'neptune_pytorch',
        'torchview',
        'graphviz',
        'wandb',
        'ydata_profiling',
        'diffusers',
        'transformers',
        'accelerate',
        'scipy',
        'safetensors',
        'supervision',
        'tqdm',
        'pycocotools',
        'opencv-python',
        'addict',
        'yapf',
        'timm'
        # Add any other dependencies here
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        'install dependencies': CustomInstallCommand,
    },
)