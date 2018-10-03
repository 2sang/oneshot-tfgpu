import sys

from absl import app, flags, logging

FLAGS = flags.FLAGS

flags.DEFINE_string("tag", "ss", "default tag tag")

def main(argv):
    print("argv: {}".format(argv))
    FLAGS(argv)
    print("this is it, ")
    print("FLAGS.tag: {}".format(FLAGS.tag))

# flags.DEFINE_string('tag', defaults['tag'],
#                     'image tag name(ex. latest-gpu-py3)')
# flags.DEFINE_string('vname', defaults['volume_name'],
#                     'specify the volume name to mount')
