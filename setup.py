from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='smudge',
    version='0.0.1',
    description='Performs passive OS detection based on SYN packets without transmitting any data.',
    py_modules=["smudge"],
    package_dir={'': 'smudge'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Networking :: Monitoring",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independant",
    ],
    install_requires=[
        "scapy ~= 2.4.5",
    ],
    extras_require = {
        "dev": [
            "pylint>=2.15.0",
        ],
    },
    url="https://github.com/activecm/smudge",
    author="Dave Quartarolo",
    author_email="david@activecountermeasures.com",
)
