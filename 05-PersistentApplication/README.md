# Persistent Application

For this activity we will change our context to building a docker container to deploy an existing off the shelf piece of software in a persistent and accessible way.

## Dockerfile Requirements

* The Dockerfile begins with FROM the jenkins:lts image
* The Dockerfile installs some dependencies into the Jenkins image. e.g. kubectl

## Deployment Requirements
* The docker has a deployment mechanism using a docker-compose file.
* The docker compose file volumes out all of the essential files from the docker container to the host disk
* The docker compose file maps the appropriate ports from the container to the host

Following these requirements we should have a docker image which is a user-modified Jenkins instance, which can be launched and destroyed via docker-compose while persisting all application data
