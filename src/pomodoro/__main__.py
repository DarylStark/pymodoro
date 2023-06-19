"""Main module for the Pomodoro.

Contains the main script for the CLI command.
"""

from re import S
from rich.console import Console
from rich.progress import Progress, TaskID
from dataclasses import dataclass
import time
from typing import List


@dataclass
class ProgramPart:
    title: str
    duration_in_seconds: int


def pomodoro_main() -> None:
    """Main function for the Pomodoro application.

    Starts the timers and displays them as nice progressbars.
    """
    stint_seconds = 25 * 60
    small_pause = 5 * 60
    big_pause = 10 * 60

    day_program = [
        ProgramPart(title='Stint 1 [25m]', duration_in_seconds=stint_seconds),
        ProgramPart(title='Pause 1 [ 5m]', duration_in_seconds=small_pause),
        ProgramPart(title='Stint 2 [25m]', duration_in_seconds=stint_seconds),
        ProgramPart(title='Pause 2 [ 5m]', duration_in_seconds=small_pause),
        ProgramPart(title='Stint 3 [25m]', duration_in_seconds=stint_seconds),
        ProgramPart(title='Pause 3 [ 5m]', duration_in_seconds=small_pause),
        ProgramPart(title='Stint 4 [25m]', duration_in_seconds=stint_seconds),
        ProgramPart(title='Pause 4 [10m]', duration_in_seconds=big_pause)
    ]

    with Progress() as progress:
        tasks: List[TaskID] = [progress.add_task(item.title, total=item.duration_in_seconds)
                               for item in day_program]
        current_task = 0

        while not progress.finished:
            progress.update(tasks[current_task], advance=1)
            time.sleep(1)


if __name__ == '__main__':
    pomodoro_main()
