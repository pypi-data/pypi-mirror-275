from setuptools import setup, find_packages

setup(
    name="AioDatabase",
    version="0.1.6",
    install_requires=["PyYAML", "aiomysql", "aiosqlite"],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={
        "": ["resources/sqlite.sql", "resources/config.yml"],
    },
    include_package_data=True,
    description="AioDatabase is a simple database abstraction layer for SQLite and MySQL.",
    author="AmitxD",
    url="https://github.com/Amitminer/AioDatabase",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
