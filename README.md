# Latests Pastes

Latests Pastes is simple python3 web crawler that crawls the [pastebin.com](https://pastebin.com/) site and stores the most recent "pastes" into storage. 

## Installation

* Make sure you have python3 installed. (python3 --version) otherwise  -> [python.org/downloads](https://www.python.org/downloads/)
* Clone this project to your desired directory.

## As python environment

* It is best to have an isolated python environment  [venv](https://realpython.com/python-virtual-environments-a-primer/). 
From project directory (latestpastes) run:
```
python3 -m venv env
source env/bin/activate
```

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
latestpastes/latestpastes.log
```
* storage
```
File Storage - latestpastes/jobs/
TinyDB storage - latestpastes/db.json
```
* run unit tests
```
python3 -m unittest
```

## As python docker image

* Make sure you have docker installed and running. (docker --version) otherwise  -> [docker](https://docs.docker.com/install/)

* build docker image:
```
docker build -t latestpastes .
```
## Usage

* execute
```
docker run latestpastes
```





