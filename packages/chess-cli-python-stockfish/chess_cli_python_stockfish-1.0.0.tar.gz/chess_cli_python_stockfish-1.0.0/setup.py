from setuptools import setup, find_packages

setup(
    name="chess_cli_python_stockfish",  # Package name
    version="1.0.0",  # Initial version
    author="Tadeas Fort",
    author_email="taddy.fort@gmail.com",
    description="A tool to play against stockfish",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tadeasf/chess_cli",  # Project URL
    packages=find_packages(),
    install_requires=[
        "chess",
        "rich",
        "rich-click",
    ],
    entry_points={
        "console_scripts": [
            "chess-cli = chess_cli.chess_cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
