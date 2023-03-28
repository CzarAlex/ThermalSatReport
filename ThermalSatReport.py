import json, datetime, time, json, urllib.request
from escpos.printer import Network

printer_ip = "192.168.0.233" # must be an IP address set as a string. If you're using Serial or USB, see https://python-escpos.readthedocs.io/en/latest/
api_key = "API STRING GOES IN HERE" # grab yours over at n2yo.com
sleep = 1 # Take a break between each JSON pull to give things time to catch up. Adjust as needed

data = urllib.request.urlopen("https://api.n2yo.com/rest/v1/satellite/radiopasses/27607/40.101/-76.085/150/1/5/&apiKey=" + api_key + "").read()
SO50 = json.loads(data)
time.sleep(sleep)
data = urllib.request.urlopen("https://api.n2yo.com/rest/v1/satellite/radiopasses/25544/40.101/-76.085/150/1/5/&apiKey=" + api_key + "").read()
ISS = json.loads(data)
time.sleep(sleep)
data = urllib.request.urlopen("https://api.n2yo.com/rest/v1/satellite/radiopasses/43017/40.101/-76.085/150/1/5/&apiKey=" + api_key + "").read()
AO91 = json.loads(data)
time.sleep(sleep)
data = urllib.request.urlopen("https://api.n2yo.com/rest/v1/satellite/radiopasses/54684/40.101/-76.085/150/1/5/&apiKey=" + api_key + "").read()
FO118 = json.loads(data)
time.sleep(sleep)

satlist = [SO50, ISS, AO91, FO118] #add/remove sats from here you wish to see data for
passlist = []

# This takes a string input of a day of the week and plops the proper suffix on the end.
def dayth(d):
    if (d in ['1', '21', '31']):
        return d + 'st'
    elif (d in ['2', '22']):
        return d + 'nd'
    elif (d in ['3', '23']):
        return d + 'rd'
    else:
        return d + "th"

# This takes a three letter compass point (NNW, ESE) and makes it just two. I don't need it that precise!        
def compasstrim(c):
    if (len(c) == 3):
        return c[1:]
    elif (len(c) == 1):
        return c.rjust(2, ' ')
    elif (len(c) == 2):
        return c
        
# Block to take the wonky given name of the satellite and turning it in to something familiar
def birdname(b):
    if (b == 'SPACE STATION'):
        return str('ISS'.ljust(6, ' '))
    elif (b == 'SAUDISAT 1C'):
        return str('SO-50'.ljust(6, ' '))
    elif (b == "FOX-1B (RADFXSAT AO-91)"):
        return str('AO-91'.ljust(6, ' '))
    elif (b == "OBJECT C"):
        return str('FO-118'.ljust(6, ' '))

for bird in satlist:
    for x in bird['passes']:
        nicetime = time.strftime('%I:%M%p', time.localtime(x['startUTC']))
        if (nicetime[0] == '0'):
            nicetime = nicetime.lstrip('0')
        if (len(nicetime) == 6):
            nicetime = ' ' + nicetime
        if (len(str(round(x['maxEl']))) == 2):
            maxel = ' ' + str(round(x['maxEl']))
        elif (len(str(round(x['maxEl']))) == 1):
            maxel = '  ' + str(round(x['maxEl']))
        passlist.append([birdname(bird['info']['satname']) + ' | ' + nicetime.lower() + maxel + "'" + ' ' + compasstrim(x['startAzCompass']) + ' -> ' + compasstrim(x['endAzCompass']), x['startUTC']])

# I have no idea how this sort voodoo works. but the [1] makes it sort by the second element which is the time
passlist.sort(key=lambda x: x[1])

p = Network(printer_ip)
p.set(align='center', font='b', width=2, height=1, custom_size=True, bold=False)
p.image("logo.gif")
p.text(time.strftime('%A %B', time.localtime()) + ' ' + dayth(time.strftime('%d', time.localtime())))
p.text("\n")
p.text("-----------------------------\n")
for satpass in passlist:
    p.text(str(satpass[0] + "\n"))
p.cut()     
