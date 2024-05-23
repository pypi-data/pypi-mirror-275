import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class TouchAction_MoveToCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.TouchAction_MoveTo")

    def execute(self, x, y):
        requestObj = [x, y]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "TouchAction_MoveTo was successful", "TouchAction_MoveTo failed")
