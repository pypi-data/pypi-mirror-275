from setuptools import setup, find_packages
import os
import subprocess
from pathlib import Path

# Function to create the directory and file with correct permissions
def create_caddy_config():
    current_dir = Path().absolute()
    caddy_config_path = current_dir / 'caddy_config'
    caddyfile_path = caddy_config_path / 'Caddyfile'

    try:
        # Create directory if it doesn't exist
        if not caddy_config_path.exists():
            caddy_config_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {caddy_config_path}")

        # Create file if it doesn't exist
        if not caddyfile_path.exists():
            caddyfile_path.touch()
            print(f"Created file: {caddyfile_path}")

    except Exception as e:
        print(f"Error creating caddy config: {e}")

create_caddy_config()

setup(
    name='cadproxdk',
    version='4.0',
    author='Piotr Tamu (Thriveroute)',
    author_email='your.email@example.com',
    description='A tool to manage Caddy reverse proxy configurations with Cloudflare DNS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cadproxdk',
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
        'twine==4.0.2'
    ],
    entry_points={
        'console_scripts': [
            'cadprox=app.main:main',
        ],
    }
)
