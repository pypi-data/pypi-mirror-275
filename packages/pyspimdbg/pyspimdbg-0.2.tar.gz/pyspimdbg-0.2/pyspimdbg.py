#! /usr/bin/env python

import pexpect
import time
import re
from termcolor import colored
import sys


class Spim(object):
    '''Main Spim class. See main() below for demo.

    Requires the command line version of Spim, available here:
    http://sourceforge.net/projects/spimsimulator/
    '''

    def __init__(self, debug = False):
        '''Spawns a Spim instance'''

        self.debug = debug
        self.last = ''
        self.last_user_input = False
        self.filename = ''
        self.syscalls = {
            1: 'print_int',
            4: 'print_string',
            5: 'read_int',
            8: 'read_string',
            10: 'exit',
            11: 'print_char',
            12: 'read_char',
        }
        
        self.sp = pexpect.spawn ('spim')
        self._expect('\(spim\) ')
        if not b'(spim)' in self.sp.after:
            #print 'one more...'
            #self._expect('.*')
            raise Exception('Could not get spim prompt. Is it installed?\n\nOutput was:\n%s' % self.sp.after)


    def _sendline(self, line):
        '''Expect a response from the underlying child process. Respects debug mode. Private.'''

        if not self.sp.isalive():
            raise Exception('Child spim process died.')
        if self.debug:
            print('\nSENDING:', line)
        self.sp.sendline(line)


    def _expect(self, pattern, timeout=-1, searchwindowsize=None):
        '''Expect a response from the underlying child process. Respects debug mode. Private.'''
        
        if not self.sp.isalive():
            raise Exception('Child spim process died.')
        if self.debug:
            print('\nEXPECTING:', pattern)
        index = self.sp.expect(pattern, timeout=timeout, searchwindowsize=searchwindowsize)
        if self.debug:
            print('GOT BEFORE: "%s"' % self.sp.before)
            print('GOT  AFTER: "%s"' % self.sp.after)
        return index


    def load(self, filename):
        '''Loads a program from a *.s file'''
        
        self._sendline('load "%s"' % filename)
        index = self._expect(['Cannot open file.*\(spim\) ',
                             '\(spim\) ',
                             pexpect.EOF,
                             pexpect.TIMEOUT],
                            timeout = 1)
        self.filename = filename
        if index == 0:
            raise Exception('Could not load file "%s"' % filename)
        elif index == 1:
            pass
        elif index == 2:
            raise Exception('Spim EOF: process died?')
        elif index == 3:
            raise Exception('Spim timeout')
        else:
            raise Exception('Unknown error with expect.')


    def run(self, timeout = 10, timeoutFatal = False):
        '''Runs the (presumably) loaded program. Returns None on
        successful exection or string containing text output on
        timeout.'''

        self._sendline('run')
        index = self._expect(['.*\(spim\) ',
                             pexpect.EOF,
                             pexpect.TIMEOUT],
                            timeout = timeout)

        if index == 0:
            # Return the output when the program runs successfully
            output = self.sp.before.decode('utf-8') + self.sp.after.decode('utf-8')
            if output.endswith('(spim) '):
                output = output[:-7]  # remove (spim) from the end
            return output
        elif index == 1:
            raise Exception('Spim EOF: process died?')
        elif index == 2:
            # Timeout, so just grab whatever is there
            index = self._expect(['.*',
                                  pexpect.EOF,
                                  pexpect.TIMEOUT],
                                 timeout = .1)
            if index == 0 or index == 1:
                return self.sp.before.decode('utf-8') + self.sp.after.decode('utf-8')
            else:
                return ''   # Another timeout
        else:
            raise Exception('Unknown error with expect.')


    def reg(self, register, timeout = 1):
        '''Gets the current value from the given register.

        Any of the following calling conventions is fine:
        spim.reg(5)
        spim.reg("$5")
        spim.reg("t0")
        spim.reg("$v0")
        '''
        
        if isinstance(register, int):
            register = str(register)
        if register[0:1] != '$':
            register = '$' + register
        self._sendline('print %s' % register)
        index = self._expect(['.*Reg.*0x([0-9a-f])+.*\(spim\) ',
                             '.*Unknown label:.*\(spim\) ',
                             pexpect.EOF,
                             pexpect.TIMEOUT],
                            timeout = timeout)

        if index == 0:
            match = re.search('.*Reg.* = (0x[0-9a-f]+) .*\(spim\) ', self.sp.after.decode('utf-8'), re.DOTALL)
            value = int(match.group(1), 0)   # base 0 -> interpret 0x... as hex
            return value
        elif index == 1:
            raise Exception('Spim: Unknown label: %s' % register)
        elif index == 2:
            raise Exception('Spim EOF: process died?')
        elif index == 3:
            raise Exception('Spim timeout')
        else:
            raise Exception('Unknown error with expect.')
    
    def print_all_regs(self, timeout = 1):
        '''Prints all the registers'''
        print(colored('---------------- [REGISTERS] ----------------', 'blue'))

        self._sendline('print_all_regs hex')
        
        # time.sleep(0.1)
        index = self._expect(['.*\(spim\) ',
                             pexpect.EOF,
                             pexpect.TIMEOUT],
                            timeout = timeout)

        if index == 0:
            # Get the output
            output = self.sp.before.decode('utf-8') + self.sp.after.decode('utf-8')

            # Split the output into lines
            lines = output.split('\n')

            # Remove the last line
            lines = lines[:-1]

            # Join the lines back together and print the result
            print('\n'.join(lines))
            print(colored('-'*45, 'blue'))
        elif index == 1:
            raise Exception('Spim EOF: process died?')
        elif index == 2:
            raise Exception('Spim timeout')
        else:
            raise Exception('Unknown error with expect.')
        
    def prompt(self):
        print(colored('pyspimdbg> ', 'red'), end = '')
        user_input = input("")
        if user_input == '':
            user_input = self.last
            # self.print_all_regs()
        else:
            self.last = user_input
        if user_input == 'quit' or user_input == 'q':
            self.quit()
            exit()
        if user_input == 'r':
            return 'run' 
        if user_input == 'reload' or user_input == 'rel':
            self.reload()
            return f"load \"{self.filename}\""
        elif user_input.split(" ")[0] == 'b':
            user_input = 'breakpoint ' + user_input.split(" ")[1]
        else:
            self.print_all_regs()
        return user_input
        
    def interactive(self):
        '''Gives the user the possibility to use spim by hand'''
        
        user_input = self.prompt()
        
        v0 = self.reg(2)
        self._sendline(user_input)
        while True:
            
            self.debug and print("Sent command: ", user_input)
            # time.sleep(0.1)
            index = self._expect(['.*\(spim\)', pexpect.EOF, pexpect.TIMEOUT], timeout = 0.2)
            self.debug and print("Index: ", index)
            
            
            if index == 0:
                # Get the output of the command
                if not self.last_user_input:
                    output = self.sp.before.decode('utf-8') + self.sp.after.decode('utf-8')
                    self.debug and print(colored("Output: ", 'light_red'), output)
                    output = output.split('\n')[1:]
                    output = '\n'.join(output)
                    output = output[:-6]
                    print(output)
                    
                    # if syscall, print syscall details
                    if 'syscall' in output:
                        syscall_code = self.reg(2)
                        print(colored(f"\tSyscall code: {syscall_code} ({self.syscalls.get(syscall_code, 'unknown')})", 'light_magenta'))
                        if syscall_code == 1:
                            print(colored(f"\tPrinted value: {self.reg(4)}", 'light_magenta'))  # $a0
                        elif syscall_code == 4:
                            end_str = False
                            offset = 0
                            print(colored(f"\tPrint string: addr={hex(self.reg(4))}", 'light_magenta'))
                            # print string
                            print(colored(f"\tPrinting string: ", 'light_magenta'), end='')
                            print(colored("\"", 'cyan'), end='')
                            while not end_str:
                                addr = self.reg(4) + offset
                                self._sendline(f"print {addr}")
                                # the output of the format is: Data seg @ 0x10010000 (268500992) = 0x65736e49 (1702063689)
                                # the first bytes of the string are after the equal sign, in hex, but before the integer representation of the string
                                index = self._expect(['.*= 0x([0-9a-f]+) \([0-9]+\)\r\n\(spim\)', pexpect.EOF, pexpect.TIMEOUT], timeout = 0.2)
                                # print(self.sp.before, self.sp.after)
                                output_str = self.sp.before.decode('utf-8') + self.sp.after.decode('utf-8')
                                output_str = output_str.split('= ')[1]
                                output_str = output_str.split(' ')[0]
                                output_str = output_str[2:]
                                # print(colored(f"\tPrinted string: {output_str}", 'light_magenta'))
                                byte_str = bytes.fromhex(output_str)
                                output_str = byte_str.decode('utf-8')[::-1]
                                print(colored(f"{output_str}", 'cyan'), end='')
                                offset += 4
                                if b'\x00' in byte_str:
                                    end_str = True
                            print(colored("\"", 'cyan'))
                            
                            
                        elif syscall_code == 5:
                            print(colored(f"\tRead integer", 'light_magenta'))
                        elif syscall_code == 8:
                            print(colored(f"\tRead string, input buffer: {hex(self.reg(4))}", 'light_magenta'))
                        elif syscall_code == 11:
                            print(colored(f"\tPrinted char: {chr(self.reg(4))}", 'light_magenta'))
                        elif syscall_code == 12:
                            print(colored(f"\tRead char", 'light_magenta'))
                        
                            
                else:
                    # pass
                    self.debug and print("Expecting user input case ")
                    output = ''
                    if type(self.sp.after) == bytes:
                        output += self.sp.after.decode('utf-8')
                        
                    output = output.split('\n')[1:]
                    
                    output = '\n'.join(output)
                    output = output[:-6]
                    print(output)
                            
                self.last_user_input = False
                user_input = self.prompt()
                # self.print_all_regs()
                v0 = self.reg(2)
                self._sendline(user_input)
            if index == 1:
                raise Exception('Spim EOF: process died?')
            elif index == 2:
                self.debug and print("Timeout, expecting user input")
                output = self.sp.before.decode()
                if type(self.sp.after) == bytes:
                    output += self.sp.after.decode()
                output = output.split('\n')[1:]
                output = '\n'.join(output)
                print(output)
                self.sp.expect('.*')
                
                if 'syscall' in output:
                    # self._sendline('\x03')
                    syscall_code = v0
                    print(colored(f"\tSyscall code: {syscall_code} ({self.syscalls.get(syscall_code, 'unknown')})", 'light_magenta'))
                    if syscall_code == 5:
                        print(colored(f"\tRead integer", 'light_magenta'))
                    elif syscall_code == 8:
                        print(colored(f"\tRead string", 'light_magenta'))
                    elif syscall_code == 12:
                        print(colored(f"\tRead char", 'light_magenta'))
                    # self._sendline('s')
                
                user_input = input(colored('[user input expected] ','green'))
                self._sendline(user_input)
                self.last_user_input = True


    def quit(self, timeout = 1):
        '''Quits the child spim process'''
        
        self._sendline('quit')
        index = self._expect([pexpect.EOF,
                             pexpect.TIMEOUT],
                            timeout = timeout)

        if index == 0:
            pass
        elif index == 1:
            raise Exception('Spim timeout')
        else:
            raise Exception('Unknown error with expect.')
    
    def reload(self):
        '''Reloads the program from a *.s file'''
        filename = self.filename
        self._sendline('reinitialize')
        index = self._expect(['.*README.*', pexpect.EOF, pexpect.TIMEOUT], timeout = 1)
        if index == 0:
            print("Reload complete")
            pass
        elif index == 1:
            pass
        elif index == 2:
            raise Exception('Spim EOF: process died?')
        elif index == 3:
            raise Exception('Spim timeout')
        else:
            raise Exception('Unknown error with expect.')
        



def main():
    if len(sys.argv) != 2:
        print("Usage: pyspimdbg <filename.s>")
        sys.exit(1)
        
    filename = sys.argv[1]
    spim = Spim(debug=False)
    
    spim.load(filename)
    spim.interactive()
    spim.quit()



if __name__ == '__main__':
    main()
