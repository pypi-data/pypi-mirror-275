from setuptools import setup, find_packages


setup(
    name='legopack',
    version='0.12',
    author='Remi Prince',
    description='personal purpose',
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
