from setuptools import setup, find_packages


setup(
    name='legopack',
    version='0.11',
    author='Remi Prince',
    description='personal purposes',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn",
        "streamad"
    ],
    zip_safe=False,
    python_requires='>=3.8'
)
# pip install setuptools wheel twine
# python setup.py sdist bdist_wheel
# twine check dist/*
# twine upload dist/*
