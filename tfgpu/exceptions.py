import logging
# Todo: Make sure writing the logs using logging package


class CommandNotSpecified(Exception):
    """docstring for CommandNotSpecified"""
    def __init__(self):
        logging.error("Command name should be specified.")
        pass


class CommandTargetNotSpecified(Exception):
    """docstring for CommandTargetNotSpecified"""
    def __init__(self):
        logging.error("Command target should be specified.")
        pass


class NoSuchCommand(Exception):
    """docstring for CommandNotSpecified"""
    def __init__(self, command_name):
        pass
