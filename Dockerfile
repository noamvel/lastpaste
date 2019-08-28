FROM python:3
ADD latestpastes.py /
RUN pip install -r ../requirements.txt
CMD [ "python", "latestpastes.py" ]
