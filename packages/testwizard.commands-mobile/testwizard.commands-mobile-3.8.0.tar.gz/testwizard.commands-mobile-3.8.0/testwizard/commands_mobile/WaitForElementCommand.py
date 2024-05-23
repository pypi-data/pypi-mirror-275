import sys
import json

from testwizard.commands_core import CommandBase
from .WaitForElementResult import WaitForElementResult

class WaitForElementCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.WaitForElement")

    def execute(self, selector, maxSeconds):
        requestObj = [selector, maxSeconds]

        result = self.executeCommand(requestObj)

        return WaitForElementResult(result, "WaitForElement was successful", "WaitForElement failed")