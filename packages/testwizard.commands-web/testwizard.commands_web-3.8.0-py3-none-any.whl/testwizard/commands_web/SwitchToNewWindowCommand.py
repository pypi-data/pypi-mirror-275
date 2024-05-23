from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class SwitchToNewWindowCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.SwitchToNewWindow")

    def execute(self, windowName, url):
        requestObj = [windowName]
        if url is not None:
            requestObj = [windowName, url]
            
        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "SwitchToNewWindow was successful", "SwitchToNewWindow failed")
