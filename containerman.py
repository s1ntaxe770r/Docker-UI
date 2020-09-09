import docker

client = docker.from_env()


class ContainerMan:

	@classmethod
    def GetRunning():
        """retruns a list of all running containers. Return Type: list """
        running = client.containers.list()
        return running

    @classmethod
    def DockerInfo():
        """ Generic Docker Info. Retrun Type: Dict """
        parsed_info = {}
        information = client.info()
        running_containers = information["ContainersRunning"]
        stopped_containers = information["ContainersStopped"]
        total_images = information["Images"]
        parsed_info["running_containers"] = running_containers
        parsed_info["stopped_containers"] = stopped_containers
        parsed_info["total_images"] = total_images

        return parsed_info	



