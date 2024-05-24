import sys
import json

from testwizard.commands_core import SessionCommandBase
from .StepExecutionResult import StepExecutionResult
from .EndStepResult import EndStepResult

class EndStepCommand(SessionCommandBase):
    def __init__(self, session):
        SessionCommandBase.__init__(self, session, "EndStep")

    def execute(self, result, message):
        requestObj = [result, message]

        result = self.executeCommand(requestObj)
        
        return EndStepResult(result, "EndStep was successful", "EndStep failed")        