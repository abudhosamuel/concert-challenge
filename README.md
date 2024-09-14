Python Application

# Concert Management System

Concert Management System is a Python-based application that simulates a concert management domain using SQLAlchemy ORM to interact with a SQLite database. The program models relationships between Bands, Venues, and Concerts, showcasing how bands perform at various venues and allowing queries on concert-related data.

The key features of the system include:

Creating bands and venues.
Scheduling concerts where bands perform at venues on specific dates.
Querying to find out which band has performed the most, which venue has hosted the most frequent band, and much more.
Using SQLAlchemy ORM for seamless object-relational mapping and interactions with the database.

Key Concepts:
Band: Represents a music band with attributes like name and hometown.
Venue: Represents a concert venue with a title and city.
Concert: Represents a concert event that belongs to both a band and a venue, with a specified date.

Relationships:
A Band has many Concerts.
A Venue has many Concerts.
A Concert belongs to both a Band and a Venue, forming a many-to-many relationship between Bands and Venues through Concerts.

Requirements:
Python 3.x
SQLAlchemy (ORM)
SQLite (for database)
Alembic (optional, for migrations)




## Authors

- [@abudhosamuel](https://www.github.com/abudhosamuel)




## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)Deployment

Step 1: Install Dependencies
Ensure you have Python 3 installed on your machine. Then, install the required dependencies by running the following commands:

Install SQLAlchemy:

pip install sqlalchemy

(Optional) Install Alembic for Migrations:
pip install alembic

Step 2: Set Up the Database
After installing the dependencies, set up your SQLite database and create the necessary tables:

Run Database Setup: This will create the concerts.db SQLite database and initialize the tables (bands, venues, concerts).

python database_setup.py

(Optional) Apply Alembic Migrations: If you're using Alembic for version control of your database schema, make sure to initialize and apply any migrations:

alembic upgrade head

Step 3: Run the Program
Now that the database is set up, you can test the functionality by running the main script. The main.py script contains code to create bands, venues, and concerts, and to query the database.

python main.py

This will:

Create two bands: The Rolling Stones and Coldplay.
Create two venues: Wembley Stadium in London and Madison Square Garden in New York.
Schedule concerts and query to print information about the concerts and relationships.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

Acknowledgements

Font Awesome
Feel free to contribute to the project by submitting a pull request or opening an issue.

