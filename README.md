# oneshot-tfgpu:
### Yet another docker management tool only for tensorflow-gpu & jupyter notebook images
### Features
- Oneshot install only with a few configuration
- Able to store multiple customized image instances
- Make tfgpu as direct shell command 
- argparse(or abseil)
- Exception check for every scenario
- Automate docker, nvidia-docker installation process 
- Image reset from corrupted ones
- Docker commit, remove volume or supports other common commands.
- Docs for common practices, like ssh port forwarding, etc.

### Install
```bash
python3 install.py
```

### Usage
```bash
# Init new config settings with a few Q/A
tfgpu init

# Start a last image container
tfgpu run

# Start a container the image numbered 1
tfgpu run 1

# Set image 1 with other option(s), changes will be saved locally at conf.yaml
tfgpu set 1 --tag=latest-gpu-py3

# List all running tfgpu containers
tfgpu ps

# List all stored images
tfgpu ls
```

