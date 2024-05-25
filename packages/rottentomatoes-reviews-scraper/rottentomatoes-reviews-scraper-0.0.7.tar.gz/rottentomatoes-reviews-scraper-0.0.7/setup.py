from setuptools import setup, find_packages

setup(
    name="rottentomatoes-reviews-scraper",
    version="0.0.7",  # バージョンを更新
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "requests",
        "pandas",
        "selenium==4.9.0"
    ],
    entry_points={
        'console_scripts': [
            'rottentomatoes-reviews-scraper=rottentomatoes_reviews_scraper.main:main',
        ],
    },
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
