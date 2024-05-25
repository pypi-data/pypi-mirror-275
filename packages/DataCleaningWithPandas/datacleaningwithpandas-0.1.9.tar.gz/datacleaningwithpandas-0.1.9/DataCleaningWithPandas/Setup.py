from setuptools import setup, find_packages

setup(
    name='DataCleaningWithPandas',
    version='0.1.9',
    description='A data preprocessing library',
    author='Muhammed Furkan Akdag & Ahmet Akif Apari',
    author_email='furkanakdag.3469@gmail.com',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
    ],
)
