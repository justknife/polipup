import pandas as pd
from itertools import groupby

class Table(object):
    """Create pandas table and more """

    def __init__(self, parserdata):
        self.parserdata = parserdata

    def interfaces(self):
        """Table interface on method non()"""
        interface = []
        b = 3
        while b < len(self.parserdata):
            interface.append(self.parserdata[b])
            b += 4
        return interface

    # Parsing mac address table module == mac and vlan
    def maci(self):
        """Table mac address on method clear_mac_info()"""
        mac = []
        b = 1
        while b < len(self.parserdata):
            mac.append(self.parserdata[b])
            b += 4
        return mac

    ### Parsing TYPE Interfaces
    def typepi(self):
        """Table of type interface on method clear_mac_info()"""
        typep = []
        b = 2
        while b < len(self.parserdata):
            typep.append(self.parserdata[b])
            b += 4
        return typep

    # Parsing Vlandata
    def vlann(self):
        """Table vlan on method clear_mac_info()"""
        vlan = []
        b = 0
        while b < len(self.parserdata):
            vlan.append(self.parserdata[b])
            b += 4
        return vlan



    def clear_mac_info(self):

        """ Create pure information on command show mac address table(after need parsing this)"""
        try:

            k = []
            for line in self.parserdata:
                a = (line.replace('   ', ' '))
                u = (a.replace('-', ''))
                b = (u.replace('\n', ''))
                c = (b.replace(',,', ''))
                d = (c.replace(',', ''))
                l = d.strip()
                k.append(l)
            k = [el for el, _ in groupby(k)]
            a = k
            g = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            for i in g:
                a.pop(0)
            d = [0, 1, 2, 3, 4, 5, 6, 7]
            for i in d:
                a.pop(-1)
            return a
        except:
            print('error in module sort mac info')

    def show_cdp_neighbors(data,betta):


        """ Give info on Cisco 2960 on command show cdp neigbords(need parsing after sort data)"""

        try:
            i = 0
            a = data
            # a.replace('Gig','Gi')
            while a[i] != 'Port':
                a.pop(0)
            a.pop(0)
            a.pop(0)
            d = [0]
            for i in d:
                a.pop(-1)
            l = a.count('S')
            # print(l)
            i = 0
            while i < l:
                a.remove('S')
                a.remove('I')
                i += 1
            if 'R' in a:
                a.remove('R')
            b = 3
            n = []
            while b < len(a):
                a.pop(b)
                b += 6
            b = 1
            while b < len(a):
                a.pop(b)
                b += 5
            b = 0
            while b < len(a):
                n.append(a[b])
                b += 5
            k = []
            b = 1
            while b < len(a):
                on = 'Gi' + a[b]
                k.append(on)
                b += 5
            data = {'Name': n, 'Interfaces': k}
            df = pd.DataFrame(data)
            pd.options.display.max_rows = 200
            betta
            a = df.loc[df['Interfaces'].str.contains(betta), 'Name'].tolist()

            return a[0]
        except:
            print('error in module cdp neighbors')
    def chown_run_inc(runinfo):

        """"Give a information on interfaces by command show run | inc + interface when you find"""
        try:
            i = 0
            a = runinfo
            while a[i] != 'mode':
                if a == []:
                    print('error 232')
                    break
                else:
                    a.pop(0)
            a.pop(0)
            # d = [1, 2, 3, 4]
            # for i in d:
            #     a.pop(-1)
            return a[0]
        except:
            print('error data module (chown_run)')
    def sorted_mac(parsinfo,needfindd):
        """Sort mac address table and find port to mac address when you find"""
        try:
            df = parsinfo
            a = df.loc[df['Mac_Address'].str.contains(needfindd), 'Interfaces'].tolist()
            while len(a) >= 2:
                a.pop(0)
            return a[0]
        except:
            print('error data module (sorted_mac)')
    def show_run_inc(self):
        """Give info bu sdp neighbors needed"""
        try:
            df = self.chown_run_inc()
            a = df.loc[df['Name'].str.contains(None), 'Interfaces'].tolist()
            while len(a) >= 2:
                a.pop(0)
            return a[0]
        except:
            print('error data module (show run)')

    def data_mac(interfaces,maci,typepi,vlann):
        """Create pandas table"""
        try:
            debuger = {'Interfaces': interfaces, 'Mac_Address': maci, 'Type': typepi,
                       'Vlan': vlann}
            df = pd.DataFrame(debuger)
            pd.options.display.max_rows = 200
            return df
        except:
            print('error data module (data_mac)')
    def parngb(self):
        """Create database on information by command show cdp neighbor on cisco 2960\\not in use"""
        data = {}
