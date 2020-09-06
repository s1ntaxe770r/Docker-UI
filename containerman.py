import docker

client =  docker.from_env()

class ContainerMan(object):
    def GetRunning():
        """retruns a list of all running containers. Return Type: list """
        running = client.containers.list()
        return running
    def DockerInfo():
        """ Generic Docker Info. Retrun Type: Dict
        pass

x = ContainerMan.DockerInfo()

print(x)