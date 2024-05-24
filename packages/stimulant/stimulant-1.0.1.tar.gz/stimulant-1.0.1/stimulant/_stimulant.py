"""
Keeps the screen awake by moving the mouse randomly
"""
import threading
import platform
import time
from itertools import cycle
import random
import sys

import pyautogui


class Stimulant:
    """
    Class to encapsulate data and logic

    *runtime*
        duration the instance should run
    *hotcorners*
        prevents mouse from touching the edges of the screen
    *animate*
        flag to determine write to console
    """
    def __init__(self, runtime: int = 0, hotcorners: bool = False, animate: bool = True) -> None:
        self.runtime = runtime
        self.hotcorners = hotcorners
        self.animate = animate

        self.system = platform.system()

        # running thread initialization
        self._running_thread = threading.Thread(target=self._running_animation)
        self._running_thread.daemon = True

        # keyboard listener initialization
        self._key_thread = threading.Thread(target=self._key_pressed)
        self._key_thread.daemon = True

        # mouse thread initialization
        self._mouse_thread = threading.Thread(target=self.move_mouse)
        self._mouse_thread.daemon = True

        # pyautogui initialization
        pyautogui.FAILSAFE = True
        self._screen_width, self._screen_height = pyautogui.size()
        self._tweening_functions = [
            pyautogui.easeInQuad,
            pyautogui.easeOutQuad,
            pyautogui.easeInOutQuad,
            pyautogui.easeInBounce,
            pyautogui.easeInElastic
        ]

        # prevents icon popup on macos
        if self.system == 'Darwin':
            from AppKit import NSBundle # pylint: disable=no-name-in-module import-outside-toplevel
            app_info = NSBundle.mainBundle().infoDictionary()
            app_info["LSBackgroundOnly"] = "1"

    def _running_animation(self):
        """
        Renders an animation to cli while the instance is running
        """
        loading_frames = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]

        start_time = time.monotonic()
        for frame in cycle(loading_frames):
            time_delta = int(time.monotonic() - start_time)
            runtime = '∞' if self.runtime == 0 else self.runtime
            print(f'Running {time_delta}/{runtime}s {frame}', flush=True, end='\r')
            time.sleep(0.1)

    def run(self):
        """
        Starts background threads and main logic
        """
        return self.start()

    def start(self):
        """
        Starts background threads and main logic
        """
        self._key_thread.start()
        if self.animate:
            self._running_thread.start()

        reinit_thread = False

        end_time = time.monotonic() + self.runtime
        while self._under_runtime(end_time):
            interval = random.randint(5, 10)
            interval_time = time.monotonic() + interval

            if reinit_thread and not self._mouse_thread.is_alive():
                self._mouse_thread = threading.Thread(target=self.move_mouse)
                self._mouse_thread.daemon = True
                self._mouse_thread.start()
            elif not reinit_thread:
                reinit_thread = True
                self._mouse_thread.start()
            else:
                continue

            while time.monotonic() < interval_time and self._under_runtime(end_time):
                if not self._key_thread.is_alive():
                    self.stop()

                time.sleep(0.01)

    def _under_runtime(self, end_time: float) -> bool:
        """
        Check to keep running the program

        *end_time*
            time the loop should end
        """
        if self.runtime == 0:
            return True

        curr_time = time.monotonic()
        return curr_time < end_time

    def move_mouse(self) -> None:
        """
        Moves mouse to random position on screen
        """
        screen_x = (0, self._screen_width)
        screen_y = (0, self._screen_height)
        if self.hotcorners:
            padding_x = int(self._screen_width * 0.1)
            padding_y = int(self._screen_height * 0.1)

            screen_x = (0 + padding_x, self._screen_width - padding_x)
            screen_y = (0 + padding_y, self._screen_height - padding_y)

        pos_x = random.randint(*screen_x)
        pos_y = random.randint(*screen_y)
        duration = random.randint(1, 5)
        tween = random.choice(self._tweening_functions)

        try:
            pyautogui.moveTo(pos_x, pos_y, duration, tween)
        except pyautogui.FailSafeException:
            pass

    def _key_pressed(self):
        """
        Listens to keypresses using getch
        """
        self._getch()

    def _getch(self):
        """
        Reads a character from stdin
        """
        if self.system == 'Darwin' or self.system == 'Linux':
            # pylint: disable=import-outside-toplevel multiple-imports import-error
            import tty, termios

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setcbreak(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            # Exit on ctrl-c, ctrl-d, ctrl-z, or ESC
            if ord(ch) in [3, 4, 26, 27]:
                sys.exit()
            return ch

        elif self.system == 'Windows':
            import msvcrt # pylint: disable=import-outside-toplevel import-error

            return msvcrt.getch()
        else:
            # Java not supported
            pass

    def stop(self) -> None:
        """
        Safely terminates instance
        """
        sys.stdout.flush()
        sys.exit()


def stimulant(runtime: int = 0, hotcorners: bool = False) -> None:
    """
    Keeps the screen awake for specified duration

    *runtime*
        duration the instance should run
    *hotcorners*
        prevents mouse from reaching the edges of the screen
    """
    stim = Stimulant(runtime, hotcorners)
    stim.run()
    stim.stop()
