from setuptools import setup, find_packages

setup(
    name="rottentomatoes-reviews-scraper",
    version="0.0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "requests",
        "pandas",
        "selenium"
    ],
    entry_points={
        'console_scripts': [
            'rottentomatoes-reviews-scraper=main:main',
        ],
    },
    author="Fami Ishikawa",
    author_email="s2222061@stu.musashino-u.ac.jp",
    description="A Python package to scrape movie data from Rotten Tomatoes, including titles and reviews.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HwaI12/rottentomatoes-reviews-scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
