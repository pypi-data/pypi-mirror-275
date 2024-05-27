from setuptools import setup, find_packages


setup(
    name='legopack',
    version='0.22',
    author='Remi Prince',
    description='personal',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn",
        "streamad"
    ],
    python_requires='>=3.8',
    zip_safe=False
)

# pip install .
# pip install setuptools wheel twine
# python setup.py sdist bdist_wheel
# twine check dist/*
# twine upload dist/* --username __token__
