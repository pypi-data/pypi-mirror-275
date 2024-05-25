from setuptools import setup, find_packages

setup(
    name="unique_pdf_reader",  # Update this line
    version="0.1.0",
    description="A package to read PDF files aloud",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "pyttsx3"
    ],
    entry_points={
        'console_scripts': [
            'unique-pdf-reader=unique_pdf_reader:main',  # Update this line if necessary
        ],
    },
)
