from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstallCommand(install):
    def run(self):
        # Run the pre-install script
        os.system("python -m dpdcyconfusion.pre_install")
        # Continue with the standard install
        install.run(self)

setup(
    name="dpdcyconfusion",
    version="0.1",
    packages=["dpdcyconfusion"],
    install_requires=[
        # Your dependencies here
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    author="dhxnush.ravi",
    author_email="your.email@example.com",
    description="A description of your package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://your.package.url",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
