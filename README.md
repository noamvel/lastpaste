# Latests Pastes

Latests Pastes is simple python3 web crawler that crawls the site: https://pastebin.com/ and stores the most recent "pastes" into storage. 

## Installation

* Make sure you have python3 installed. [python.org/downloads](https://www.python.org/downloads/)
* Clone this project to your desired directory.

### As python project
* It is best to have an isolated python environments [python-virtual-environments](https://realpython.com/python-virtual-environments-a-primer/). From project directory (latestpastes) run:

```bash
python3 -m venv env
source env/bin/activate
```
* Install project required modules:

```bash
pip install -r requirements.txt
```
* Now your environment is set. you can:

* * execute

```bash
python3 latestpastes.py
```
* * view log

```bash
tail -f latestpastes.log
```
* * view storage

 * * *   File Storage - latestpastes/jobs/

 * * *   TinyDB storage - latestpastes/db.json

* * run project tests

```bash
python3 -m unittest
```

### As Docker image




