FROM python:3.8.3-alpine
WORKDIR /usr/src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update
RUN pip install --upgrade pip
RUN apk add python3-dev
RUN apk add gpgme-dev
RUN apk add libc-dev
RUN apk add gcc jpeg-dev zlib-dev libffi-dev freetype-dev musl-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev cairo-dev pango-dev gdk-pixbuf-dev git
RUN apk add mariadb-dev
RUN git clone -b main https://github.com/jpleyvat/ngo-donation.git
WORKDIR /usr/src/ngo-donation
RUN pip install -r requirements.txt
WORKDIR /usr/src/ngo-donation/ngo
COPY ./ngo/ngo/.env ./ngo/
RUN chmod +x start
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
