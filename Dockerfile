FROM python:3
ADD latestpastes.py /
RUN pip install arrow
RUN pip install lxml
RUN pip install requests
RUN pip install schedule
RUN pip install tinydb
CMD [ "python3", "latestpastes.py" ]
