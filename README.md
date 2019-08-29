# Latests Pastes

Latests Pastes is a simple python3 web crawler that crawls the [pastebin.com](https://pastebin.com/) site and stores the most recent "pastes" into storage. 

## Installation

* Make sure you have python3 installed:
```
python3 --version
```
otherwise -> [python.org/downloads](https://www.python.org/downloads/)

* Clone this project to your desired directory.
## As python environment

* It is best to have an isolated python environment. from project home directory 'latestpastes' run:
```
python3 -m venv env
source env/bin/activate
```
you can refer -> [venv](https://realpython.com/python-virtual-environments-a-primer/)
* Install project required modules:
```
pip install -r requirements.txt
```
## Usage

* execute
```
python3 latestpastes.py
```
* log
```
latestpastes.log
```
* storage
```
Files - jobs/
TinyDB - db.json
```
* run unit tests
```
python3 -m unittest
```

## As python docker image

* Make sure you have docker installed and running:
```
docker --version
docker run hello-world
```
otherwise  -> [docker](https://docs.docker.com/install/)


* build docker image, from project home directory run:
```
docker build -t latestpastes .
```
## Usage

* execute
```
docker run --name you_decide -v $(pwd):/lpapp latestpastes
```
* log
```
latestpastes.log
```
* storage
```
Files - jobs/
TinyDB - db.json
```




