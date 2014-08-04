import urllib2

class Viera(object):
    def __init__(self, hostname, control_url, service_type):
        self.hostname = hostname
        self.control_url = control_url
        self.service_type = service_type

        self.sendkey_action = Action('X_SendKey', ('X_KeyEvent',))

    def _sendkey(self, slug):
        req = self.sendkey_action.to_soap_request(
            self.control_url,
            self.hostname,
            self.service_type,
            (slug,),
        )

        urllib2.urlopen(req).read()

    def __unicode__(self):
        return u'<Hostname:%s ControlURL:%s ServiceType:%s>' % (
            self.hostname,
            self.control_url,
            self.service_type,
        )

    def vol_up(self):
        self._sendkey('NRC_VOLUP-ONOFF')

    def vol_down(self):
        self._sendkey('NRC_VOLDOWN-ONOFF')

    def mute(self):
        self._sendkey('NRC_MUTE-ONOFF')

    def num(self, number):
        for digit in str(number):
            self._sendkey('NRC_D%s-ONOFF' % digit)

    def power(self):
        self._sendkey('NRC_TV-ONOFF')

    def toggle_3D(self):
        self._sendkey('NRC_3D-ONOFF')

    def toggle_SDCard(self):
        self._sendkey('NRC_SD_CARD-ONOFF')

    def red(self):
        self._sendkey('NRC_RED-ONOFF')

    def green(self):
        self._sendkey('NRC_GREEN-ONOFF')

    def yellow(self):
        self._sendkey('NRC_YELLOW-ONOFF')

    def blue(self):
        self._sendkey('NRC_BLUE-ONOFF')

    def vtools(self):
        self._sendkey('NRC_VTOOLS-ONOFF')

    def cancel(self):
        self._sendkey('NRC_CANCEL-ONOFF')

    def option(self):
        self._sendkey('NRC_SUBMENU-ONOFF')

    def Return(self):
        self.sendkey('NRC_RETURN-ONOFF')

    def enter(self):
        self._sendkey('NRC_ENTER-ONOFF')

    def right(self):
        self._sendkey('NRC_RIGHT-ONOFF')

    def left(self):
        self._sendkey('NRC_LEFT-ONOFF')

    def up(self):
        self._sendkey('NRC_UP-ONOFF')

    def down(self):
        self._sendkey('NRC_DOWN-ONOFF')

    def display(self):
        self._sendkey('NRC_DISP_MODE-ONOFF')

    def menu(self):
        self._sendkey('NRC_MENU-ONOFF')

    def connect(self):
        self._sendkey('NRC_INTERNET-ONOFF')

    def link(self):
        self._sendkey('NRC_VIERA_LINK-ONOFF')

    def guide(self):
        self._sendkey('NRC_EPG-ONOFF')

    def text(self):
        self._sendkey('NRC_TEXT-ONOFF')

    def subtitles(self):
        self._sendkey('NRC_STTL-ONOFF')

    def info(self):
        self._sendkey('NRC_INFO-ONOFF')

    def index(self):
        self._sendkey('NRC_INDEX-ONOFF')

    def hold(self):
        self._sendkey('NRC_HOLD-ONOFF')

class Action(object):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def to_soap_request(self, url, hostname, service_type, values):
        assert len(values) == len(self.arguments)

        params = ''.join(['<%s>%s</%s>' % (arg, value, arg) for arg, value in zip(self.arguments, values)])

        soap_body = (
            '<?xml version="1.0"?>'
            '<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
            '<SOAP-ENV:Body>'
            '<m:%(method_name)s xmlns:m="%(service_type)s">'
            '%(params)s'
            '</m:%(method_name)s>'
            '</SOAP-ENV:Body>'
        '</SOAP-ENV:Envelope>'
        ) % {
            'method_name': self.name,
            'service_type': service_type,
            'params': params,
        }

        headers = {
            'Host': hostname,
            'Content-Length': len(soap_body),
            'Content-Type': 'text/xml',
            'SOAPAction': '"%s#%s"' % (service_type, self.name),
        }

        req = urllib2.Request(url, soap_body, headers)

        return req
