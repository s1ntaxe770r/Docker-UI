import docker

client = docker.from_env()


class ContainerMan:
    @staticmethod
    def GetRunning(self):
        running = client.containers.list()
        return running

    @staticmethod
    def DockerInfo():
        """
        Generic Docker Info. Retrun Type: Dict
        """
        parsed_info = {}
        information = client.info()
        running_containers = information["ContainersRunning"]
        stopped_containers = information["ContainersStopped"]
        total_images = information["Images"]
        parsed_info["running_containers"] = running_containers
        parsed_info["stopped_containers"] = stopped_containers
        parsed_info["total_images"] = total_images

        return parsed_info
