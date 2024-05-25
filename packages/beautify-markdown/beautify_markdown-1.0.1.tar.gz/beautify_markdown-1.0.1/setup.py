from setuptools import setup, find_packages

setup(
    name="beautify_markdown",
    version="1.0.1",
    author="Tadeas Fort",
    author_email="taddy.fort@gmail.com",
    description="A tool to beautify markdown output from chatgpt-cli (https://github.com/marcolardera/chatgpt-cli)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tadeasf/beautify_markdown",
    packages=find_packages(),
    install_requires=["rich", "pyperclip"],
    entry_points={
        "console_scripts": [
            "beautify_markdown = beautify_markdown.beautify_markdown:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
