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

### Getting Started
```bash
git clone https://github.com/EpisysScience/oneshot-tfgpu && \
cd oneshot-tfgpu && python3 -m tfgpu.install 
```

### Usage
```bash
# Init new config settings with a few Q/A
tfgpu init

# Start a last image container
tfgpu run

# Start a container the image named '1'
tfgpu run 1

# Set image '1' with other option(s), changes will be saved locally at conf.yaml
tfgpu set 1 --tag=latest-gpu-py3

# Apply 'a' container changes to image '1'
tfgpu commit a:1

# List all running tfgpu containers
tfgpu ps

# List all stored images
tfgpu ls
```

