# Latests Pastes
Latests Pastes is a simple python3 web crawler that crawls the [pastebin.com](https://pastebin.com/) site and stores the most recent "pastes" into storage. 

## Installation 
* Make sure you have python3 installed with latest version 3.7.4 and pointed by 'python' command:
```
python --version
```
python3 is not installed -> [install python](https://www.python.org/downloads/)

* Clone this project to your desired directory.
git is not installed -> [install git](https://git-scm.com/download)

### As python environment

* It is best to have an isolated python virtual environment. from project home directory 'latestpastes' run:
```
python -m venv env
source env/bin/activate
```
you can refer -> [venv](https://realpython.com/python-virtual-environments-a-primer/)
* Install project required modules:
```
pip install -r requirements.txt
```
* execute
```
python latestpastes.py
```

### As python docker image

* Make sure you have docker installed and running:
```
docker --version
docker ps
```
otherwise  -> [docker](https://docs.docker.com/install/)

* build docker image, from project home directory run:
```
docker build -t latestpastes .
```
* execute
```
docker run --name you_decide -v $(pwd):/lpapp latestpastes
```

## Usage

* log
```
latestpastes.log
```
* storage
```
Files - jobs/
TinyDB - db.json
```




