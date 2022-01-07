from queue import Queue

IF_STATE_DOWN = 0
IF_STATE_UP = 1


class Iface:
    def __init__(self, name, speed, mac_adr, ip_adr, ip_mask):
        self.name = name
        self.speed = speed
        self.mac_adr = mac_adr
        self._ip_adr = ip_adr
        self._ip_mask = ip_mask

        self.in_queue = Queue()
        self.out_queue = Queue()
        self.state_up = False
        self.ttl_received = 0
        self.ttl_sent = 0
        self.ttl_errors = 0

        self.attached = None


    def send(self, packet):
        self.ttl_sent += 1
        self.out_queue.put(packet)

    def receive(self):
        self.ttl_received += 1

    def if_up(self):
        self.state_up = True

    def if_down(self):
        self.state_up = False

    @property
    def ip_addr(self):
        return self.ip_addr

    @ip_addr.setter
    def ip_addr(self, ip):
        self._ip_adr = ip

    @property
    def ip_mask(self):
        return self._ip_mask

    @ip_mask.setter
    def ip_mask(self, mask):
        self._ip_mask = mask

    @property
    def _format_speed(self):
        if self.speed >= 1_000_000_000:
            return f'{int(self.speed / 1_000_000_000)}Gbps'
        elif self.speed < 1_000_000_000 and self.speed >= 1_000_000:
            return f'{int(self.speed / 1_000_000)}Mbps'
        else:
            return f'{int(self.speed / 1000)}Kbps'


    def __str__(self):
        line =  f'{self.name} {"UP" if self.state_up else "DOWN"} {self._format_speed}'
        line += f' mac: {self.mac_adr} ip: {self._ip_adr}/{self._ip_mask}'
        line += f' Recv: {self.ttl_received} Sent: {self.ttl_sent} Errors: {self.ttl_errors}'

        return line
