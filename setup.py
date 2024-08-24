# setup.py
from setuptools import setup, find_packages

setup(
    name='cnnClassifier',
    version='0.1',
    description='A CNN Classifier for skin disease detection',
    author='Jay Dhameliya',
    author_email='ravi.galathiya@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'tensorflow', 'scikit-learn', 'imblearn', 'PyYAML', 'dvc'
    ],
    entry_points={
        'console_scripts': [
            'cnnClassifier=cnnClassifier.__main__:main',
        ],
    },
)
