import json
import sys

from testwizard.commands_core.ResultBase import ResultBase


class InitDriverResult(ResultBase):
    def __init__(self, result, successMessage, failMessage):
        ResultBase.__init__(self, result["ok"] is True, successMessage, failMessage)

        self.executorUrl = result["executorUrl"]
        self.sessionId = result["sessionId"]

        if self.success is True:
            return

        self.errorCode = result["errorCode"]
        self.message = self.getMessageForErrorCode(self.message, result["errorCode"])
