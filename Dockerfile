FROM python:3
WORKDIR /lpapp
COPY . /lpapp
RUN pip install -r requirements.txt
CMD [ "python3", "latestpastes.py" ]
