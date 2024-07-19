This is an Invoice Management System built using Django web framework of Python and all the data is stored inside Postgres database. 
All the packages and libraries used are listed in the requirements.txt file. 

To set it up in your local environment, you must have docker, python and any python supporting IDE installed as a prerequisite. For
this project, I am creating a PostgreSQL database in Docker and its done in Ubuntu. You can do it just by following the instructions 
mentioned in this link: https://www.commandprompt.com/education/how-to-create-a-postgresql-database-in-docker/

First, start by cloning the repo and opening it in your preferred IDE. 

Next, create a virtual environment by running the command -> python3 -m venv env(for ubuntu users). Or, create your virtual environment 
using the link: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

After the virtual environment is created, activate it using -> source env/bin/activate(for ubuntu users)

To store the environment variables to be used, create a .env file in the root directory of the project and store the db name, host,
port, password etc. and through the terminal run the command -> source .env(for ubuntu users)
