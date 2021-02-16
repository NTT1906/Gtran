import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="gtran",
	version="0.1.5",
	description="A free and unlimited Google translator.",
    long_description=README,
    long_description_content_type="text/markdown",
	author="NTT1906",
	author_email="nttispay@gmail.com",
	url="https://github.com/NTT1906/Gtran",
	python_requires=">3.2.0",
	license="MIT",
	packages=["gtran"],
	keywords="translate gtran gtrans Gtran",
	install_requires=[
		"pycurl",
		"urllib3"
	],
	classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "Topic :: Education",
	],
)