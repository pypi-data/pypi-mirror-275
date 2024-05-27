from setuptools import setup, find_packages

# LOADING DOCUMENTATION
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'CinetPay',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        'httpx',
        'simplejson',
        'colorlog',
        'pydantic'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = '#Einswilli',
    author_email = 'einswilligoeh@email.com',
    description = 'Python SDK for CinetPay Payment API. ',
    url = 'https://github.com/AllDotPy/CinetPay.git',
)