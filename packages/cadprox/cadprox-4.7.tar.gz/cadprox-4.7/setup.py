from setuptools import setup, find_packages
import subprocess
import sys
import os

def check_caddy_installed():
    try:
        result = subprocess.run(['caddy', 'version'], capture_output=True, text=True, check=True)
        print(f"Caddy (system) version: {result.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Caddy (system) is not installed or not found in PATH.")
        print("Please install Caddy before proceeding.")
        print("Refer to the installation guide: https://caddyserver.com/docs/install#debian-ubuntu-raspbian")
        sys.exit(1)
    
    try:
        result = subprocess.run(['docker', 'exec', 'caddy', 'caddy', 'version'], capture_output=True, text=True, check=True)
        print(f"Caddy (Docker) version: {result.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Caddy (Docker) is not installed or not found.")
        print("Please ensure Docker is installed and the Caddy container is running if you intend to use Docker-based Caddy.")
        # Do not exit since system Caddy may still be used

check_caddy_installed()

# Ensure configuration directory exists
config_dir = os.path.expanduser('~/cadprox_config')
if not os.path.exists(config_dir):
    os.makedirs(config_dir)
    
# Ensure dummy Caddyfile exists
for caddyfile_name in ['Caddyfile', 'Caddyfile_docker']:
    caddyfile_path = os.path.join(config_dir, caddyfile_name)
    if not os.path.exists(caddyfile_path):
        with open(caddyfile_path, 'w') as f:
            f.write('localhost:80 {\n    reverse_proxy http://example.com\n}\n')


# Read the version from version.txt
with open("version.txt") as version_file:
    version = version_file.read().strip()

setup(
    name='cadprox',
    version=4.7,
    author='Piotr Tamu (Thriveroute.com)',
    author_email='nonyour@ssenisub.com',
    description='A tool to manage Caddy reverse proxy configurations with Cloudflare DNS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/reegen66/cadprox',
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
)
