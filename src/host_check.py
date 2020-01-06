import requests
from config import data
from user_agent import user_agent
import time
class host:
    def __init__(self, host):
        self.host = host
        if "https" in host:
            self.is_ssl = True
            self.port_used = 443
        else:
            self.port_used = 80
            
    def probe(self):
        fill = True
        x = {}
        try:
            start = time.clock()
            r = requests.get(
                self.host,
                headers=user_agent.get_headers(),
                #proxies=proxies.get(),
                timeout=data.probe_timeout,
                allow_redirects=True
                )
            request_time = time.clock() - start
        except Exception as E:
            print(E)
            x['status'] = ":exclamation:Down"
            x['status_code'] = 500
            x['request_time'] = "> 8 sec"
            fill = False
            
        if fill == True:            
            if r:
                x['status'] = ":white_check_mark:Up"
            else:
                x['status'] = ":warning:Problematic"
            x['status_code'] = r.status_code
            x['request_time'] = round(request_time, 4)
        x['port_used'] = self.port_used        
                     
        return x

        
        
        
            
        
