from setuptools import setup, find_packages

setup(
    name="CompactObject_TOV",
    version="1.9.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "pandas",
        "ultranest"  # This is the added dependency from your list that is not in the standard library
    ]
)
