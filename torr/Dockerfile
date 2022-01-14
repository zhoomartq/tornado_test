FROM python:3.8.10
ENV PYTHONUNBUFFERED 1

EXPOSE 8000


WORKDIR /torr
RUN pip install --upgrade pip

COPY requirements.txt /torr
RUN pip install -r /torr/requirements.txt

ADD . /torr/