from abc import ABC, abstractmethod
from dataclasses import dataclass
import time


@dataclass
class RaceTrack:
    points: list[tuple]


class LineFollowingStrategy(ABC):
    @abstractmethod
    def run(self, race_track: RaceTrack) -> None:
        pass


class LearingStrategy(LineFollowingStrategy):
    def run(self, race_track: RaceTrack) -> None:
        print(f'Scanning the track...')
        for point in race_track.points:
            time.sleep(1.25)
            print(f'Saved point {point}')
        print('Scan completed\n')


class CompetitionStrategy(LineFollowingStrategy):
    def run(self, race_track: RaceTrack) -> None:
        print(f'Going max speed...')
        for point in race_track.points:
            time.sleep(0.5)
            print(f'Passed point {point}')
        print('Finished race\n')


class Robot:
    def __init__(self, race_track: RaceTrack) -> None:
        self.track = race_track

    def movement(self, strategy: LineFollowingStrategy) -> None:
        strategy.run(self.track)


if __name__ == "__main__":
    track = RaceTrack([(1, 2), (3, 4), (0, 3), (-1, 4)])
    robot = Robot(track)

    print('Robot slowly runs through the track to scan the path')
    robot.movement(LearingStrategy())

    print('Robot starts the race going as fast as possible')
    robot.movement(CompetitionStrategy())
