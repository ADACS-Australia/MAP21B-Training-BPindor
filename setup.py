import setuptools
import skysim

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

reqs = ['numpy>=1.19', ]

setuptools.setup(
    name="SkySim",
    version=skysim.__version__,
    author=skysim.__author__,
    author_email="author@example.com",
    description="Simulate sky locations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevOne/sky_sim",
    scripts=['sim_catalog'],
    python_requires=">=3.6",
)
