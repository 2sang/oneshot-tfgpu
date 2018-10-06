# oneshot-tfgpu(WORK IN PROGRESS):
### Yet another docker management tool for tensorflow-gpu & jupyter notebook

### Todos & Features
- CircleCI
- Oneshot install only with a few configuration
- Able to store multiple customized image instances -> But controls only one container
- Make tfgpu as direct shell command  DONE
- argparse(or abseil)  WIP
- Exception check for every scenario  WIP
- Automate docker, nvidia-docker installation process  WIP
- Image reset from corrupted ones
- Docker commit, remove volume or supports other common commands.
- Docs for common use cases like ssh port forwarding, etc.
- IT DOES NOT ALLOW MULTIPLE CONTAINERS

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

# Start a container the image named 'c1'
tfgpu run c1

# Set image '1' with other option(s), changes will be saved locally at conf.yaml
tfgpu set 1 --tag=latest-gpu-py3

# Apply 'a' container changes to image '1'
tfgpu commit a:1

# List all running tfgpu containers
tfgpu ps

# List all stored images
tfgpu ls
```

