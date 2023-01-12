# MSC_EMOD

The purpose of this project is to create a simulation based on EMOD(Epidemiological Modelling Software) 
for modeling the disease dynamics and transmission mechanics for the malaria disease. The purpose of such a simulation is to create an 
environment in which reinforcement learning algorithms can be run.

## How to use the simulation tool

### Build the docker image

To use the project a docker image that contains the EMOD simulation executable is to be built. To do this clone this repository and run the command below at 
the root of this project

> docker build . -t <name of image>:<version>

Eg. 
> docker build . -t idm:v3

### Run the main.py python file

> python main.py
