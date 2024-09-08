This is an Invoice Management System built using Django and all the data is stored inside a Postgres database. All the packages and libraries used are listed in the requirements.txt file. OS used: Ubuntu

For this project, I have containerized the database in local using Docker for ease of use. You can do it just by following the instructions mentioned in this link: : https://www.commandprompt.com/education/how-to-create-a-postgresql-database-in-docker/

To set it up in your local environment, you must have docker, python and any python supporting IDE installed as a prerequisite. 
First, start by cloning the repo and opening the project in your preferred IDE.

Next, create a virtual environment by running the command -> python3 -m venv env(for ubuntu users). Or, create your virtual environment using the link: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

After the virtual environment is created, activate it using -> source env/bin/activate(for ubuntu users)

To store the environment variables to be used, create a .env file in the root directory of the project and store the db name, host, port, password etc. and through the terminal run the command -> source .env(for ubuntu users)

Tools used:
1. Insomnia for API Testing
2. Mailtrap for mail testing

Customers:

To create new customers and view the existing ones, you can visit the link: http://0.0.0.0:8000/customers/ where 0.0.0.0 is the localhost address and :8000 is the port number that you have set up

![create customers](/static/static_files/images/customer_creation.png) 

To update an existing customer, get his detailed view or delete customer, visit the link: http://0.0.0.0:8000/customers/id where id is the customer id(integer) example: 134.

![update, get_detailed_view](/static/static_files/images/update_customer.png)

![delete customer](/static/static_files/images/delete_customer.png)

Offers/Estimates:

To create new estimates and view the existing ones, you can visit the link: http://0.0.0.0:8000/estimates/index/ where 0.0.0.0 is the localhost address and :8000 is the port number that is have set up

![create estimates](/static/static_files/images/estimate_creation.png)

To generate an estimate in pdf format, you have to send a GET request to the url: http://0.0.0.0:8000/estimates/pdf_view/14 where 0.0.0.0 is the localhost address and :8000 is the port number that is have set up

![generate estimate in pdf](/static/static_files/images/generate_pdf.png)

For email testing, I have used Mailtrap tool.

To send estimate to a customer, send a POST request to the url: http://0.0.0.0:8000/estimates/send_estimate/13/ where 13 is the estimate_id (primary key) 

![send estimate to customer](/static/static_files/images/send_estimate_mail.png)

