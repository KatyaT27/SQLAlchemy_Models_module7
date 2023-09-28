# SQLAlchemy Models Module 7

This is a Python program that interacts with a PostgreSQL database using SQLAlchemy models. It provides various queries to retrieve and display information from the database.

## Setup required to run the program

-Docker must be installed on your system.
-Ensure you have the necessary Python packages by running pip install -r requirements.txt.
-Include any specific instructions for setting up the PostgreSQL database, if necessary.
-Mention that the program is designed to run within a Docker container.

## How to run the program. Include the following steps

-Clone or download the project repository.
-Open a terminal and navigate to the project directory.

git clone <https://github.com/KatyaT27/SQLAlchemy_Models_module7.git>
cd SQLAlchemy_Models_module7

-Build the Docker containers using docker-compose:
docker-compose up --build

-Access the Docker container with the following command:
docker run -it --entrypoint /bin/bash sqlalchemy_models_module7-students

-Inside the container, navigate to the /app directory:
cd /app

-Run the program by executing:
python main.py

-Follow the on-screen instructions to select and execute queries
