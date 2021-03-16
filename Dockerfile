# pull official base image
FROM python:3.8.3-alpine

ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/ngo-donations

# install dependencies
RUN apk update

RUN pip install --upgrade pip

COPY ./requirements/development.txt ./requirements.txt
COPY ./.envs/.production ./.env
RUN pip install -r requirements.txt


WORKDIR /usr/src/ngo-donations/ngo
COPY ./ngo/start .
RUN chmod +x ./start

COPY ngo/ .

EXPOSE 8000

# RUN ./start
CMD ["./start"]
