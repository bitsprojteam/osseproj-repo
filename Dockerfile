FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

ENV IS_DOCKER=true

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip \
    pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8030

CMD ./app.sh