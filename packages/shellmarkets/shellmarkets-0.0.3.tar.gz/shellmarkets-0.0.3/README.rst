.. image:: https://img.shields.io/pepy/dt/shellmarkets
   :alt: Pepy Total Downlods



ShellMarkets
============

SHELLMARKETS v0.0.2 - by Croketillo

ShellMarkets is a command-line tool (CLI) for retrieving stock market
information. It uses the Yahoo Finance API to fetch data about specific
stocks and provides various options to display detailed information
about companies.

Installation
------------

You can install ShellMarkets directly from PyPI using ``pip``:

.. code:: bash

   pip install shellmarkets

Usage
-----

After installation, you can use the shmkt command to interact with the
tool. Below are the available options and usage examples.

Show Version
~~~~~~~~~~~~

To display the version of ShellMarkets:

.. code:: bash

   shmkt --version

Get Basic Information
~~~~~~~~~~~~~~~~~~~~~

To get basic information about one or more stocks:

.. code:: bash

   shmkt TICKER1 TICKER2 ...

Extended Information
~~~~~~~~~~~~~~~~~~~~

To get extended information about a specific stock:

.. code:: bash

   shmkt TICKER -e

Company Information
~~~~~~~~~~~~~~~~~~~

To get detailed information about the company:

.. code:: bash

   shmkt TICKER -i

Company News
~~~~~~~~~~~~

To get recent news about the company:

.. code:: bash

   shmkt TICKER --n

Show Portfolio
~~~~~~~~~~~~~~

To display the stocks in a portfolio file:

.. code:: bash

   shmkt -p /path/to/portfolio/file

Create a New Portfolio
~~~~~~~~~~~~~~~~~~~~~~

To create a new portfolio file with an optional list of stocks:

.. code:: bash

   shmkt -c /path/to/new/portfolio/file TICKER1 TICKER2 ...

Add a Stock to the Portfolio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a stock to an existing portfolio file:

.. code:: bash

   shmkt -a TICKER /path/to/portfolio/file

Remove a Stock from the Portfolio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To remove a stock from an existing portfolio file:

.. code:: bash

   shmkt -d TICKER /path/to/portfolio/file

Help
~~~~

.. code:: bash

   shmkt --help

Contributions
-------------

Contributions are welcome. Please open an issue or submit a pull request
on GitHub.

License
-------

This project is licensed under the GNU General Public License (GPL). See
the LICENSE file for details.
