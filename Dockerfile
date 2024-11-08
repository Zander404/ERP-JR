FROM python:3.12.2-slim-bullseye

WORKDIR /app/

ENV PYTHONDONTWRITECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod 777 /app/entrypoint.sh

COPY . .

ENTRYPOINT [ "/app/entrypoint.sh" ]