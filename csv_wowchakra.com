Type,Name,Address,Target,Port,String
SOA,europe-41.banahosting.com,107.6.171.35
NS,europe-42.banahosting.com,107.6.171.36
NS,europe-41.banahosting.com,107.6.171.35
MX,wowchakra.com,107.6.171.37
A,wowchakra.com,107.6.171.37
TXT,wowchakra.com,,,,'v=spf1 ip4:107.6.171.34 ip4:107.6.150.18 ip4:107.6.169.226 ip4:107.6.150.154 +a +mx include:relay.mailchannels.net ~all'
SRV,_caldav._tcp.wowchakra.com,107.6.171.34,europe-40.banahosting.com,2079
SRV,_caldavs._tcp.wowchakra.com,107.6.171.34,europe-40.banahosting.com,2080
SRV,_carddav._tcp.wowchakra.com,107.6.171.34,europe-40.banahosting.com,2079
SRV,_carddavs._tcp.wowchakra.com,107.6.171.34,europe-40.banahosting.com,2080
