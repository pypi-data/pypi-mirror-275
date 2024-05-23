import sys
import json

from testwizard.commands_core import CommandBase
from .GetSizeResult import GetSizeResult


class GetElementSizeCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.GetElementSize")

    def execute(self, selector):
        requestObj = [selector]

        result = self.executeCommand(requestObj)

        return GetSizeResult(result, "GetElementSize was successful", "GetElementSize failed")
