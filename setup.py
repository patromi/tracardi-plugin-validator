from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi_plugin_validator-0.10',
    version='0.2.1',
    description='The purpose of this plugin is valide data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Patryk Migaj',
    author_email='patromi123@gmail.com',
    packages=['tracardi_plugin_validator-0.10'],
    install_requires=[
        'aiofiles==0.7.0',
        'aiohttp==3.7.4.post0',
        'asgiref==3.4.1',
        'async-timeout==3.0.1',
        'asyncio==3.4.3',
        'attrs==21.2.0',
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'click==8.0.1',
        'colorama==0.4.4',
        'dateparser==1.0.0',
        'device-detector==0.10',
        'dotty-dict==1.3.0',
        'elasticsearch==7.13.4',
        'fastapi==0.65.2',
        'h11==0.12.0',
        'idna==3.2',
        'lark==0.11.3',
        'multidict==5.1.0',
        'numpy==1.20.3',
        'prodict==0.8.18',
        'pydantic==1.8.2',
        'python-dateutil==2.8.2',
        'python-multipart==0.0.5',
        'pytz==2021.1',
        'PyYAML==5.4.1',
        'regex==2021.7.6',
        'setuptools-scm==6.0.1',
        'six==1.16.0',
        'starlette==0.14.2',
        'tracardi-graph-runner==0.4.32',
        'tracardi-plugin-sdk==0.1.25',
        'typing-extensions==3.10.0.0',
        'tzlocal==2.1',
        'urllib3==1.26.6',
        'uvicorn==0.14.0',
        'xlrd==2.0.1',
        'yarl==1.6.3',
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)
