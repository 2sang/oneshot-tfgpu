import os
import docker
import yaml


def check_prerequisites():
    return True;

def load_conf(yaml_path='./conf.yaml'):
    with open(yaml_path, 'r') as f:
        return yaml.load(f)

def install():
    if os.path.exists('~/.tfgpu'):
        return True;
    with open('~/.tfgpu', 'w') as tfgpu_f:
        tfgpu_f.write("")



def main():
    # Todo: Sanity check for --runtime=nvidia option Mon 01 Oct 2018 12:42:35 PM KST
    if not (check_prerequisites()):
        print("prerequisites not satistied")
        return
    
    conf = load_conf('conf.yaml')
    install()

if __name__ == "__main__":
    main()
