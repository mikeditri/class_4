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

Continuous Intengration:

This is more than just a tool, but a best practice methodology often used in DevOps models. 
Continuous integrations means frequent (mulitple times per day) integration of code from multiple developers
followed by a series of tests and code checks to ensure problems in the code are caught early on.
A much better approach than the traditional manual integration in which developers would write their code, then
at one point integrate and spend a ton of time solving the bugs due to the fact that they were not coding on
the latest versions.

CI is a much more agile process and allows teams to focus more on developing features rather than fixing integration bugs.

 One tool that I found online is Travis CI when i searched for best CI for github. 


"Travis CI because:

Automatically builds and tests incremental code changes
Manages deployments and notifications
Free for open source projects
Supports a wide variety of programming languages
Customizable software support
Enterprise plans available" (citation: https://www.quora.com/Whats-the-best-Continuous-Integration-tool-for-GitHub)