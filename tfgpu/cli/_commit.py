import sys

from absl import app, flags, logging

FLAGS = flags.FLAGS

flags.DEFINE_string("tag", "ss", "default tag tag")


def main(argv):
    FLAGS(argv)
