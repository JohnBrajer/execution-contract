"""Reference state machine for John Brajer's Execution Contract."""
from dataclasses import dataclass
from enum import Enum


class Stage(str, Enum):
    INTENT = "intent"
    SUCCESS_STATE = "success_state"
    EXECUTION = "execution"
    OBSERVATION = "observation"
    VERIFICATION = "verification"
    RETRY_ADAPT = "retry_adapt"
    COMPLETE = "complete"


_ALLOWED = {
    Stage.INTENT: {Stage.SUCCESS_STATE},
    Stage.SUCCESS_STATE: {Stage.EXECUTION},
    Stage.EXECUTION: {Stage.OBSERVATION},
    Stage.OBSERVATION: {Stage.VERIFICATION},
    Stage.VERIFICATION: {Stage.COMPLETE, Stage.RETRY_ADAPT},
    Stage.RETRY_ADAPT: {Stage.EXECUTION},
    Stage.COMPLETE: set(),
}


@dataclass
class Execution:
    stage: Stage = Stage.INTENT

    def advance(self, next_stage: Stage) -> None:
        if next_stage not in _ALLOWED[self.stage]:
            raise ValueError(f"Invalid transition: {self.stage} -> {next_stage}")
        self.stage = next_stage


if __name__ == "__main__":
    run = Execution()
    for stage in [
        Stage.SUCCESS_STATE,
        Stage.EXECUTION,
        Stage.OBSERVATION,
        Stage.VERIFICATION,
        Stage.COMPLETE,
    ]:
        run.advance(stage)
    print(run.stage)
