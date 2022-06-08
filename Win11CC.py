"""https://valky.dev/"""

import os
from Utils import tools


class Win11CC:
    __file__ = "Win11CC.py"

    def __init__(self, config: dict, debug: bool):
        """
        - initialize
        """

        # Timer
        self._config = config
        self._debug = debug

    def controller(self):
        console = """
**************************************************************************************************************

                                    Valky's Windows 11 Core Console
                                              Version: 0.1
                                              
**************************************************************************************************************


        >> Browser
        ---------------------------------------------
        Edge            :       11
        Chrome          :       12
        
        
        >> Software
        ---------------------------------------------
        PyCharm         :       21
        WebStorm        :       22
        PhpStorm        :       23
        VS Code         :       24
        
        
        >> Misc
        ---------------------------------------------
        PowerShell      :       31
        Explorer        :       32
        Music           :       33
        Discord         :       34


**************************************************************************************************************

        $ > """

        startup = {
            11: "start msedge",
            12: "start chrome",

            21: "start pycharm",
            22: "start webstorm",
            23: "start phpstorm",
            24: "start code",

            31: "start pwsh",
            32: "explorer",
            33: "https://music.youtube.com",
            34: "start C:\\Users\\Valky\\AppData\\Local\\Discord\\Update.exe"
        }

        i0 = input(console)
        if i0.isdigit():
            os.system(startup[int(i0)])
            tools.createLog(f"Command '{startup[int(i0)]}'", self._debug)
        else:
            tools.createLog(f"ERROR: Unknown input '{i0}'", self._debug)

    def run(self):
        while True:
            self.controller()


if __name__ == '__main__':
    # Log recycle
    if os.path.exists(f"./logs/Win11CC.log"):
        tools.recycleLog()

    # Get config values
    _config = tools.readConfig('config.ini')
    if _config['Base']['debug'] == "True":
        _debug = True
    else:
        _debug = False

    # Start Console
    _Win11CC = Win11CC(_config, _debug)
    _Win11CC.run()
