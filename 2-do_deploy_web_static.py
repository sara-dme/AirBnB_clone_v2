#!/usr/bin/python3
""" module doc (Fabric script)
"""
import os
from fabric.api import env, local, put, run
from datetime import datetime

# the ramote hosts
env.hosts = ['52.86.86.244' , '54.160.125.195']


def do_deploy(archive_path):
    """
    deploys an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False
    
    # file name
    fl_name = os.path.basename(archive_path)
    fl_no_ext = os.path.splitext(fl_name)[0]
    dpath = "/data/web_static/releases/"
    try:
        # upload archive to the temporary folder on the web server
        put(archive_path, "/tmp/")

        #create the directory where the code will be depload
        run("mkdir -p /data/web_static/releases/{}/"
            .format(fl_no_ext))

        # uncompress the archive into the deployment folder
        run("tar -xzf /tmp/{} -C {}{}/".format(fl_name, dpath, fl_no_ext))

        # remove the archive from the server
        run("rm /tmp/{}".format(fl_name))

        # move the files to a new folder
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fl_no_ext))

        # delete the old symbolic link
        run("rm -rf {}{}/web_static".format(dpath, fl_no_ext))

        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fl_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
