import socket

from urllib2 import urlopen

from parsing import parse_discovery_response, parse_description

IFACE = '0.0.0.0'
SSDP_MCAST_ADDR = '239.255.255.250'
SSDP_PORT = 1900

class VieraFinder(object):

    def __init__(self):
        desc_url = self.discover()

        desc = urlopen(desc_url).read()
        self.viera = parse_description(desc, desc_url)

    def get_viera(self):
        return self.viera

    def create_new_listener(self, ip, port):
        newsock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
            socket.IPPROTO_UDP
        )
        newsock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1,
        )
        newsock.bind((ip, port))
        return newsock

    def discover(self):
        header = 'M-SEARCH * HTTP/1.1'
        fields = (
            ('ST', 'urn:panasonic-com:device:p00RemoteController:1'),
            ('MX', '1'),
            ('MAN', '"ssdp:discover"'),
            ('HOST', '239.255.255.250:1900'),
        )

        p = self._make_packet(header, fields)

        sock = self.create_new_listener(IFACE, SSDP_PORT)
        sock.sendto(p, (SSDP_MCAST_ADDR, SSDP_PORT))

        data = sock.recv(1024)

        location = parse_discovery_response(data)

        return location

    def _make_packet(self, header, fields):
        return '\r\n'.join([header] + [': '.join(pair) for pair in fields]) + '\r\n'
