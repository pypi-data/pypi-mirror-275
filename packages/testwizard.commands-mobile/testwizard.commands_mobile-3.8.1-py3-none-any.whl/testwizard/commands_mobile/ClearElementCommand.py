import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class ClearElementCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.ClearElement")

    def execute(self, selector):
        requestObj = [selector]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "ClearElement was successful", "ClearElement failed")
