from setuptools import setup, find_packages
import subprocess
import sys
import os

def check_caddy_installed():
    try:
        result = subprocess.run(['caddy', 'version'], capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        return False

def print_post_install_message():
    caddyfile_path = os.path.expanduser('~/caddy_config/Caddyfile')
    message = f"""
    CADProxy installation is complete!
    
    Please run the following Docker command to start Caddy with the appropriate configuration:

    sudo docker run -d --name caddy -p 8088:80 -p 8543:443 -v {caddyfile_path}:/etc/caddy/Caddyfile caddy

    Make sure the Caddyfile is located at {caddyfile_path}
    """
    print(message)

if not check_caddy_installed():
    print("Caddy is not installed on this system. Please install Caddy before proceeding.")
    print("See https://caddyserver.com/docs/install for installation instructions.")
    sys.exit(1)

from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print_post_install_message()

setup(
    name='cadproxdk',
    version='1.0',  # Initial version
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
        'requests',
        'dnspython',
        'boto3',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'cadprox=app.main:main',
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    }
)
