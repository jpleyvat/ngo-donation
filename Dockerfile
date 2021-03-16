##################################################
# NGO Donatios app Running in Docker
# Based on Alpine Linux
##################################################

# Pull official base image
FROM python:3.8.3-alpine

# Set environment
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/ngo-donations

# Install dependencies
RUN apk update

RUN pip install --upgrade pip

# Copy requirements and environment
COPY ./requirements/development.txt ./requirements.txt
COPY ./.envs/.production ./.env

# Install requirementes
RUN pip install -r requirements.txt

# Set work directory
WORKDIR /usr/src/ngo-donations/ngo

# Copy running script
COPY ./ngo/start .

# Make running script executable
RUN chmod +x ./start

# Copy app
COPY ngo/ .

# Expose port
EXPOSE 8000

# Migrate and start server
CMD ["./start"]
