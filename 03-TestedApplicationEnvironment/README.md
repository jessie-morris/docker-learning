# Tested Application Environment

For this activity we want to improve our application environment container by ensuring any images which are created are production quality. 

## Dockerfile Requirements

* Runs a given cannonical base image like Ubuntu 16.04
* Installs some set of dependencies on top of the base image for the language of your choice
* Copys in an outside application which has unit tests into the image, and runs the tests, failing the docker build if these tests fail
* Executes the application as the entrypoint of the docker container it will produce  
