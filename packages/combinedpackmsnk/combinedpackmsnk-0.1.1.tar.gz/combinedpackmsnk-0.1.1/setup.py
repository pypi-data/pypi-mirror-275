from setuptools import setup, find_packages

setup(
    name='combinedpackmsnk',
    version='0.1.1',  # Increment the version number
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'seaborn',
        'matplotlib',
        'pandas',
        'nbconvert',
        'statsmodels',
        'ydata-profiling',
    ],
    entry_points={
        'console_scripts': [],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A comprehensive package for data analysis, data visualization, data preprocessing, and machine learning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo-name',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
