FROM python:3.6

# Adding large dependencies
RUN pip install torch==1.1.0

RUN pip install scipy>=0.13.3

RUN pip install fastai==1.0.52

ADD . /var/lib/trollblock

RUN pip install -r /var/lib/trollblock/requirements.txt

RUN cd /var/lib/trollblock/models/zoo/demo && pip3 install .
# RUN cd /var/lib/trollblock/models/zoo/ulmfit_bpe && pip3 install .

WORKDIR /var/lib/trollblock

# CMD ["python", "./server.py"]

CMD ["gunicorn", "--timeout=100", "server:app"]
