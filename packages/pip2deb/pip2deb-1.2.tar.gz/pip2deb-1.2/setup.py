from setuptools import setup

def readme():
    with open('README.rst', 'r') as f:
        content = f.read()
    return content

setup(
    name='pip2deb',
    version='1.2',
    license='MIT',
    description='Package PIP Module as .deb, and this in under 1.5 minutes',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    author='PacSpedd',
    author_email='pacspedd@outlook.com',
    url='https://github.com/pacspedd',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    scripts=['pip2deb'],
)
