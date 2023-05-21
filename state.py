from __future__ import annotations
from abc import ABC, abstractmethod


class Robot:
    state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Robot: Transition to {type(state).__name__}")
        self.state = state
        self.state.context = self

    def stop_running(self):
        self.state.handle_running_to_standby()

    def start_running(self):
        self.state.handle_standby_to_running()


class State(ABC):
    @property
    def context(self) -> Robot:
        return self._context

    @context.setter
    def context(self, context: Robot) -> None:
        self._context = context

    @abstractmethod
    def handle_running_to_standby(self) -> None:
        pass

    @abstractmethod
    def handle_standby_to_running(self) -> None:
        pass


class RobotRunningState(State):
    def handle_running_to_standby(self) -> None:
        print("Robot in running state handles stop_running.")
        print('\x1b[33mstopping motors\x1b[0m')
        print('\x1b[33mdisabling sensors\x1b[0m')
        print('\x1b[33msending running report\x1b[0m')
        self.context.transition_to(RobotStandbyState())

    def handle_standby_to_running(self) -> None:
        print("Robot in running state handles stop_running.")


class RobotStandbyState(State):
    def handle_running_to_standby(self) -> None:
        print("Robot in standby state handles start_running.")

    def handle_standby_to_running(self) -> None:
        print("Robot in standby state handles start_running.")
        print('\x1b[33mstarting motors\x1b[0m')
        print('\x1b[33menabling sensors\x1b[0m')
        print('\x1b[33mestablishing communication with controller\x1b[0m')
        self.context.transition_to(RobotRunningState())


if __name__ == "__main__":
    robot = Robot(RobotStandbyState())
    
    print('\n')
    robot.start_running()
    print('\n')
    robot.stop_running()
