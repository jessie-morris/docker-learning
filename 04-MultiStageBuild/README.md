# MultiStage Builds 

For this activity we want to improve our tested application environment container by ensuring any images which are created are thin and with minimal dependencies. 

## Dockerfile Requirements

* Dockerfile has 2 stages.  The first stage should be responsible for building and testing your application, if either of these is not successful, Docker build should fail.
* The output of the docker build command should be an image which does not contain the dependencies to retrieve, build, and test your application.  In the case of a statically compiled binary for instance, you should not need to install the language in this image.  For a web project, a FROM such as nginx or node-alpine are reasonable examples.
* The build product created in the first container should be copied into the final container, ensuring the build is not performed twice.
* This page should provide you with a pattern for completing this exercise: https://docs.docker.com/develop/develop-images/multistage-build/
