import sys
import json

from testwizard.commands_core import CommandBase
from .FilterResult import FilterResult


class FilterCBICommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "FilterCBI")

    def execute(self, contrast, brightness, intensity):
        requestObj = [contrast, brightness, intensity]

        result = self.executeCommand(requestObj)

        return FilterResult(result, "FilterCBI was successful", "FilterCBI failed")
