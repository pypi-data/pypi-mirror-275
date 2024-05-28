from setuptools import setup, find_packages

setup(
    name='chatgpt_interface',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver-manager',
    ],
    author='SpicaNet',
    author_email='dev@spicanet.net',
    description='A Python interface for interacting with ChatGPT via web interface using Selenium',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/spicanet/ChatGPTInterface',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
