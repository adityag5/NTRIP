from NTRIP_Client import NtripClient

username = 'tr+zen01636701'
password = '65152416'
caster = 'ca.smartnetna.com'
port = 9950
mountpoint = 'MSM_VRS_ITRF14'
lat = 37.85917252094228
lon = -122.29157635549005
height = 14.0208

NtripClient.main([username, password, caster, port, mountpoint, lat, lon, height])