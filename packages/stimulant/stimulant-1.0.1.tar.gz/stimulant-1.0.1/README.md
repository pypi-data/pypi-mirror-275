# Stimulant

Keeps the screen awake by moving the mouse randomly.

## Description

Stimulant is intended to be used as a cli tool or imported to another python project.

If used as a cli tool or with importing stimulant(), Stimulant will move the mouse for the specified runtime. While under the runtime the mouse will move to a random location on the screen. This process will repeat at random intervals. The movement of the mouse is achieved using the pyautogui library. Pyautogui's duration and tweening parameters allow for more natural mouse movement patterns across the screen. To terminate Stimulant, simply press any key on the keyboard.

For more granular control over the logic, the Stimulant class can be imported. The class, along with its public methods, allows for customized use cases to be implemented. An example may be to have the mouse move for an unknown duration of time that would be determined by another process.

## Installation

1. Have Python 3.12+ installed (may work with older versions of python)
    - [How to install](https://www.python.org/downloads/)

2. Execute the following command in your console

```console
pip install stimulant

# or install from git repo
pip install git+https://github.com/sidganti/stimulant.git
```

## Documentation

### CLI

#### Run indefinitely

```console
stim
```

#### Run for a specified time in seconds

Limited to one day aka 86,400 seconds.

If 0 is given as an argument then Stimulant will run indefinitely.

```console
stim <0-86400>
```

or

```console
stim -t <0-86400>
```

or

```console
stim --time <0-86400>
```

#### Hotcorner protection

Pass the flag to prevent triggering [hotcorners](https://support.apple.com/guide/mac-help/use-hot-corners-mchlp3000/mac) enabled on your device.

```console
stim -c
```

or

```console
stim --corners
```

#### End Stimulant manually

Press any key on the keyboard.

In case something pressing any single key went wrong, you have two options. Use you operating systems preferred termination signal: <kbd>ctrl</kbd>+<kbd>c</kbd> on Mac/Linux or <kbd>ctrl</kbd>+<kbd>z</kbd> on Windows. Since pyautogui's failsafe option is enabled you can also drag your mouse to the top left corner of the screen to terminate.

#### Help

Provides detail on CLI's usage.

```console
stim -h
```

or

```console
stim --help
```

#### Version

Prints the version of Stimulant

```console
stim -V
```

or

```console
stim --version
```

### stimulant() function

Functions nearly identical to the CLI. The CLI is essentially a wrapper for the stimulant() function.

```python
# recommended individual import
from stimulant import stimulant

# recommended module import
import stimulant as stim
```

```python
# stimulant function definition
def stimulant(runtime: int = 0, hotcorners: bool = False) -> None:
```

- runtime
    - duration the instance should run
    - if 0 is passed in to the function then stimulant will run indefinitely
- hotcorners
    - prevents mouse from reaching the edges of the screen

```python
# example function call
stimulant(600, True)
```

### Stimulant class

Encapsulates all of the data and logic required to move the mouse for a specified duration of time.

```python
# recommended individual import
from stimulant import Stimulant

# recommended module import
import stimulant as stim
```

```python
# Stimulant class constructor definition
def __init__(self, runtime: int = 0, hotcorners: bool = False, animate: bool = True) -> None:
```

- runtime
    - duration the instance should run
- hotcorners
    - prevents mouse from touching the edges of the screen
- animate
    - flag to determine write to console

```python
# example instantiation
stim = Stimulant(600, True)
```

#### start() method

Starts logic to run Stimulant for a specified duration.

```python
# start method definition
def start(self):
```

```python
# example call
stim.start()
```

#### run() method

Alias for the start() method

```python
# run method definition
def run(self):
```

```python
# example call
stim.run()
```

#### move_mouse() method

Moves the mouse to a random position on the screen for a random duration. Also takes advantage of pyautogui's tweening functions to make mouse movement more natural.

```python
# move_mouse method definition
def move_mouse(self) -> None:
```

```python
# example call
stim.move_mouse()
```

#### stop() method

Safely terminates Stimulant instance

```python
# stop method definition
def stop(self) -> None:
```

```python
# example call
stim.stop()
```

## Future
- Improve threading to allow exception handling and safer thread termination
- Allow access to more variables to cli and class/function calls
- Ability to kill stimulant via callback function

## License

[LICENSE](LICENSE)