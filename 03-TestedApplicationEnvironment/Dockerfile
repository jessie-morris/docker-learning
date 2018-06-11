FROM ubuntu:16.04
RUN apt-get update && apt-get install -y go git
RUN git clone https://github.com/TheAnig/quoteget-golang
WORKDIR /quoteget-golang
CMD ["go", "test"]
CMD ["go", "run", "quoteget.go"]