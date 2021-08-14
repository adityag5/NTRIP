from NTRIP_Client import NtripClient as nc

username = 'tr+zen01636701'
password = '65152416'
caster = 'ca.smartnetna.com'
port = 9950
mountpoint = 'MSM_VRS_ITRF14'
lat = 37.85917252094228
lon = -122.29157635549005
height = 14.0208

ntripArgs = {}
ntripArgs['lat']= lat
ntripArgs['lon']= lon 
ntripArgs['height']= height
ntripArgs['user']= username + ":" + password
ntripArgs['caster']= caster
ntripArgs['port']= port 
ntripArgs['mountpoint']= mountpoint

if ntripArgs['mountpoint'][0:1] !="/":
    ntripArgs['mountpoint'] = "/"+ntripArgs['mountpoint']

ntripArgs['V2']= False

n = nc.NtripClient(**ntripArgs)

while True:
    data = n.read()

    if data is None:
        continue
    
    print(f'gotta send this {data}')