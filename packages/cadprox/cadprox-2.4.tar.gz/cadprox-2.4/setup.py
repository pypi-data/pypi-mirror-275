#cadprox/setup.py
from setuptools import setup, find_packages
import subprocess
import sys

def check_caddy_installed():
    try:
        result = subprocess.run(['caddy', 'version'], capture_output=True, text=True, check=True)
        print(f"Caddy version: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print("Caddy is not installed or not found in PATH.")
        print("Please install Caddy before proceeding.")
        print("Refer to the installation guide: https://caddyserver.com/docs/install#debian-ubuntu-raspbian")
        sys.exit(1)
    except FileNotFoundError:
        print("Caddy is not installed or not found in PATH.")
        print("Please install Caddy before proceeding.")
        print("Refer to the installation guide: https://caddyserver.com/docs/install#debian-ubuntu-raspbian")
        sys.exit(1)

check_caddy_installed()

setup(
    name='cadprox',
    version='2.4',  # Increment the version number
    author='Piotr Tamu (Thriveroute.com)',
    author_email='nonyour@ssenisub.com',
    description='A tool to manage Caddy reverse proxy configurations with Cloudflare DNS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/reegen66/cadprox',  # Update with your GitHub repository URL
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
