import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class TouchAction_TapCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.TouchAction_Tap")

    def execute(self, x, y):
        requestObj = [x, y]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "TouchAction_Tap was successful", "TouchAction_Tap failed")
