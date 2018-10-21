from setuptools import setup, find_packages

setup(
    name="tfgpu",
    version="0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["tfgpu=tfgpu.app:main"]},

    install_requires=[
        'docker>=3.4',
        'pyyaml>=3.1',
        'fire>=0.1',
    ],

    author="Sang Su Lee",
    author_email="sangsulee92@gmail.com",
    description="Docker command line helper for tensorflow",
    license="MIT",
    keywords="docker tensorflow tensorflow-gpu",
)
