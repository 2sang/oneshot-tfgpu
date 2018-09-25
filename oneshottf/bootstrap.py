import yaml
import docker

def init_client():
    return docker.from_env()


def check_requirements():
    return True


def build_image_from_config(conf):
    pass


def load_config():
    with open('conf.yaml', 'r') as f:
        config = yaml.load(f)
    return config
        

def main():
    conf_dict = load_config()
    client = init_client(conf_dict)
    if not check_requirements():
        print("check requirement failed, exit.")
        return
    
    image = build_image_from_config()
    
        
if __name__ == "__main__":
    main()
