import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class StartDeviceLoggingCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.StartDeviceLogging")

    def execute(self, filename, username, password):
        requestObj = [filename, username, password]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "StartDeviceLogging was successful", "StartDeviceLogging failed")
