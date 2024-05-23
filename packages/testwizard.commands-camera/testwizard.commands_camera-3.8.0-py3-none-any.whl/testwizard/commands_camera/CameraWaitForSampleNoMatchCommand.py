import sys
import json

from testwizard.commands_core import CommandBase
from .CameraWaitForSampleResult import CameraWaitForSampleResult


class CameraWaitForSampleNoMatchCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Camera.WaitForSampleNoMatch")

    def execute(self, x, y, width, height, timeout, distanceThreshold):
        if distanceThreshold is None:
            requestObj = [x, y, width, height, timeout]
        else:
            requestObj = [x, y, width, height, timeout, distanceThreshold]

        result = self.executeCommand(requestObj)

        return CameraWaitForSampleResult(result, "WaitForSampleNoMatch was successful", "WaitForSampleNoMatch failed")
