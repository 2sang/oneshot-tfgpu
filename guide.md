# TFGPU: Guide to simplicity
## CLI tool for tensorflow docker image
You might think this tool useless, but just give it a try.  
You'll love this 

### Commands
```bash
# Init new config settings with a few Q/A
tfgpu init

# Run last successful container
tfgpu run

# Start & stop a container named 'c1' over the specified image 'image1'.
tfgpu run image1 --name=c1
tfgpu stop c1

# Set image 'image1' with other option(s), changes will be saved locally at conf.yaml
# See 'tfgpu set --help' to see all available options
tfgpu set image1 --tag=latest-gpu-py3
tfgpu set image1 --volume=~/myvolume

# Apply container changes to corresponding image
tfgpu commit c1


# List all pulled images
tfgpu ls
```
