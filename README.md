# Data_Rep_Project

Data Representation Project, GMIT 2020-2021

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

___

## Introduction

This is my assignment project to Data Representation module, Galway-Mayo Institute of Technology, 2020.

This GitHub repository documents my research, project progress (git version control) and findings of the assignment project - a Web Application deployment.

### Assignment delivery

This project avail of several tools commonly used in the industry, such as Python programing language, Flask, Git, etc.

The project is delivered via this GitHub [repository](https://github.com/andkoc001/Data_Rep_Project.git).

In this README.md file I have incorporated the research and described the project progress. It is illustrated with the applied concepts and methods together with relevant code snippets. Finally, inside the README.md I have included also references to sources being consulted for this assignment.

The project is based predominantly and heavily on the lecture materials. The reference to the lecture materials is not specifically provided. Other generic resources are listed at the bottom of this README.md file. More specific references are provided when applicable.

### Project objectives

The objective of the is to develop a web service to access, display, modify etc. data from an API using Flask.

The goal of the project is to produce a web app that will do the following:

- Consuming a RESTful API, either in Python (your server) or  javascript (web page)
- Running a Server
- Web frontend to display data and interact with server (If the project requires it).

The detailed project instruction can be found in the [file]<https://github.com/andkoc001/Data_Rep_Project.git/blob/main/Project%20Description.pdf>  

___

## The Project

### Setting the environment

The project requires external Python libraries. In order to preserve the same condition _virtual environment_ is created, that manages additional libraries.

The following script (from [REST API Crash Course](https://docs.google.com/document/d/1v0l4TC2ZyFYyk6Y0ggFw86li2F6cwr5GLuTUyrzSpT4/edit#)) should be run in your terminal to create the virtual environment and activate it. It will also install the required libraries and list them in the requirements.txt file.

```
python3 -m venv .venv  
source .venv/bin/activate  
pip3 install flask  
pip3 freeze > requirements.txt
```

The virtual environment should be kept running.

___

## References

General, high-level, reference sources are listed below. References to specific problems are included in the Notebook.

### Regarding the project

- Project details [project brief](https://github.com/andkoc001/Data_Rep_Project.git/blob/main/Project%20Description.pdf).

### Regarding Python environment

- Python 3 Documentation. [online] Available at: <https://docs.python.org/3/> [Accessed November 2020].
- Flask User Guide - [online] Available at: <https://flask.palletsprojects.com/en/1.1.x/#user-s-guide> [Accessed November 2020].
- A beginner's guide to building a simple database-backed Flask website on PythonAnywhere - [online] Available at: <https://blog.pythonanywhere.com/121/> [Accessed November 2020].
- Caleb Curry - REST API Crash Course.[online] Available at: <https://docs.google.com/document/d/1v0l4TC2ZyFYyk6Y0ggFw86li2F6cwr5GLuTUyrzSpT4/edit#> [Accessed November 2020].

### Regarding the accessed API

- REST API Crash Course - https://youtu.be/qbLc5a9jdXo and https://docs.google.com/document/d/1v0l4TC2ZyFYyk6Y0ggFw86li2F6cwr5GLuTUyrzSpT4/edit#

___

Andrzej Kocielski, October 2020 - January 2021