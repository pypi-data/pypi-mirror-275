import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class AddCapabilityCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.AddCapability")

    def execute(self, name, value):
        requestObj = [name, value]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "AddCapability was successful", "AddCapability failed")
