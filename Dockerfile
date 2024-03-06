# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask==2.1.* Werkzeug==2.2.2

# install app
COPY main.py /

# final configuration
ENV FLASK_APP=main
EXPOSE 8000
CMD flask run --host 0.0.0.0 --port 8000
