# class_4

To build Dockerfile from terminal:

1. Clone repo
2. navigate to directory and run:
docker build -t mikeditri/my-new-image:latest ./
(Where mikeditri/my-new-image:latest is the name of the build and the version after the : )

To check if build worked:
docker image ls
	verify if the image is listed and updated.

To run container:
docker run -ti mikeditri/my-new-image:latest

if using windows and gitbash to run add winpty before `docker run -ti ....`
