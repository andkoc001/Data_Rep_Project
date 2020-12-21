# Data_Rep_Project

Data Representation Project, GMIT 2020-2021

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

___

## Introduction

This is my assignment project to Data Representation module, Galway-Mayo Institute of Technology, 2020.

This GitHub repository documents my research, project progress (git version control) and findings of the assignment project - a Web Application deployment.

In this README.md file I have incorporated the research and described the project progress. It is illustrated with the applied concepts and methods together with relevant code snippets.

The project is based predominantly and heavily on the lecture materials. The reference to the lecture materials is not specifically provided. General resources are listed at the bottom of this README.md file. More specific references are provided the text body when applicable. The project source code and resources are also available on this GitHub [repository](https://github.com/andkoc001/Data_Rep_Project.git).

### Project objectives

The objective of the is to develop a web service to access, display, modify etc. data from an API using Flask back-end framework and other tools commonly used in the industry, such as Python programing language, Flask, Git, etc. as required.

The goal of the project is to produce a web app that will do the following:

- Consuming a RESTful API, either in Python (server) or javascript (client)
- Running the server
- CRUD operations on data (create, read, update, delete)
- Web frontend to display data and interact with server.

The detailed project instruction can be found in the [file]<https://github.com/andkoc001/Data_Rep_Project.git/blob/main/Project%20Description.pdf>  

___

## Assignment delivery

The project is delivered so that it can be accessed in two ways:

1. By setting up a local server (see below instructions).
2. Depoloyed on the PythonAnywhere server. It is accessible at the following address: [andkoc001.pythonanywhere.com](andkoc001.pythonanywhere.com).
 
**Note**: The web app requires credential authentication. For the purpose of this assignment use >> **gmit** << for both user name and password.

## To access the Project on localhost

Please follow the below steps to set up a local host server.

### 1. Download the repository content

  Go to <https://github.com/andkoc001/Data_Rep_Project.git> website and, click on 'Code' button and then 'Download ZIP'. Unzip the downloaded file on your hard drive.

### 2. Set up the environment

  Ensure all the required modules are installed. In the folder, where the repository has been unzipped, start the terminal (Linux systems, on Windows use the counterpart). Install the required modules, specified in requirements.txt, typing:

  ```bash
  pip3 install -r requirements.txt
  ```

### 3. Set up MySQL database

  In the project folder run MySQL (more about [MySQL](https://www.a2hosting.com/kb/developer-corner/mysql/managing-mysql-databases-and-users-from-the-command-line)):

  ```bash
  mysql -uusername -ppass
  ```

  where 'username' is your mysql username and 'pass' is your mysql password.

  While MySQL is running, create a new database 'datarepresentation' and switch to this database

  ```SQL
  CREATE DATABASE datarepresentation;
  USE datarepresentation;
  ```

  Create a new schema for the table 'equipment':

  ```SQL
  CREATE TABLE equipment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    category ENUM('Tier 1', 'Tier 2', 'Auxiliary', 'Spare') DEFAULT 'Tier 1',
    name VARCHAR(50),
    supplier VARCHAR(50),
    price_eur FLOAT(10, 2)
    );
  ```
  
### 4. Set up MySQL configuration file

  Create a new file called 'config.py'. Paste in the following:

  ```python
  mysql = {
    'host': 'localhost',
    'user': 'username',
    'password': 'pass',
    'database': 'datarepresentation'
    }
  ```

  where 'username' should be replaced with your username, and 'pass' - with your password.

### 4. Run the server

  On Linux systems, type:

  ```bash
  export FLASK_APP=app.py
  python3 -m flask run
  ```
  
  On Windows systems, type:

  ```bash
  set FLASK_APP=app.py
  python -m flask run
  ```

Keep the virtual environment running. Press ctrl+c to terminate the server.

### 5. Testing the connection

On a new terminal (separate to the one keeping the server running) test the connection by checking the http responses with the Curl, for example:

```bash
curl -i http://localhost:5000/
```

### 6. Run the web app

In your Internet browser, access the following address: <http://localhost:5000/>.

___

## References

General, high-level, reference sources are listed below. References to specific problems are included in the Notebook.

### Regarding the project

- Project details [project brief](https://github.com/andkoc001/Data_Rep_Project.git/blob/main/Project%20Description.pdf).

### Regarding Python

- Python 3 Documentation. [online] Available at: <https://docs.python.org/3/> [Accessed November 2020].
- Python Virtual Environment. [online] Available at: <https://docs.python-guide.org/dev/virtualenvs/> [Accessed November 2020].

### Regarding web server, API and related

- Flask User Guide - [online] Available at: <https://flask.palletsprojects.com/en/1.1.x/#user-s-guide> [Accessed December 2020].
- Julian Nash - Learning Flask - [online] Available at: <https://pythonise.com/series/learning-flask> [Accessed December 2020].
- A beginner's guide to building a simple database-backed Flask website on PythonAnywhere - [online] Available at: <https://blog.pythonanywhere.com/121/> [Accessed December 2020].
- Caleb Curry - REST API Crash Course.[online] Available at: <https://docs.google.com/document/d/1v0l4TC2ZyFYyk6Y0ggFw86li2F6cwr5GLuTUyrzSpT4/edit#> [Accessed December 2020].
- REST API Crash Course [online] Available at: <https://youtu.be/qbLc5a9jdXo> and <https://docs.google.com/document/d/1v0l4TC2ZyFYyk6Y0ggFw86li2F6cwr5GLuTUyrzSpT4/edit> [Accessed December 2020].

### Regarding other tools and technologies

- MySQL documenation. [online] Available at: [<https://docs.python.org/3/](https://dev.mysql.com/doc/)> [Accessed December 2020].
- How to manage MySQL databases, users, and tables from the command line [online] Available at: <https://www.a2hosting.com/kb/developer-corner/mysql/managing-mysql-databases-and-users-from-the-command-line> [Accessed December 2020]

___

Andrzej Kocielski, 2020