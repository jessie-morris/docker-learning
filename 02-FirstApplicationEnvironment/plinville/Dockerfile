FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
    python

ADD ./example_test.py /
CMD ["python", "example_test.py"]
