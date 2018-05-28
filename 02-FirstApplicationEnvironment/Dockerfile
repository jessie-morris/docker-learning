FROM ubuntu:16.04
RUN apt-get update && apt-get install -y golang go git
RUN git clone https://github.com/TheAnig/golang_fizzbuzz
+WORKDIR /golang_fizzbuzz
+CMD ["go run fizzbuzz.go"]