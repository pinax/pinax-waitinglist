import pkg_resources

__version__ = pkg_resources.get_distribution("pinax-waitinglist").version
default_app_config = "pinax.waitinglist.apps.AppConfig"
