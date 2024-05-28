import setuptools

with open("README.md", "r",encoding='UTF-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name="ble_library",
    py_modules=['ble_library'],
    version="1.0.0",
    author="kocoafab",
    author_email="kocoafab@kocoa.or.kr",
    description="Library for Using Bluetooth on ESP32 Board.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://kocoafab.cc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )