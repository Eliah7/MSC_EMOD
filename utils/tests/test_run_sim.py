import subprocess

# # specify paths
# binary_path = "binDirectory\Eradication.exe"
# input_path = "inputDirectory\Namawala\

# commission job
subprocess.call( ["docker run -it  -v ${PWD}:/om/work openmalaria:v2 -c \"./openMalaria  -s ./work/scenario.xml -o ./work/output2.txt\""] ) 
# run simulation
# gather results and get the reward
# give new state and reward back to the agent
