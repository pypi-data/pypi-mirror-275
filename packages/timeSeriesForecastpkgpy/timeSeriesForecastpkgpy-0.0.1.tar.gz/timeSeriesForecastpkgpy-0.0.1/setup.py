from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A package that supports forecasting tasks in python'

# Setting up
setup(
    name="timeSeriesForecastpkgpy",
    version=VERSION,
    author="Miguel Vuori",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'plotly', 'statsmodels', 'matplotlib', 'numpy', 'sklearn', 'tensorflow'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)