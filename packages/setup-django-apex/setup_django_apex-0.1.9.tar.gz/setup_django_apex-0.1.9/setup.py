from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

# class CustomInstallCommand(install):
#     def run(self):
#         # Custom pre-installation steps can go here
#         install.run(self)
#         # Custom post-installation steps can go here
#         print("Custom installation steps completed.")
#         subprocess.run(["echo", "Post-installation script executed."])

# Read the license file
with open('LICENSE') as f:
    license_text = f.read()

setup(
    name='setup_django_apex',
    version='0.1.9',
    author='Anirudha Udgirkar',
    author_email='anirudhaudgirkar.work.email@example.com',
    description='A library to set up Django projects with multiple apps',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Anirudha1821/setup_django_apex',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'Django>=3.0',
    ], 
    # cmdclass={
    #     'install': CustomInstallCommand,
    # },
    entry_points={
        'console_scripts': [
            'setup_django=setup_django_apex.installer:create_django_project',
            'setup_django_drf=setup_django_apex.installer:create_django_drf_project',
        ],
    },
    # Include license file
    license=license_text,
)
