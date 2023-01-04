#! bin/bash
docker run -it  -v ${PWD}/data:/EMOD idm:v3 -c "/Eradication  --help"
docker run -it  -v ${PWD}/data:/EMOD idm:v3 -c "/Eradication -C config.json"

# run no 11 from a python script and get the output into this program.
# convert the results to a reward 
# 

# what is the state of this openMalaria environment
# what is the reward
# what are the actions that the agent can perform
# How do we simulate this run for single region
# We need to run this for multiple cities