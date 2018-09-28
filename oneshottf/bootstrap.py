import os
import yaml
import docker
CONFIG_FILE = 'conf.yaml'
CONFIG_PATH = os.path.join(os.getcwd(), CONFIG_FILE)

def init_client():
    return docker.from_env()


def check_requirements():
    return True


def build_image_from_config(conf_dict):
    pass


def load_config(config_path=CONFIG_PATH):
    with open(config_path, 'r') as f:
        config = yaml.load(f)
    return config
        

def main():
    conf_dict = load_config()
    client = docker.from_env()
    if not check_requirements():
        print("check requirement failed, exit.")
        return
    
    image = build_image_from_config(conf_dict)
    
        
if __name__ == "__main__":
    main()
