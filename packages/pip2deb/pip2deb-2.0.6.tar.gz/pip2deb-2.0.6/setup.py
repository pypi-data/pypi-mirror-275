from setuptools import setup, find_packages

def readme():
    with open('README.rst', 'r') as f:
        content = f.read()
    return content

setup(
    name="pip2deb",
    version="2.0.6",
    decription="A Simple Tool to Pack Python Project into a Debian Package, For Debian/Ubuntu and Termux",
    long_description=readme(),
    url='https://github.com/pacspedd/pip2deb',
    author="PacSpedd",
    author_email="pacspedd@outlook.com",
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(),
    scripts=['pip2deb-bash', 'pip2deb-python', 'python-pip2deb', 'bash-pip2deb']
)
