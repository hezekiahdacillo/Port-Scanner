from datetime import datetime
import socket
import ipaddress
import re


def print_logo():
    """
    Prints my logo.
    """
    print(r'''
     _   _  ____       ____ _   __ _       _       ____              _  _  _
    | | | |/ ___|____ / ___| | / /(_)     | |     |  _ \            (_)| || |
    | |_| | |_  |__  | |_  | |/ /  _  ____| |___  | | | | ____  ___  _ | || | ___
    |  _  |  _|   / /|  _| |   <  | |/ _  `  _  \ | | | |/ _  `/ __)| || || |/ _ \
    | | | | |__  / /_| |__ | |\ \ | | (_) | | | | | |_| | (_) | |__ | || || | (_) |
    |_| |_|\____|____|\____|_| \_\|_|\__,_|_| |_| |____/ \__,_|\___)|_||_||_|\___/
    ''')
    print()
    print('   ' + '*' * 80)
    print('   *' + (' ' * 78) + '*')
    print('   *' + (' ' * 21) + f'Copyright of Hezekiah Dacillo, {datetime.today().year}' + (' ' * 22) + '*')
    print('   *' + (' ' * 78) + '*')
    print('   ' + '*' * 80)
    print()
    print()


def error(message):
    """
    Prints the error message and exits the program.
    :param message: error message
    """
    print(message)


def get_ip():
    """
    Gets the IP for the nmnap to be scanned for open ports.
    """
    while True:
        ip_entered = input("\nPlease enter the ip address that you want to scan: ")
        try:
            ip_address_obj = ipaddress.ip_address(ip_entered)
            # The following line will only execute if the ip is valid.
            print("You entered a valid ip address.")
            break
        except:
            error('You entered an invalid ip address')
    return ip_entered
    

def get_port_range():
    """
    Gets the port range to be scanned for open ports.
    """
    port_range_pattern = re.compile('([0-9]+)-([0-9]+)')
    port_min = 0
    port_max = 65535
    while True:
        print('Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)')
        port_range = input('Enter port range: ')
        port_range_valid = port_range_pattern.search(port_range.replace(' ',''))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
    return [port_min, port_max]


def scan(port_min, port_max, ip):
    """
    Starts the process of scanning for open ports.
    """
    open_ports = []
    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip, port))
                open_ports.append(port)
        except:
            pass

    for port in open_ports:
        print(f'Port {port} is open on {ip}.')


if __name__ == '__main__':
    print_logo()
    ip = get_ip()
    port_min = get_port_range()[0]
    port_max = get_port_range()[1]
    scan(port_min, port_max, ip)
