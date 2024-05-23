import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkResult import OkResult


class SetTextOnScreenDisplayCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "SetTextOnScreenDisplay")

    def execute(self, osdText, osdArea,  textColor, backgroundColor, duration):
        requestObj = [osdText]
        if osdArea is not None:
            requestObj = [osdText, osdArea]
            if textColor is not None:
                requestObj = [osdText, osdArea, textColor]
                if backgroundColor is not None:
                    requestObj = [osdText, osdArea, textColor, backgroundColor]
                    if duration is not None:
                        requestObj = [osdText, osdArea, textColor, backgroundColor, duration]

        result = self.executeCommand(requestObj)

        return OkResult(result, "SetTextOnScreenDisplay was successful", "SetTextOnScreenDisplay failed")
