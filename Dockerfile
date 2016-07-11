FROM python:2.7.12

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -v -r requirements.txt

COPY fetch_url /usr/src/app/fetch_url
WORKDIR fetch_url
CMD ["nameko","run","fetch_url"]
