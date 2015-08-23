from nose.plugins import Plugin

from docker import Client
from docker.utils import kwargs_from_env

__author__ = 'Liam Costello'
__doc__ = '''


'''


class Twarm(Plugin):
    def __init__(self):
        super(Twarm, self).__init__()

    def options(self, parser, env):
        super(Twarm, self).options(parser, env)
        parser.add_option(
            '--dockerfile',
            dest='docker_file',
            help="The path to the Dockerfile to create test containers from.",
            default=env.get('TWARM_DOCKER_FILE')
        )
        parser.add_option(
            '--num-containers',
            dest='num_containers',
            default=2,
            help="The number of Docker containers to run the tests against."
        )

    def configure(self, options, conf):
        super(Twarm, self).configure(options, conf)

        # This may throw an exception. It's best to throw the Docker exception
        # so the user can fix the error.
        docker_env_args = kwargs_from_env(assert_hostname=False)
        docker_client = Client(**docker_env_args)
        docker_client.info()

        # Dockerfile
        # Read in the Dockerfile provided by the user. Again, this may throw
        # an exception and we should let it float up.
        if not options.docker_file:
            raise ValueError(
                'Must provide a path to a Dockerfile or set '
                'the TWARM_DOCKER_FILE environment variable.'
            )

        with open(options.docker_file, mode='r') as _file:
            self.docker_file = _file.read()

        # Docker containers
        self.num_containers = options.num_containers
