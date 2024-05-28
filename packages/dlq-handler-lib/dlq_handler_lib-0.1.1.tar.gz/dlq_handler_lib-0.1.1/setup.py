from setuptools import setup, find_packages

setup(
    name="dlq_handler_lib",
    version="0.1.1",
    description="A library for handling DLQ messages in AWS SQS",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MarceloJay/lambda-dlq-reprocess-message.git",
    author='Marcelo Ferreira',
    author_email='jaytilangus@gmail.com',
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "dlq_handler_lib"},
    install_requires=[
        "boto3>=1.16.0",
        "mock>=4.0.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)