def run_simulation():
    """
    - execute docker command to run simulation for one year
    - get results from the output folder
    - compute the reward and return the reward
    """
    print("\nStarting Simulation...\n")
    execute_docker_commands()
    # compute reward
    # consider states as input to the simulation
    # find out how states will be represented
    


def execute_docker_commands(*commands):
    """
    - docker run -it  -v ${PWD}/data:/EMOD idm:v3 -c "/Eradication  --help
    - docker run -it  -v ${PWD}/data:/EMOD idm:v3 -c "/Eradication -C config.json
    """
    import docker
    import os

    # try:
    client = docker.from_env()

    # print(f"{os.getcwd()}")
    cont = client.containers.run(image="idm:v3", volumes=[f"{os.getcwd()}/data:/EMOD"], command=["-c", "/Eradication -C config.json"], detach=True)
    cont.wait()
    print(cont.logs().decode('UTF-8'))
    # print(client.containers.list())


if __name__ == '__main__':
    run_simulation()
