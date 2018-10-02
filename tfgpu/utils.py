import os
import subprocess


# From https://stackoverflow.com/questions/7040592/calling-the-source-
# command-from-subprocess-popen/12708396
def shell_source(script_path):
    """Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it."""
    pipe = subprocess.Popen(". %s; env" % script_path,
                            stdout=subprocess.PIPE, shell=True)
    output = pipe.communicate()[0]
    env = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(env)
