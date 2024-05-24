from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class SwitchToPreviousWindowCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.SwitchToPreviousWindow")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "SwitchToPreviousWindow was successful", "SwitchToPreviousWindow failed")
