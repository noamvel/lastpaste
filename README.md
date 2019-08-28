# Latests Pastes

Latests Pastes is simple python3 web crawler that crawls the [pastebin.com](https://pastebin.com/) site and stores the most recent "pastes" into storage. 

## Installation

* Make sure you have python3 installed. (python3 --version) otherwise  -> [python.org/downloads](https://www.python.org/downloads/)
* Clone this project to your desired directory.

## As Docker python image

* Make sure you have docker installed. (docker --version) otherwise  -> [docker](https://docs.docker.com/install/)
```
pip docker yoyo
```

## As python project

* It is best to have an isolated python environment [python-virtual-environments](https://realpython.com/python-virtual-environments-a-primer/). From project directory (latestpastes) run:

```
python3 -m venv env
source env/bin/activate
```
* Install project required modules:

```
pip install -r requirements.txt
```

# Usage

* execute
```
python3 latestpastes.py
```
* view log
```
latestpastes/latestpastes.log
```
* view storage
```
File Storage - latestpastes/jobs/
TinyDB storage - latestpastes/db.json
```
* run project tests
```
python3 -m unittest
```





