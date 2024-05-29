from setuptools import setup, find_packages

setup(
    name="ML-Inz-example",
    version="0.0.1",
    description="A project with Flask backend and ML service for search answers in documents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Anton Loiko",
    author_email="loikoanton@yandex.ru",
    url="https://github.com/Appjey/ML-Inz-example.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "jinja2",
        "requests",
        "diffusers",
        "torch",
        "GPUtil",
        "numba",
        "flask-cors"
    ],
    entry_points={
        "console_scripts": [
            "backend = backend.app.main:app",
            "ml_service = ml_service.app.main:app"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
