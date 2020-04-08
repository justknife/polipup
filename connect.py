import paramiko
import time
from createbd import Table
import configparser


class Connect_ssh(object):
    paramiko.SSHClient().set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connecting(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        # username =
        # password =
        lore = paramiko.SSHClient()
        lore.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        lore.connect(hostname=config["SSH_user"]["hostname"], username=config["SSH_user"]["username"],
                     password=config["SSH_user"]["password"], port=22,
                     look_for_keys=False, timeout=600)
        ssh = lore.invoke_shell()
        return ssh

    def show_mac(ssh):
        """Take a mac_address_table"""
        command = "sh mac address-table"
        ssh.send('terminal length 0\n')
        time.sleep(1)
        ssh.recv(1000)
        ssh.send(command + '\n')
        time.sleep(2)
        result = ssh.recv(20000).decode('ascii')
        k = result.split()
        first_step = Table(k).clear_mac_info()
        body_first = Table(first_step).interfaces()
        body_two = Table(first_step).vlann()
        body_three = Table(first_step).typepi()
        body_four = Table(first_step).maci()
        two_step = Table.data_mac(body_first, body_four, body_three, body_two)
        return two_step
    def show_mac_hot(ssh,mac):
        command = "sh mac address-table | inc " + mac
        ssh.send('terminal length 0\n')
        time.sleep(1)
        ssh.recv(1000)
        ssh.send(command + '\n')
        time.sleep(2)
        result = ssh.recv(20000).decode('ascii')
        k = result.split()
        i = 0
        a = k
        while a[i] != 'DYNAMIC':
            a.pop(0)
        a.pop(0)
        a.pop(-1)
        return a[0]

    def current_host(ssh, password):
        """Current host it's"""
        command = 'ssh 10.100.43.2'
        print('connection ' + command)
        ssh.send('terminal length 0\n')
        time.sleep(1)
        ssh.recv(1000)
        ssh.send(command + '\n')
        ssh.send(password + '\n')
        time.sleep(2)

    def show_run(ssh, tell):
        """Show running config - send command"""
        command = "sh run int " + tell
        ssh.send('terminal length 0\n')
        time.sleep(1)
        ssh.recv(1000)
        ssh.send(command + '\n')
        time.sleep(2)
        result = ssh.recv(20000).decode('ascii')
        k = result.split()
        first_steep = Table.chown_run_inc(k)
        return first_steep

    def show_cdp_neighbors(ssh, parsmac):
        """Show cdp neighbors"""
        command = "show cdp neig"
        ssh.send('terminal length 0\n')
        time.sleep(1)
        ssh.recv(1000)
        ssh.send(command + '\n')
        time.sleep(2)
        result = ssh.recv(20000).decode('ascii')
        k = result.split()
        cdpneigh = Table.show_cdp_neighbors(k, parsmac)
        return cdpneigh

    def switch_host(ssh, nextip, password):
        """Current host it's"""
        command = 'ssh ' + nextip
        print('connection ' + command)
        ssh.send('terminal length 0\n')
        time.sleep(1)
        ssh.recv(1000)
        ssh.send(command + '\n')
        ssh.send(password + '\n')
        time.sleep(2)

    def switch_vlan(ssh, com):
        ssh.send('terminal length 0\n')
        time.sleep(1)
        ssh.recv(1000)
        ssh.send("conf t\n")
        time.sleep(2)
        ssh.recv(1000)
        ssh.send("int " + parsmac + "\n")
        time.sleep(1)
        ssh.recv(1000)
        ssh.send("switchport access vlan " + com + "\n")
        time.sleep(1)
        ssh.recv(1000)
        ssh.send("end\n")
        time.sleep(1)
        ssh.recv(1000)
        ssh.send("write")
        time.sleep(1)
        ssh.recv(1000)
        print('Succesful vlan switch')
