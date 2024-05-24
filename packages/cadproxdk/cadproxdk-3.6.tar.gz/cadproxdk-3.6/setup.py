from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        self.run_post_install()

    def run_post_install(self):
        subprocess.run(['python', 'post_install.py'])

setup(
    name='cadproxdk',
    version='3.6',  # Incremented version
    author='Piotr Tamu (Thriveroute)',
    author_email='your.email@example.com',
    description='A tool to manage Caddy reverse proxy configurations with Cloudflare DNS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cadproxdk',  # Update with your GitHub repository URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=[
        'requests==2.31.0',
        'dnspython==2.6.1',
        'boto3==1.34.112',
        'python-dotenv==1.0.1',
        'twine==4.0.2'  # Specify the version of twine to ensure compatibility
    ],
    entry_points={
        'console_scripts': [
            'cadprox=app.main:main',
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    }
)
