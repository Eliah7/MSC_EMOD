def run_simulation():
    """
    - execute docker command to run simulation for one year
    - get results from the output folder
    - compute the reward and return the reward
    """
    print("\nStarting Simulation...\n")
    execute_docker_commands("idm:v3" ,"images")
    pass

def execute_commandline_command(command):
    """
    """
    print(command)

def execute_docker_commands(*commands):
    """
    - docker run -it  -v ${PWD}/data:/EMOD idm:v3 -c "/Eradication  --help"
    - docker run -it  -v ${PWD}/data:/EMOD idm:v3 -c "/Eradication -C config.json"
    """
    import docker
    import os

    # try:
    client = docker.from_env()

    print(f"{os.getcwd()}")
    container = client.containers.run(image="idm:v3", command='ls', volumes=[f"{os.getcwd()}/data:/EMOD"], detach=True, init=True, tty=True, privileged=True)
    # container = client.containers.run("alpine",["echo", "hello", "world"], detach=True)
    
    print(container.logs())
    # except Exception:
    #     print("\n *** Something Failed *** \n")
    

if __name__ == '__main__':
    run_simulation()
