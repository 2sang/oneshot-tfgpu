def ask_tag():
    print("We're loading available tags from Dockerhub, please wait...")
    available_tags_by_version = utils.load_available_tags_by_version()
    select_version = [{
        'type': 'list',
        'name': 'version',
        'message': 'Choose tensorflow image version you want to fetch:',
        'choices': sorted(available_tags_by_version.keys(), reverse=True)
    }]
    answer = prompt(select_version, style=custom_style_1)
    version = answer['version']

    select_tag = [{
        'type': 'list',
        'name': 'tag',
        'message': 'Choose specific tag:',
        'choices': sorted(available_tags_by_version[version], reverse=True)
    }]
    answer = prompt(select_tag, style=custom_style_1)
    return answer['tag']


def create_new_image_prompt():
    selected_tag = ask_tag()
    questions = [
        {
            'type': 'input',
            'name': 'host_mountpath',
            'message': 'Mount path of Docker Volume in your local filesystem:',
            'default': '~/tfgpu/'
        },
        {
            'type': 'input',
            'name': 'container_mountpath',
            'message': 'Mount path on the container that will synchronize with the local mount path:',
            'default': '/notebooks/'
        },
        {
            'type': 'input',
            'name': 'volume_name',
            'message': 'name for the docker volume:',
            'default': 'tfgpu_volume'
        },
        {
            'type': 'input',
            'name': 'local_port',
            'message': 'local port number for accessing jupyter notebook:',
            'default': '9999'
        },
    ]
    answer = prompt(questions, style=custom_style_1)
    return True

    default_config = conf['images']['default']
    new_config = {}
    utils.update_conf()
