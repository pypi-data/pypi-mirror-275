from setuptools import setup, find_packages

setup(
    name='pdfzipcracker',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyPDF2',  
        'pyzipper', 
    ],
    entry_points={
        'console_scripts': [
            'pdfzipcrack=pdfzipcracker.pdfzipcrack:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
