from setuptools import setup, find_packages

setup(
    name="stellar_occultations",
    version="0.1.0",
    packages=["stellar_occultations"],
    install_requires=[
        "numpy",
        "pandas",
    ],
    author="Joel H. Castro-Chacón & Alvarez-Santana. F.I",
    python_requires=">=3.6",
)
