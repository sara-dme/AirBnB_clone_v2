#!/usr/bin/python3
""" fabric script that generates a .tgz archive """
import os
from datetime import datetime
from fabric.api import local, task

@task
def do_pack():
    """ Archives the static files
    """
    dt = datetime.now().strftime('%Y%m%d%H%M%S')
    dr = "mkdir -p versions"
    path = "versions/web_static_{}".format(dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(dr, path)).succeeded:
        return path
    return None
