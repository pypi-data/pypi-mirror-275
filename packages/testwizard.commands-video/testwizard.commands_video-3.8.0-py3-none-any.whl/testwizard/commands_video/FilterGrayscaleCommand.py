import sys
import json

from testwizard.commands_core import CommandBase
from .FilterResult import FilterResult


class FilterGrayscaleCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "FilterGrayscale")

    def execute(self, levels):
        requestObj = [levels]

        result = self.executeCommand(requestObj)

        return FilterResult(result, "FilterGrayscale was successful", "FilterGrayscale failed")
