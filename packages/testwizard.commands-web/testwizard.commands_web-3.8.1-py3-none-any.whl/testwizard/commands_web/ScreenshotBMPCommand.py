import sys
import json

from testwizard.commands_core import CommandBase
from .ScreenshotResult import ScreenshotResult


class ScreenshotBMP(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.ScreenShotBMP")

    def execute(self, filename):
        requestObj = [filename]

        result = self.executeCommand(requestObj)

        return ScreenshotResult(result, "ScreenshotBMP was successful", "ScreenshotBMP failed")
