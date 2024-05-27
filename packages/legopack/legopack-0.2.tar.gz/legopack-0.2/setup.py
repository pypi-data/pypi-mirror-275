from setuptools import setup, find_packages


setup(
    name='legopack',
    version='0.2',
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

# python3 -m build
# python3 -m twine upload --repository testpypi dist/*

# pip install setuptools wheel twine
# python setup.py sdist bdist_wheel
# twine check dist/*
# twine upload dist/* --username __token__
