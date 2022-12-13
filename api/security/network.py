from typed import *
from socket import gethostbyname, gethostbyaddr
from dns.resolver import resolve
from geocoder import ip as geo
from ipaddress import ip_address, ip_network, IPv4Address, IPv6Address, IPv4Network, IPv6Network

record_types = [ 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV', 'TXT' ]


class Record(BaseModel):
    """Record model"""
    domain:str
    ttl:int
    type_:str
    value:str

class Network(object):
    """Scanning tools"""
    domain:str

    def __init__(self, domain:str):
        self.domain = domain

    def dns_records(self):
        """Get all records for a domain"""
        records = []
        for record_type in record_types:
            try:
                records.extend(str(resolve(self.domain, record_type).rrset).split('\n'))
            except Exception: # pylint: disable=broad-except
                pass
        responses = []
        for record in records:
            if record not in responses:
                record = record.split(' ')
                record.pop(2)
                record.pop(0)
                responses.append(record)
            if record[1] == 'MX':
                record.pop(2)
        return dumps([Record(domain=self.domain, ttl=int(record[0]), type_=record[1], value=record[2]).dict() for record in responses])

    def geo_location(self):
        """Get's geo information for a domain"""
        return dumps(geo(gethostbyname(self.domain)).json['raw'])

    def sub_domains(self):
        """Get's all subdomains for a domain"""
        response = []
        with open('./subdomains.txt', 'r', encoding='utf-8') as file:
            subdomains = file.read().split('\n')
            for subdomain in subdomains:
                try:
                    res = resolve(f"{subdomain}.{self.domain}", 'A')
                    for ipval in res:
                        response.append({"ip":str(ipval),"domain": f"{subdomain}.{self.domain}"})
                except Exception:
                    pass# pylint: disable=broad-except
        return dumps(response)
    
    @property
    def ip(self)->IPv4Address or IPv6Address:
        """Get's ip address for a domain"""
        return ip_address(gethostbyname(self.domain))
    
    @property
    def cidr(self)->IPv4Network or IPv6Network:
        """Get's cidr for a domain"""
        return ip_network(self.ip)
    
    @property
    def cidr_range(self)->List[IPv4Address or IPv6Address]:
        """Get's cidr range for a domain"""
        return list(self.cidr.hosts())
    
    @property
    def netmask(self)->str:
        """Get's netmask for a domain"""
        return str(self.cidr.netmask)
    
    @property
    def broadcast(self)->IPv4Address or IPv6Address:
        """Get's broadcast for a domain"""
        return str(self.cidr.broadcast_address)
    
    @property
    def network(self)->IPv4Network or IPv6Network:
        """Get's network for a domain"""
        return str(self.cidr.network_address)
    
    @property
    def is_private(self)->bool:
        """Get's if domain is private"""
        return self.cidr.is_private
    
    @property
    def is_global(self)->bool:
        """Get's if domain is global"""
        return self.cidr.is_global

class NetworkResource(APIRouter):
    """Network resource"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        @self.get('/dns/{domain}')
        async def dns(domain:str):
            """Get all records for a domain"""
            return Network(domain).dns_records()
    
        @self.get('/geo/{domain}')
        async def geo(domain:str):
            """Get's geo information for a domain"""
            return Network(domain).geo_location()
        
        @self.get('/sub/{domain}')
        async def sub(domain:str):
            """Get's all subdomains for a domain"""
            return Network(domain).sub_domains()
        
        @self.get('/net/{domain}')
        async def ip(domain:str):
            """Get's ip address for a domain"""
            network = Network(domain)
            return dumps({
                "ip": str(network.ip),
                "cidr": str(network.cidr),
                "cidr_range": [str(ip) for ip in network.cidr_range],
                "netmask": network.netmask,
                "broadcast": network.broadcast,
                "network": network.network,
                "is_private": network.is_private,
                "is_global": network.is_global
            })    
    
