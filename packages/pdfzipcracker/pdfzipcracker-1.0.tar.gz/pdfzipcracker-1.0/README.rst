pdfzipcracker
=============

pdfzipcracker is a Python package designed to help you crack passwords for encrypted ZIP and PDF files using brute-force techniques.

Features
--------

- Crack passwords for encrypted ZIP files.
- Crack passwords for encrypted PDF files.
- Flexible options to specify character sets and password lengths.

Installation
------------

You can install pdfzipcracker via pip:

.. code-block:: bash

    pip install pdfzipcracker

Usage
-----

To use pdfzipcracker, run the script and follow the on-screen instructions:

.. code-block:: bash

    pdfzipcracker

You will be prompted to choose between cracking a PDF or a ZIP file, and then to provide necessary details about the expected password characteristics.

Crack a ZIP Password
--------------------

.. code-block:: text

    Enter ZIP File Path: /path/to/yourfile.zip
    Is The Password Contains Numbers? (if don't know, enter 'yes') (yes / no): yes
    Is The Password Contains Characters? (if don't know, enter 'yes') (yes / no): yes
    Is The Password Contains Special Characters? (if don't know, enter 'yes') (yes / no): no
    Enter Exact Length Of Password If You know Else Enter 'n': n
    Enter Maximum Guessed Password Length (e.g., 6 numbers or 9 characters): 6

Crack a PDF Password
--------------------

.. code-block:: text

    Enter PDF File Path: /path/to/yourfile.pdf
    Is The Password Contains Numbers? (if don't know, enter 'yes') (yes / no): yes
    Is The Password Contains Characters? (if don't know, enter 'yes') (yes / no): yes
    Is The Password Contains Special Characters? (if don't know, enter 'yes') (yes / no): no
    Enter Exact Length Of Password If You know Else Enter 'n': n
    Enter Maximum Guessed Password Length (e.g., 6 numbers or 9 characters): 6

License
-------

This project is licensed under the MIT License. See the `LICENSE.txt <https://github.com/yourusername/pdfzipcracker/blob/main/LICENSE.txt>`_ file for more details.

Contributing
------------

Contributions are welcome! Please fork the repository and submit a pull request.

Support
-------

If you have any questions or issues, please open an issue in the GitHub repository.

Acknowledgments
---------------

This package uses the following libraries:

- `pyzipper <https://github.com/mnooner256/pyzipper>`_
- `PyPDF2 <https://github.com/mstamy2/PyPDF2>`_

