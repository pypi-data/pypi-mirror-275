from setuptools import setup, find_packages

setup(
    name='sdl-webui-lite',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    description='This web UI aims to ease up the control of any Python-based SDLs by displaying functions and their parameters dynamically.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ivory Zhang',
    author_email='ivoryzhang@chem.ubc.ca',
    license='MIT',
    install_requires=[
        'Flask-SocketIO',  # List all dependencies here
    ],
    url='https://gitlab.com/heingroup/sdl_webui_lite'
)
