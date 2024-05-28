from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='chatgpt_interface',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'selenium>=3.141.0',
        'webdriver-manager>=3.4.2',
    ],
    python_requires='>=3.6',
    author='SpicaNet',
    author_email='dev@spicanet.net',
    description='A Python interface for interacting with ChatGPT via web interface using Selenium',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/spicanet/ChatGPTInterface',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/spicanet/ChatGPTInterface/issues',
        'Source': 'https://github.com/spicanet/ChatGPTInterface',
    },
)
