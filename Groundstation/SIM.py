import random
import binascii
import time
from datetime import datetime

n = int(input("input a number of packet"))
a = 0
with open("simi.xml", 'w') as file:
    file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n")
    file.write("<data>\n")
    file.write("  <loop>true</loop>\n")
    file.write("  <repeat_times>1</repeat_times>\n")
    file.write("  <repeat_period>1000</repeat_period>\n")
    file.write("  <packets_list>\n")

    for i in range(n + 1):
        stime = datetime.now().time()
        t = str('%02d' % stime.hour) + ':' + str('%02d' % stime.minute) + \
            ':' + str('%02d' % stime.second)
        if a <= 1000:
            a += 15
        else:
            a = 0
        temp = random.randrange(40)
        V = random.randrange(12)
        gsat = random.randrange(9)
        gla = random.uniform(13.0, 13.5)
        glo = random.uniform(100.0, 100.5)
        ro1 = random.uniform(50, 100)
        pres = random.uniform(50, 100)
        p10 = random.uniform(1, 200)
        p25 = random.uniform(1, 200)
        roooo = round(random.uniform(0, 100),2)

        teamid = str(binascii.hexlify(b'3751'), "ascii")
        packet = str(binascii.hexlify(str(i).encode()), "ascii")
        mode = str(binascii.hexlify(str("F").encode()), "ascii")
        sp1r = str(binascii.hexlify(str("R").encode()), "ascii")
        sp2r = str(binascii.hexlify(str("R").encode()), "ascii")
        pkgtypec = str(binascii.hexlify(b'C'), "ascii")
        pkgtypeP1 = str(binascii.hexlify(b'S1'), "ascii")
        pkgtypeP2 = str(binascii.hexlify(b'S2'), "ascii")
        time = str(binascii.hexlify(str(t).encode()), "ascii")
        alt = str(binascii.hexlify((str(a).encode())), "ascii")
        tem = str(binascii.hexlify(str(temp).encode()), "ascii")
        voltage = str(binascii.hexlify(str(V).encode()), "ascii")
        gpstime = str(binascii.hexlify(str(t).encode()), "ascii")
        gpsla = str(binascii.hexlify((str(gla).encode())), "ascii")
        pressure = str(binascii.hexlify((str(pres).encode())), "ascii")
        gpslon = str(binascii.hexlify((str(glo).encode())), "ascii")
        gpsalt = str(binascii.hexlify((str(a).encode())), "ascii")
        gpsat = str(binascii.hexlify((str(gsat).encode())), "ascii")
        pm10 = str(binascii.hexlify((str(p10).encode())), "ascii")
        pm25 = str(binascii.hexlify((str(p25).encode())), "ascii")
        rotation = str(binascii.hexlify((str(roooo).encode())), "ascii")
        swstage = str(binascii.hexlify(b'Launch'), "ascii")
        cmd = str(binascii.hexlify(b'ST'), "ascii")
        com = str(binascii.hexlify(b','), "ascii")

        cp = teamid + com + time + com + packet + com + pkgtypec + com + mode + com + sp1r + com + sp2r + com + alt + com + tem + com + voltage + com + gpstime + com + gpsla + com + gpslon + com + gpsalt + com + gpsat + com + swstage + com + packet + com + packet + com + cmd + '24'
        s1p = teamid + com + time + com + packet + com + pkgtypeP1 + com + alt + com + tem + com + rotation + com + gpsla + com + gpslon + '24'
        s2p = teamid + com + time + com + packet + com + pkgtypeP2 + com + alt + com + tem + com + rotation + com + gpsla + com + gpslon + '24'

        file.write(f"    <packet name=\"c-{i}\">\n")
        file.write("      <payload>" + cp + "</payload>\n")
        file.write("    </packet>\n")
        file.write(f"    <packet name=\"sp1-{i}\">\n")
        file.write("      <payload>" + s1p + "</payload>\n")
        file.write("    </packet>\n")
        file.write(f"    <packet name=\"sp2-{i}\">\n")
        file.write("      <payload>" + s2p + "</payload>\n")
        file.write("    </packet>\n")

    file.write("  </packets_list>")
    file.write("</data>")
