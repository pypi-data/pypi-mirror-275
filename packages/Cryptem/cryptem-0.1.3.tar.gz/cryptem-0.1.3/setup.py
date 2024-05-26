import setuptools
import os
import sys
sys.path.append(os.path.dirname(__file__))
if True:    # just to sto my IDE's script formatter moving the following import to the start of the script
    from __project__ import project_name, version
with open(os.path.join(os.path.dirname(__file__), "ReadMe.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=project_name,
    version=version,
    author="emendir",
    description="Cryptographic applications library based on elliptic curve cryptography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ipfs.io/ipns/k2k4r8ld8q6344t8dop0rwuk8f3vhpo42un6zrnrffogaayr7xv59p83",

    project_urls={
        "Source Code on IPFS": "https://ipfs.io/ipns/k2k4r8ld8q6344t8dop0rwuk8f3vhpo42un6zrnrffogaayr7xv59p83",
        "Github": 'https://github.com/emendir/Cryptem-Python',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # 'package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    py_modules=['cryptem', 'Cryptem'],
    install_requires=['eciespy', 'coincurve', 'cryptography'],
)
