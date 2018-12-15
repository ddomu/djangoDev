import requests, json, sys
import f5login 
# define program-wide variables


def get_arp(host):
    bigip = requests.session()
    bigip.auth = (f5login.username, f5login.password)
    bigip.verify = False
    bigip.headers.update({'Content-Type' : 'application/json'})
    
 
    # Requests requires a full URL to be sent as arg for every request, define base URL globally here
    BIGIP_URL_BASE = 'https://%s/mgmt/tm' % host

    arpstats = '/net/arp/stats' 
    arp_uri = BIGIP_URL_BASE+arpstats 
    print arp_uri
    # Response 
    r = bigip.get(arp_uri)
    rj = r.json()
    
    # Return value
    arp_dict = {} #{ipaddress:{mac:xxx, vlan:xxx, status:xxx}, ,,,, } 
    for k,v in rj['entries'].iteritems():
        entries =  v['nestedStats']['entries']
        ipAddress = str(entries['ipAddress']['description'])
        macAddress = str(entries ['macAddress']['description'])
        vlan = str(entries ['vlan']['description'])
        status =str (entries ['status']['description'])
        arp_dict[ipAddress] = {'mac':macAddress,'vlan':vlan, 'status': status }

    return arp_dict


# -- main() --- #
if __name__ == '__main__' : 
    if len(sys.argv)  ==  2: 
        # Usage : "python save_db.py 10.14.0.1  "
        host = sys.argv[1]
    else: 
        print "get_arp.py  <device ip/hostname >" 
        print "get_arp.py mtw-ltm1-tst1.nts.jhu.edu "
        #host = 'mtw-ltm1.nts.jhu.edu'
        #sys.exit()

    arp_dict = get_arp(host)
    if arp_dict is True : 
        print arp_dict 
    else : 
        sys.exit("Unable to update") 



