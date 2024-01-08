# phase3-project

## Blood Donation System

This is a Python application that allows users to manage blood donations and donors. The application uses SQLAlchemy ORM to create and modify a database with 3+ related tables.

## Installation
Clone the repository to your local machine.

Install the required dependencies using pipenv install.

Create a .env file in the root directory of the project and add the following line:

DATABASE_URL=sqlite:///blood_bank.db

This sets the database URL to a SQLite database named blood_bank.db. You can change this to a different database if you prefer.

## Usage
Open a terminal or command prompt.
Navigate to the directory where the Python file is located using the cd command.
Activate the virtual environment using pipenv shell.
Run the Python file using the python main.py command.
The application will create the necessary database tables and add a sample donor and donation record. It will then display the contents of the donors table in a table format.

You can modify the code to add more donors and donations, or to perform other operations on the database.

## Requirements
Python 3.x
SQLAlchemy
PrettyTable

## License
This project is licensed under the MIT License. See the LICENSE file for details.