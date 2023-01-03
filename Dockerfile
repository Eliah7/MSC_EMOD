FROM docker-production.packages.idmod.org/idm/centos:dtk-build
RUN id -u $USER`:`id -g $USER
WORKDIR /EMOD
RUN scons --Disease=Generic
RUN /EMOD/build/x64/Release/Eradication/Eradication --version
ENTRYPOINT [ "bash" ]