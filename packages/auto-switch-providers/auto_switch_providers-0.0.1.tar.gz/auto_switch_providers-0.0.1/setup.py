from pathlib import Path
import re

from setuptools import find_packages, setup


here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")
with open(here / "requirements.txt") as fp:
    install_reqs = [r.rstrip() for r in fp.readlines() if not r.startswith("#")]


def get_version():
    file = here / "src/auto_switch_providers/__init__.py"
    return re.search(
        r'^__version__ = [\'"]([^\'"]*)[\'"]', file.read_text(), re.M
    ).group(1)


setup(
    name="auto-switch-providers",
    version=get_version(),
    description="Auto Switch Providers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="fuongz",
    author_email="hi@phuongphung.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="",
    url="https://github.com/fuongz/auto_switch_providers",
    project_urls={
        "Bug Reports": "https://github.com/fuongz/auto_switch_providers/issues",
        "Source": "https://github.com/fuongz/auto_switch_providers",
    },
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8, <4",
    install_requires=install_reqs,
)
