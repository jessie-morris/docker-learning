# Segregated Networks

For this activity we will want to create an application which does not expose the sensitive pieces of the infrastructure to the public.

## Dockerfile Requirements

* You can use your own custom dockerfiles here, but you can also use prebuilt images.  The most obvious example to do this exercise would be to use a wordpress + mysql set of docker images.

## Deployment Requirements
* The docker has a deployment mechanism using a docker-compose file.
* The docker compose file volumes out all of the essential files from the docker container to the host disk
* The docker compose file creates a network which allows the applications in this stack to communicate amongst each other but private infrastrture such as databases are network segregated.

