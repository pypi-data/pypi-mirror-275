# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# zyx is open source
# use it however you want :)
#
# 2024 Hammad Saeed
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<

from setuptools import setup, find_packages

setup(
    name="zyx",
    version="0.1.90",
    author="Hammad Saeed",
    author_email="hammad@supportvectors.com",

    description="Lightspeed Python functions for the AI era.",

    python_requires=">3.8",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[

        "loguru", "pathlib", "rich", "tqdm",
        "instructor",
        "llama-index", "llama-index-llms-litellm", "llama-index-readers-web",
        "litellm",

])
