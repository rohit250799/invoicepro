This is an Invoice Management System built using Django web framework of Python and all the data is stored inside Postgres database. All the packages and libraries used are listed in the requirements.txt file.

To set it up in your local environment, you must have docker, python and any python supporting IDE installed as a prerequisite. For this project, I am creating a PostgreSQL database in Docker and its done in Ubuntu. You can do it just by following the instructions mentioned in this link: https://www.commandprompt.com/education/how-to-create-a-postgresql-database-in-docker/

First, start by cloning the repo and opening it in your preferred IDE.

Next, create a virtual environment by running the command -> python3 -m venv env(for ubuntu users). Or, create your virtual environment using the link: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

After the virtual environment is created, activate it using -> source env/bin/activate(for ubuntu users)

To store the environment variables to be used, create a .env file in the root directory of the project and store the db name, host, port, password etc. and through the terminal run the command -> source .env(for ubuntu users)

Customers:

To create new customers and view the existing ones, you can visit the link: http://0.0.0.0:8000/customers/ where 0.0.0.0 is the localhost address and :8000 is the port number that you have set up

![create customers](/media/coding/Python_projects/django_projects/coursera_projects/invoicePro/static/static_files/images/customer_creation.png)  

To update an existing customer, get his detailed view or delete customer, visit the link: http://0.0.0.0:8000/customers/id where id is the customer id(integer) example 134.

![update, get_detailed_view](/media/coding/Python_projects/django_projects/coursera_projects/invoicePro/static/static_files/images/update_customer.png)

![delete customer](/media/coding/Python_projects/django_projects/coursera_projects/invoicePro/static/static_files/images/delete_customer.png)

Offers/Estimates:

To create new estimates and view the existing ones, you can visit the link: http://0.0.0.0:8000/estimates/index/ where 0.0.0.0 is the localhost address and :8000 is the port number that is have set up

![create estimates](/media/coding/Python_projects/django_projects/coursera_projects/invoicePro/static/static_files/images/estimate_creation.png)