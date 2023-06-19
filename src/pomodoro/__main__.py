"""Main module for the Pomodoro.

Contains the main script for the CLI command.
"""

from re import S
from rich.console import Console
from rich.progress import Progress, TaskID
from dataclasses import dataclass
import time
from typing import List
from datetime import datetime, timedelta


@dataclass
class ProgramPart:
    title: str
    duration_in_seconds: int
    color: str = 'green'
    is_pause: bool = False


def pomodoro_main() -> None:
    """Main function for the Pomodoro application.

    Starts the timers and displays them as nice progressbars.
    """
    # TODO: Move to configfile
    stint_seconds = 25 * 60
    small_pause = 5 * 60
    big_pause = 10 * 60

    day_program = [
        ProgramPart(
            title='Stint 1 [25m]',
            duration_in_seconds=stint_seconds,
            color='red'),
        ProgramPart(
            title='Pause 1 [ 5m]',
            is_pause=True,
            duration_in_seconds=small_pause,
            color='green'),
        ProgramPart(
            title='Stint 2 [25m]',
            duration_in_seconds=stint_seconds,
            color='red'),
        ProgramPart(
            title='Pause 2 [ 5m]',
            is_pause=True,
            duration_in_seconds=small_pause,
            color='green'),
        ProgramPart(
            title='Stint 3 [25m]',
            duration_in_seconds=stint_seconds,
            color='red'),
        ProgramPart(
            title='Pause 3 [ 5m]',
            is_pause=True,
            duration_in_seconds=small_pause,
            color='green'),
        ProgramPart(
            title='Stint 4 [25m]',
            duration_in_seconds=stint_seconds,
            color='red'),
        ProgramPart(
            title='Pause 4 [10m]',
            is_pause=True,
            duration_in_seconds=big_pause,
            color='green'),
    ]

    console = Console()

    # Calculate the staticstics
    total_time_in_seconds = sum([
        stint.duration_in_seconds
        for stint in day_program
    ])
    total_pause_in_seconds = sum([
        stint.duration_in_seconds
        for stint in day_program
        if stint.is_pause
    ])
    start = datetime.now()
    end = start + timedelta(seconds=total_time_in_seconds)

    # Print the statistics
    console.print('Starting the workday!\n')
    console.print(f'-> Pause time: {total_pause_in_seconds} seconds')
    console.print(
        f'-> Work time:  {total_time_in_seconds - total_pause_in_seconds} seconds')
    console.print(f'-> Start:      {start:%H:%M:%S}')
    console.print(f'-> End:        {end:%H:%M:%S}\n')

    with Progress() as progress:
        # Add the tasks
        _ = [
            progress.add_task(
                f'[{item.color}]{item.title}[/]',
                total=item.duration_in_seconds)
            for item in day_program]
        current_task = 0

        # Start the loop
        while not progress.finished:
            # Get the task
            task = progress.tasks[current_task]
            if task.finished:
                current_task += 1
                task = progress.tasks[current_task]

            # Update the task
            progress.update(task.id, advance=1)

            # Wait a second
            time.sleep(1)


if __name__ == '__main__':
    pomodoro_main()
