FROM docker-production.packages.idmod.org/idm/centos:dtk-build
WORKDIR /EMOD
COPY ./model /
# RUN bash /PrepareLinuxEnvironment.sh
# RUN git clone https://github.com/InstituteforDiseaseModeling/EMOD

# RUN scons --Release --Disease=Malaria
# RUN /EMOD/build/x64/Release/Eradication/Eradication --version
ENTRYPOINT [ "bash" ]