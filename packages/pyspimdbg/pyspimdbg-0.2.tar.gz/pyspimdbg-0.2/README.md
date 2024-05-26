About pyspimdbg
=====================

[pyspimdbg](https://github.com/Gabrain24/pyspimdbg) is a very minimal Python
interface to [SPIM](http://sourceforge.net/projects/spimsimulator/), so as to make
MIPS32 debugging easier. Pyspimdbg is known to work on Linux.



Installing pyspimdbg
=====================

First install the requirements:

1. [SPIM](http://spimsimulator.sourceforge.net/)

2. The [pexepct](http://sourceforge.net/projects/pexpect/) Python module. Users with ```pip``` can install pexpect via

        sudo pip install pexpect

Then, install pyspim itself:

    git clone git@github.com:Gabrain24/pyspimdbg.git
    cd pyspim/
    ./install.sh



Example Usage
=====================

Basic Usage
---------------------

The basic commands for interacting with SPIM to load and run the included [```test.s```](https://github.com/yosinski/pyspim/blob/master/test.s) are shown below.

    spim = Spim(debug = False)      # Start the underlying SPIM process

    spim.load('test.s')             # Load a .s file
    spim.run()                      # Run the loaded file
    print 't0 is', spim.reg(8)      # Get the value from a register

    spim.quit()                     # Quit the underlying spim process


Debugging
---------------------
This version attempts to provide a simple interface to SPIM's debugging
Run using ```pyspimdbg <filename>```
Commands:
- ```run``` - Run the program (alias: ```r```)
- ```step``` - Step through the program (alias: ```s```)
- ```quit``` - Quit the debugger (alias: ```q```)
- ```break``` - Set a breakpoint at a line number (alias: ```b```)
and all the basic spim commands



License
=======================

Pyspimdbg is released under the [GNU GPL v3](http://www.gnu.org/licenses/gpl.txt).


This is a fork of the original [pyspim](https://github.com/yosinski/pyspim)
