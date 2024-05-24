from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class SwitchToFirstWindowCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.SwitchToFirstWindow")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "SwitchToFirstWindow was successful", "SwitchToFirstWindow failed")
