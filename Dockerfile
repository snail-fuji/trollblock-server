FROM python:3.6

ADD . /var/lib/trollblock

RUN pip install -r /var/lib/trollblock/requirements.txt

RUN cd /var/lib/trollblock/models/zoo/demo && pip3 install .
RUN cd /var/lib/trollblock/models/zoo/trollblock-ulmfit-bpe && pip3 install .

WORKDIR /var/lib/trollblock

CMD ["gunicorn", "server:app"]