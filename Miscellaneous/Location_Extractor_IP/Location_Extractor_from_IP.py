# pip install pygeoip

import pygeoip

# Open-source IP Geolocation Database
gip = pygeoip.GeoIP("GeoLiteCity.dat")
# Insert IP address
res = gip.record_by_addr('')

for key,val in res.items():
    print('%s : %s' %(key,val))

'''Post-execution of this code, you can obtain Country name, City name,
area code, postal code, region, latitude and longitude from the output.'''
