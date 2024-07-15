# Backend Flask Task app (react)

## Create an environment
create project folder and a `.venv` folder within:
```bash
mkdir myproject
cd myproject
python3 -m venv .venv
```
clone repository `git clone`

## Install Application
activate environment and install dependencies:
```bash
. .venv/bin/active
pip install -r requirements.txt
```
and run application with `flask run`

## Running Test
for run test:
```bash
python -m pytest /tasks/*
```