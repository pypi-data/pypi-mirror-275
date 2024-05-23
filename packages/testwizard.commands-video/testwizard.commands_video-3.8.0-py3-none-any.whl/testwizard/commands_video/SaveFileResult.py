import json
import sys

from testwizard.commands_core.ResultBase import ResultBase


class SaveFileResult(ResultBase):
    def __init__(self, result, successMessage, failMessage):
        if "saved" in result:
            result["ok"] = result["saved"] is True

        ResultBase.__init__(self, result["ok"] is True, successMessage, failMessage)

        self.filePath = result["filePath"]

        if self.success is True:
            return

        self.errorCode = result["errorCode"]
        if "errorCode" in result:
            self.message = self.getMessageForErrorCode(self.message, result["errorCode"])
        elif result["errorMessage"]:
            self.message = self.message + ": " + result["errorMessage"]
