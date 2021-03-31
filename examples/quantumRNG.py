import urllib.request as urlrequest
from numpy import array
# CASEY PANCOAST 2019
# Adapted from https://github.com/pcragone/anurandom/blob/master/anurandom.py
class ANURandom:
    BINARY = "BINARY"
    HEX = "HEX"
    CHAR = "CHAR"

    def getRandom(self,type):
        if type == self.BINARY:
            url = 'http://150.203.48.55/RawBin.php'
        elif type == self.HEX:
            url = 'http://150.203.48.55/RawHex.php'
        elif type == self.CHAR:
            url = 'http://150.203.48.55/RawChar.php'

        page = urlrequest.urlopen(url, timeout=10)

        data = page.read()
        num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
        return num

    def getBin(self):
        return self.getRandom(self.BINARY)

    def getHex(self):
        return self.getRandom(self.HEX)

    def getChar(self):
        return self.getRandom(self.CHAR)

def realrandom(k=1):
    anuRandom = ANURandom()
    ran = []
    i = 0
    while i<k:
        r = str(anuRandom.getBin())
        pr=len(r)
        initial = 5
        ran.append(float(r[initial:pr])/10**(pr-initial))
        i+=1
    return array(ran)