import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cdmn",
    version="2.1.2",
    author="Simon Vandevelde",
    author_email="s.vandevelde@kuleuven.be",
    description="A package providing a (c)DMN solver and API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://cdmn.be",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=['openpyxl==3.0.10', 'ply==3.11',
                      'numpy', 'python-dateutil',
                      'Levenshtein'],
    entry_points={
        'console_scripts': ['cdmn=cdmn.cdmn:main']
    }
)
