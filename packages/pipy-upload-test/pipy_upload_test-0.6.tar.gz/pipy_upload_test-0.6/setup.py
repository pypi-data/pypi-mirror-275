from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name='pipy_upload_test',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        'prompt_toolkit'
    ],
    entry_points={
        "console_scripts": [
            "pipy_upload_test = project.main:main"
        ]
    },
    long_description=description,
    long_description_content_type="text/markdown"
)
