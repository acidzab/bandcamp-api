from setuptools import *

setup(
    name="bandcamp_api",
    version="0.2.4",
    description="Obtains information from bandcamp.com. Forked from RustyRin project",
    author="AcidZab",
    packages=['bandcamp_api'],
    url="https://github.com/acidzab/bandcamp-api",
    install_requires=["setuptools", "beautifulsoup4", "demjson3", 'html5lib', 'lxml', "requests", "pycurl"],
    keywords=["api", "bandcamp"],
    zip_safe=False
    )
