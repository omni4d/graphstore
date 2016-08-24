Graphstore
==========
An implementation of a 4D model within a relational database with a RESTful api.

Getting Started
---------------

To run this project, you will need to install `Docker <https://docs.docker.com/>`_ on your machine.

Once Docker is installed and running, enter the following command from within the project folder to start the web and database servers:

.. code::

    docker-compose up

This will take several minutes the first time you run it as it needs to download and install all the necessary components into a docker container.

If successful, you should see the following messages at the end of the installation and configuration:

.. code::

    web_1  | Django version 1.9.8, using settings 'config.settings'
    web_1  | Starting development server at http://0.0.0.0:8000/
    web_1  | Quit the server with CONTROL-C.

and you can view the browseable API in your browser at http://localhost:8000

On OS X, you may need to use the IP address of your docker virtual machine rather then 'localhost' To find that address, use the following command:

.. code::

    docker-machine ip default
