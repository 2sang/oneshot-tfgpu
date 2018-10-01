import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='onehost-tfgpu',
    version='0.0.1',
    author='Sang Su Lee',
    author_email='sangsulee92@gmail.com',
    description='Simple tool that utilizes tf docker image',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/2sang/oneshot-tfgpu',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
    ]

)
