FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip wget git

RUN git clone https://github.com/freeman91/kata.git && cd kata/fizzbuzz
WORKDIR /kata/fizzbuzz/

CMD ["python", "-m", "unittest", "discover", "test_fizzbuzz"]