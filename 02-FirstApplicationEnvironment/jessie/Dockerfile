FROM ubuntu:16.04

RUN apt-get update && apt-get install -y ruby-full git

RUN git clone https://github.com/jessiemorris/ruby_fizzbuzz 
RUN gem install rspec
WORKDIR /ruby_fizzbuzz
CMD ["rspec"]
