FROM python:3.6

ADD . /var/lib/trollblock

RUN pip install -r /var/lib/trollblock/requirements.txt

RUN cd /var/lib/trollblock && nosetests .

WORKDIR /var/lib/trollblock

CMD ["gunicorn", "server:app"]