FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

RUN mkdir /doc_dir
WORKDIR /doc_dir

RUN pip install --upgrade pip
ADD requirements.txt /doc_dir/
RUN pip install -r requirements.txt
ADD . /doc_dir/