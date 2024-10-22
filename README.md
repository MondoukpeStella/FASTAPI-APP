# API CRUD with FastAPI and SQLite3

<div align="center" >
    <img src="https://img.shields.io/badge/Create-white" height="30"/>
    <img src="https://img.shields.io/badge/Simple-blue" height="30"/>
    <img src="https://img.shields.io/badge/API-red" height="30"/>
    <img src="https://img.shields.io/badge/with-white" height="30"/>
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi"height="30"/>
    <img src="https://img.shields.io/badge/and-black" height="30"/>
    <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" height="30"/>
</div>

## Table of Contents
- [Overview](#Overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)

## Overview
This is a simple CRUD (Create, Read, Update, Delete) API built using FastAPI and SQLite3 for the database. FastAPI is a modern, high-performance web framework for building APIs with Python, and SQLite3 is a lightweight relational database.

## Features

- *FastAPI Framework*: High-performance, easy to use, and compatible with both Python 3.6+ and type hints.
- *CRUD Operations*: Allows you to perform Create, Read, Update, and Delete operations on the data stored in SQLite3.
- *SQLite3*: A simple, file-based database, no separate server required.

## Requirements

To run this project, you need the following tools installed on your machine:

- *Python 3.6+*
- *FastAPI*: Can be installed via pip
- *Uvicorn*: ASGI server to serve your FastAPI application

You can install the required packages by running:

```sh
pip install fastapi uvicorn sqlite3
```

1. Clone the repository to your local machine:
```sh
git clone git@github.com:MondoukpeStella/FASTAPI-APP.git
cd FASTAPI-APP
```

2. Create an virtual environment:

```sh
    python -m venv env_name
    source env_name/bin/activate #To activate virtual environment
```
3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

4. Running the Application

To run the FastAPI application, you need to use the Uvicorn server:

uvicorn app:app --reload

Once the server is running, you can access the API documentation via Swagger at:
http://127.0.0.1:8000/docs

You can also access the ReDoc documentation at:
http://127.0.0.1:8000/redoc
