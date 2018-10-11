# oneshot-tfgpu(WORK IN PROGRESS):
### Yet another docker management tool for tensorflow-gpu & jupyter notebook

### Getting Started
```bash
```

### WIP
```bash
# Init new config settings with a few Q/A
tfgpu init

# Run last successful container
tfgpu run

# Start a container the image named 'c1'
tfgpu run c1

# Set image '1' with other option(s), changes will be saved locally at conf.yaml
# See 'tfgpu set --help' to see all available options
tfgpu set 1 --tag=latest-gpu-py3

# Apply 'c1' container changes to corresponding image
tfgpu commit c1

# List all pulled images
tfgpu ls
```

### Todos & Features
- CircleCI, PyInquirer, python-fire
- Oneshot install only with a few configuration
- Stores multiple customized image instances -> restrict the number of countainer to one.
- Make tfgpu as direct shell command  DONE
- argparse(or abseil)  WIP
- Exception check for every scenario  WIP
- Automate docker, nvidia-docker installation process  WIP
- Image reset corrupted ones
- Docker commit, remove volume or supports other common commands.
- Docs for common use cases like ssh port forwarding, etc.

