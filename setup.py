from setuptools import setup, find_packages

setup(
    name="operaciones_fechas",
    version="1.0.0",
    author="Diego Manzano",
    author_email="diegomanzano23@hotmail.com",
    description="Un paquete para realizar operaciones con fechas en Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/diegomanzano23/fecha_utils.git",
    packages=find_packages(),
    install_requires=[
        "datetime"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)