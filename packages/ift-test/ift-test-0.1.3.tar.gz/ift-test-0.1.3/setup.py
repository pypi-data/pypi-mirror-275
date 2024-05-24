from setuptools import setup, find_packages


setup(
    name="ift-test",
    version="0.1.3",
    authors="Lea Tonejca, Julian Zulehner",
    author_email="julian.zulehner@gmail.com",
    description="IFT test PyPi Version",
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url="https://git.ift.tuwien.ac.at/lab/ift/sis/data-science/nxopen-export/-/tree/lea?ref_type=heads",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ift-test': ['static/*.prt', 'static/*.csv', 'static/*.txt', 'static/*.json', 'build/*.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
