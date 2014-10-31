import sys
import os

from docker import Client

from time import time


_BASE_URL = 'tcp://192.168.59.103:2375'


def get_test_files(tests_dir):
    test_files = []
    for _file in os.listdir(tests_dir):
        if _file.startswith("test_") and _file.endswith(".py"):
            test_files.append(_file)
    return test_files


def create_containers_for_files(docker_client, files):
    container_ids = []
    for _file in files:
        command = 'bash -c "nosetests /twarm/tests/{} &> ' \
                  '/twarm/output/{}.txt"'.format(_file, _file)
        container = docker_client.create_container('twarm:latest',
                                                   command=command,
                                                   volumes=['/twarm'])
        container_ids.append(container['Id'])
    return container_ids


def start_containers(docker_client, container_ids, volume_bind):
    for container_id in container_ids:
        docker_client.start(container_id, binds=volume_bind)

    # Wait on all containers
    for container_id in container_ids:
        docker_client.wait(container_id)


def main(main_dir, tests_dir):
    test_files = get_test_files(tests_dir)

    docker_client = Client(base_url=_BASE_URL,
                           version='1.3.0')

    volume_binds = {
        main_dir: {
            'bind': '/twarm',
            'ro': False
        }
    }

    container_ids = create_containers_for_files(docker_client, test_files)
    start_containers(docker_client, container_ids, volume_binds)


if __name__ == '__main__':
    directory = sys.argv[1]
    tests_directory = '{}/tests'.format(directory)

    start = time()
    main(directory, tests_directory)
    end = time()
    print 'Tests ran in {}ms'.format((end - start) * 1000.0)
