from setuptools import setup, find_packages

setup(
    name='ZeroXRequests',
    version='1.0',
    description='Requests for hackers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rafax00/ZeroXRequests',
    author='Rafax00',
    author_email='',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'requests',
        'h2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
