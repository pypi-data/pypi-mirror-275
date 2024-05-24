from setuptools import setup, find_packages

setup(
    name='cdproxy',
    version='1.4',  # Increment the version number
    author='Piotr Tamu (Thriveroute)',
    author_email='your.email@example.com',
    description='A tool to manage Caddy reverse proxy configurations with Cloudflare DNS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cdproxy',  # Update with your GitHub repository URL
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
            'cdprox=cdprox.main:main',
        ],
    },
)
