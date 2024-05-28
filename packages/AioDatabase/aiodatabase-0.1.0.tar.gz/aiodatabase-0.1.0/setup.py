from setuptools import setup, find_packages

setup(
    name="AioDatabase",
    version="0.1.0",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=["PyYAML", "aiomysql", "aiosqlite"],
    entry_points={
        "console_scripts": [
            "aiodatabase=src.AioDatabase:main",
        ],
    },
    package_data={
        "": ["queries.sql", "config.yml"],
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
