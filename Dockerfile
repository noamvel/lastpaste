FROM python:3
COPY . /tmp/docker
WORKDIR /tmp/docker
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python3", "latestpastes.py" ]
