FROM python:3
ADD latestpastes.py /
RUN pip install arrow
RUN pip install lxml
RUN pip install requests
RUN pip install schedule
RUN pip install tinydb
RUN pip install certifi
RUN pip install chardet
RUN pip install idna
RUN pip install python-dateutil
RUN pip install six
RUN pip install urllib3
CMD [ "python3", "latestpastes.py" ]
