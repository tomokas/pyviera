import urlparse

from lxml import objectify

from viera import Viera

class NoServiceDescriptionError(StandardError): pass

def parse_discovery_response(data):
    for line in data.splitlines():
        parts = line.split(': ')
        if len(parts) > 1 and parts[0] == 'LOCATION':
            return parts[1]

def parse_description(data, abs_url):
    desc = objectify.fromstring(data)

    try:
        service = desc.device.serviceList.service

        service_type = service.serviceType.text
        control_url= urlparse.urljoin(abs_url, service.controlURL.text)

        # Unused urls
        #service_id = urlparse.urljoin(abs_url, service.serviceId.text)
        #scpd_url = urlparse.urljoin(abs_url, service.SCPDURL.text)
        #event_url = urlparse.urljoin(abs_url, service.eventSubURL.text)

        hostname = urlparse.urlparse(abs_url).netloc

        return Viera(
            hostname,
            control_url,
            service_type,
        )
    except AttributeError:
        raise NoServiceDescriptionError
