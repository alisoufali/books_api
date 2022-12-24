# BOOKS API

A simple book management system in REST-API made with python and fastapi.

## Description

I made this project to show my fluency in python and backend development using fastapi. It's just a simple book management system with multiple endpoints (CRUD operations).
To findout more information about how to run the code, the dependencies and etc. please refer to the sections below.

## Dependencies

This project is based on python v3.10 or more. I have testes this project with python v3.11 and v3.10.
It might not work with older versions.
Other dependencies are fastapi and uvicorn libraries which are provided in the requirements.txt file.
To learn how you can setup and run the project in your own environment, Please refer to the sections below.

## How to Setup?

After installing python make sure it is the default python interpreter in terminal(or powershell in windows).
Then in the project directory open a terminal and enter the following commands.

### Linux/Mac Users

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```

### Windows Users

For windows users all steps are the same except the second step (sourcing the activate script). Instead of `source .venv/bin/activate` you need to enter `.\.venv\Scripts\activate`.

## How to run?

All you need to do is to run main.py file (as the following command) and openup `0.0.0.0:8000` link in your browser.

```bash
python main.py
```

You may want to change the link and the port. To do so, please modify the main.py file and change `0.0.0.0` to the ip address of your choice and `8000` to the port of your choice.

## How to use?

This project has multiple endpoints. All documentation are provided in the openapi (swagger UI). Just run the project and head to the home directory (link `0.0.0.0:8000/`). You will find all documentations there.
