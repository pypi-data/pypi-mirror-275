import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.SimpleResult import SimpleResult

class StartBackgroundCaptureCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "StartBGCapture")
    
    def execute(self, stepSize, captures):
        requestObj = [stepSize, captures]

        result = self.executeCommand(requestObj)

        return SimpleResult(result, "StartBackgroundCapture was successful", "StartBackgroundCapture failed")