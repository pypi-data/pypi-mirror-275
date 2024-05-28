import setuptools


setuptools.setup(
    name="pokespeed",
    version="1.1.1",
    description="Calculate Pokemon speed tiers.",
    long_description="Run `pokespeed` to generate a csv of speed tiers.",
    url="https://github.com/evhub/pokespeed",
    author="Evan Hubinger",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "pypokedex",
        "beautifulsoup4",
        "tqdm",
        "clize",
    ],
    entry_points={
        "console_scripts": [
            "pokespeed = pokespeed:run_main",
        ],
    },
)
