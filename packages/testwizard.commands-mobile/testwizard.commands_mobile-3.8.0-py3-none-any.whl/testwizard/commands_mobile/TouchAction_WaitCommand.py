import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class TouchAction_WaitCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.TouchAction_Wait")

    def execute(self, duration):
        requestObj = [duration]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "TouchAction_Wait was successful", "TouchAction_Wait failed")
