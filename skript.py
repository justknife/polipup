#!/usr/bin/env python3.8
#Software License Agreement (BSD License)
#Copyright (c) 2020 Mikhael Ivanov(justknife)
#All rights reserved.




import time
from connect import Connect_ssh
import configparser
import gui

nextip = None
parsmac = None
portmode = None
cdpneigh = None
endi = None
ssh = Connect_ssh
config = configparser.ConfigParser()
config.read("config.ini")
password = config["SSH_user"]["password"]
wsehosti = {}
try:
    connect = ssh.connecting('o')
    ssh.current_host(connect,password)
    while True:
        c = input('input command: ')
        if c == 'shmac':
            """Take a mac_address_table"""

            macpac = input('input mac_address: ')
            def sorted_mac():
                """Sort mac address table and find port to mac address when you find"""
                df = ssh.show_mac(connect)
                a = df.loc[df['Mac_Address'].str.contains(macpac), 'Interfaces'].tolist()
                while len(a) >= 2:
                    a.pop(0)
                return a[0]

            three_step = sorted_mac()
            print(three_step)
        elif c == 'shrun':

            """Show running config - send command"""
            ssh.show_run(connect)

        elif c == 'shcdp':
            """Show cdp neighbors"""
            ssh.show_cdp_neighbors(ssh)
        elif c == 'showw':
            mac = input('input mac: ')
            ssh.show_mac_hot(connect, mac)
        elif c == 'find':
            macpac = input('input mac_address:')
            while True:
                endi = portmode
                while endi != 'trunk':
                    try:
                        """Take a mac_address_table"""
                        if len(macpac) == 4:
                            three_step = ssh.show_mac_hot(connect,macpac)

                        else:
                            def sorted_mac():
                                """Sort mac address table and find port to mac address when you find"""
                                df = ssh.show_mac(connect)
                                a = df.loc[df['Mac_Address'].str.contains(macpac), 'Interfaces'].tolist()
                                while len(a) >= 2:
                                    a.pop(0)
                                return a[0]
                            three_step = sorted_mac()
                    except:
                        print('error mac not found.Sorry bro')
                        break
                    parsmac = three_step
                    print(parsmac)

                    """Show run module"""

                    tell = parsmac
                    if tell == 'CPU':
                        print('Error. Not supported  find System mac address')
                        break
                    else:
                        first_steep = ssh.show_run(connect,tell)
                        portmode = first_steep
                        print(portmode)
                        """Show cdp neighbors module """
                    if portmode == 'access':
                        print('Succesfull! Mac_address:', macpac, 'find on this commutator:', nextip, '\n')
                        c = input('Do yo want switch vlan?yes/no(default no)')
                        try:
                            if c == 'yes':
                                com = input('input vlan(300-defender network,310-users vlan): ')
                                ssh.switch_vlan(connect, com)
                                break
                            else:
                                print('Aborted by user')
                                break
                        except:
                            print('unknown error when i switch config.Maybe connection close.Please try again')
                            break
                    else:
                        cdpneigh = ssh.show_cdp_neighbors(connect,parsmac)

                        """Current host it's"""
                        nextip = wsehosti[cdpneigh]
                        ssh.switch_host(connect,nextip,password)
                break

        elif c == 'exit':
            break

except:
    print('server not avaible')
