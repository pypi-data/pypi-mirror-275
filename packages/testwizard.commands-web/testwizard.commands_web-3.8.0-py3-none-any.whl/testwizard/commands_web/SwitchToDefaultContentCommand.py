from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class SwitchToDefaultContentCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.SwitchToDefaultContent")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "SwitchToDefaultContent was successful", "SwitchToDefaultContent failed")
