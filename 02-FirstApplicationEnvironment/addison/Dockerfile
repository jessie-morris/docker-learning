FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python3-pip git
RUN apt-get install -y python-setuptools && easy_install pip
RUN pip install -U pytest

RUN git clone https://github.com/freeman91/kata.git

WORKDIR /kata/babysitter

CMD ["pytest", "test_babysitter.py"]