import sys
import json

from testwizard.commands_core import CommandBase
from .GetElementAttributeResult import GetElementAttributeResult


class GetElementAttributeCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Mobile.GetElementAttribute")

    def execute(self, selector, attribute):
        requestObj = [selector, attribute]

        result = self.executeCommand(requestObj)

        return GetElementAttributeResult(result, "GetElementAttribute was successful", "GetElementAttribute failed")
