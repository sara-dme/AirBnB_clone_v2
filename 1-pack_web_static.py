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
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    path = "versions/web_static_{}.tgz".format(dt)
    try:
        print("Packing web_static to {}".format(path))
        local("tar -cvzf {} web_static".format(path))
        sz = os.stat(path).st_size
        print("web_static packed: {} -> Bytes".format(path, sz))
        return path
    except Exception:
        return None
