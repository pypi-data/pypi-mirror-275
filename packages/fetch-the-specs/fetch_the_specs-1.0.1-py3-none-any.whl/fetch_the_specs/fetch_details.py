import platform
import psutil
from rich.console import Console
from rich.table import Table
import socket
from datetime import datetime

def get_system_info():
    info = {
        'Hostname': socket.gethostname(),
        'OS': platform.system(),
        'OS Version': platform.version(),
        'Architecture': platform.architecture()[0],
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Total RAM': f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        'Available RAM': f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
        'Disk Total': f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB",
        'Disk Used': f"{psutil.disk_usage('/').used / (1024 ** 3):.2f} GB",
        'Disk Free': f"{psutil.disk_usage('/').free / (1024 ** 3):.2f} GB",
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'MAC Address': ':'.join(['{:02x}'.format((psutil.net_if_addrs()['eth0'][0].address >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]) if 'eth0' in psutil.net_if_addrs() else 'N/A',
        'Uptime': str(datetime.now() - datetime.fromtimestamp(psutil.boot_time())),
        'Boot Time': datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        'CPU Usage': f"{psutil.cpu_percent(interval=1)}%"
    }

    return info

def format_info(info):
    table = Table(title='System Information')

    table.add_column('Component', style='bold cyan')
    table.add_column('Details', style='bold green')

    for key, value in info.items():
        table.add_row(key, str(value))
    
    return table


def main():

    system_info = get_system_info()
    table = format_info(system_info)

    console = Console()
    console.print(table)

if __name__ == '__main__':
    main()