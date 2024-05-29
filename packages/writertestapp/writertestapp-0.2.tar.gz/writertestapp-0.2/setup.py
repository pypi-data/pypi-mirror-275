from setuptools import setup, find_packages


setup(
    name='writertestapp',
    version='0.2',
    description='A simple writer app thats printing to the console',
    package_dir={'': 'simple_writer_app'},
    packages=find_packages(where='simple_writer_app'),
    long_description_content_type='text/markdown',
    author='Aleksander Likus',
    author_email='test@email.com',
    license='MIT',
    )
