import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class ClickPositionCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.ClickPosition")

    def execute(self, x, y):
        requestObj = [x, y]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "ClickPosition was successful", "ClickPosition failed")
