import os
import subprocess


# From https://stackoverflow.com/questions/7040592/calling-the-source-
# command-from-subprocess-popen/12708396
def shell_source(script_path):
    """Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it."""
    pipe = subprocess.Popen(". %s; env" % script_path,
                            stdout=subprocess.PIPE, shell=True)
    output = pipe.communicate()[0].decode('utf-8')
    env = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(env)


def line_exists_in_file(filepath, line):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return line in lines


def remove_line_from_file(filepath, line):
    if not os.exists(filepath):
        print("No such file: {}".format(filepath))
        return False

    # Read lines, remove target string from file
    with open(filepath, 'r') as f:
        lines = f.readlines()
        if line in lines:
            lines.remove(line)
        else:
            return False

    # Rewrite file
    with open(filepath, 'w') as f:
        for line in lines:
            f.write(line)
    return True
