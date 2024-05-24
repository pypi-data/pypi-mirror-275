import sys
import json

from testwizard.commands_core import CommandBase
from .ScreenshotResult import ScreenshotResult


class ScreenshotJPGCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.ScreenShotJPG")

    def execute(self, filename, quality):
        requestObj = [filename]
        if quality is not None:
            requestObj = [filename, quality]
            
        result = self.executeCommand(requestObj)

        return ScreenshotResult(result, "ScreenshotJPG was successful", "ScreenshotJPG failed")
