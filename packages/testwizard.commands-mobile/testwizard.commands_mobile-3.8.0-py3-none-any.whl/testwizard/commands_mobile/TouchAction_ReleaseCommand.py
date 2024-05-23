import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult


class TouchAction_ReleaseCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.TouchAction_Release")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "TouchAction_Release was successful", "TouchAction_Release failed")
