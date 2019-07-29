## Python Virtual Enviroment

Because we do not want to influence the local system python pip library version, we create independent environment for the project

Open poject folder with shell, and follow below command to create the project virtual environment:

    $projectpath: python -m venv project-env

Next, for windows 10, follow below command to switch the environment:
    $projectpath: project-env\Script\activate.bat

Other OS command to swich the environment, please go to [pyQt5 tutorial page](https://build-system.fman.io/pyqt5-tutorial)

## Install PyQt5
We want to write the python graphical user interface.there are so much python GUI framework such as: tkinter, Kivy, wxPython, PyQt. We decide to use PyQt as our project graphical user interfac framework.

Follow below command to install framework:

    $(project-env) projectpath: pip install pyQt5==5.9.2

## Visual Studio Code Setting
We want to intellisense can work on **project-env**.

    Press Key: Ctrl + Shift + P
    Input keyword to select interpreter: Python: Select Interpreter
    Click interpreter from the list: Python XXX ('project-env':venv)

VSCode will show not found QtXXX in QtXXX when import Qt module.Because "Pylint doesn't load any C extensions by default, because those can run arbitrary code", Pylint bring out the import probelm.

We need to add some rule in **.vscode folder/settings.json**, input following below rule in settings.json:


        {
            "python.pythonPath": "tutorial-env\\Scripts\\python.exe",
            "python.linting.pylintArgs": ["--extension-pkg-whitelist=PyQt5"]  // Added rule
        }
