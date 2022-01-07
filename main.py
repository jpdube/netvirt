from iface import Iface

def main():
    print('Network simulator')
    eth0 = Iface('eth0', 1_000_000_000, '00:01:02:03:04:05', '192.168.242.144', '255.255.255.0')
    eth0.ip_addr = '24.37.16.64'
    eth0.ip_mask = '255.255.255.239'
    print(eth0)

    eth1 = Iface('eth1', 40_000_000_000,'0a:01:02:03:04:05', '10.0.0.18', '255.255.255.0')
    eth1.if_up()
    eth1.send(None)
    print(eth1)

    eth2 = Iface('eth2', 5_000_000,'0b:01:02:03:04:05', '192.168.2.14', '255.255.255.0')
    print(eth2)

    eth3 = Iface('eth3', 1_000,'0c:01:02:03:04:05', '192.168.242.149', '255.255.255.0')
    print(eth3)


if __name__ == '__main__':
    main()
