from setuptools import setup, find_packages
import os
from setuptools.command.install import install
from pathlib import Path

def create_caddy_config():
    current_dir = Path().absolute()
    caddy_config_path = current_dir / 'caddy_config'
    caddyfile_path = caddy_config_path / 'Caddyfile'

    if not caddy_config_path.exists():
        caddy_config_path.mkdir(parents=True)
        print(f"Created directory: {caddy_config_path}")

    if not caddyfile_path.exists():
        caddyfile_path.touch()
        print(f"Created file: {caddyfile_path}")

def print_post_install_message():
    current_dir = Path().absolute()
    caddyfile_path = current_dir / 'caddy_config' / 'Caddyfile'
    message = f"""
    CADProxy installation is complete!
    
    Please run the following Docker command to start Caddy with the appropriate configuration:

    docker run -d --name caddy -p 8088:80 -p 8543:443 -v {caddyfile_path}:/etc/caddy/Caddyfile caddy

    Make sure the Caddyfile is located at {caddyfile_path}
    """
    print(message)

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        create_caddy_config()
        print_post_install_message()

setup(
    name='cadproxdk',
    version='3',  # Incremented version
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
        'install': PostInstallCommand,
    }
)
