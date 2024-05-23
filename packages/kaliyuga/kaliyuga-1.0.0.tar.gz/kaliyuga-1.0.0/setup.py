from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='kaliyuga',
    version='1.0.0',
    author='Fidal',
    author_email='mrfidal@proton.me',
    description='Kaliyuga: The Hindu-inspired hacking marvel. Unleash its potent arsenal for advanced cybersecurity. Exploit vulnerabilities, crack passwords, and analyze networks with divine precision. Harness its forensic prowess and generate impactful reports. Empowering defenders in the digital age.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mr-fidal/kaliyuga',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kaliyuga = kaliyuga.cli:main'
        ]
    },
    install_requires=[
        'requests',
        'beautifulsoup4',
        'scapy',
        'paramiko'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords=[
        'mrfidal',
        'kaliyuga',
        'cybersecurity',
        'hacking',
        'network analysis',
        'password cracking',
        'forensics',
        'exploitation',
        'security',
        'python'
    ],
)
