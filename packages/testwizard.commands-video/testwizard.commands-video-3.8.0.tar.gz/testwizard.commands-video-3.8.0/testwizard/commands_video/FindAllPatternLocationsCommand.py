import sys
import json

from testwizard.commands_core import CommandBase
from .FindAllPatternLocationsResult import FindAllPatternLocationsResult


class FindAllPatternLocationsCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "FindAllPatternLocations")

    def execute(self, filename, mode, similarity):
        requestObj = [filename, mode, similarity]

        result = self.executeCommand(requestObj)

        return FindAllPatternLocationsResult(result, "FindAllPatternLocations was successful", "FindAllPatternLocations failed")
