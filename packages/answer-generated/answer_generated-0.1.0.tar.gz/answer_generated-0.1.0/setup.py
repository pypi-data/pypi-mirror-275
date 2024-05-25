from setuptools import setup, find_packages

setup(
    name='answer_generated',
    version='0.1.0',
    description='Generated python files for answer service',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Danya Talent',
    author_email='danyatalent@mail.ru',
    url='https://github.com/danyatalent/protos',
    license='MIT',
    packages=find_packages(where='gen/python'),
    package_dir={'': 'gen/python'},
    install_requires=[
        'grpcio',
        'protobuf',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
