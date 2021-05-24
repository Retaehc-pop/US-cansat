import math


class coord:
    def __init__(self, Satlatitude, Satlongitude, Glatitude, Glongtitude, Sataltitude, Galtitude, gx, gy, gz):

        self.lat1 = math.radians(float(Satlatitude))
        self.lat2 = math.radians(float(Glatitude))
        self.lon1 = math.radians(float(Satlongitude))
        self.lon2 = math.radians(float(Glongtitude))
        self.dlon = self.lon2 - self.lon1
        self.dlat = self.lat2 - self.lat1

        self.a1 = float(Sataltitude)
        self.a2 = float(Galtitude)
        self.alt = self.a2 - self.a1

        self.gx = float(gx)
        self.gy = float(gy)
        self.gz = float(gz)

    def arc(self):
        a = (math.sin(self.dlat / 2) ** 2) + (
                    math.cos(self.lat1) * math.cos(self.lat2) * ((math.sin(self.dlon / 2)) ** 2))
        x = math.sqrt(a)
        y = math.sqrt(1 - a)
        c = 2 * math.atan2(x, y)
        return c

    def dist(self):
        R0 = 6371000
        d = R0 * self.arc()
        return d

    def lineofsight(self):
        R0 = 6371000
        R = R0 + self.a1
        baselength = 2 * R * math.cos((math.pi - self.arc()) / 2)
        heightlength = self.alt

        los = baselength ** 2 + heightlength ** 2 - 2 * baselength * heightlength * math.cos((math.pi + self.arc()) / 2)
        los = math.fabs(los)
        los = math.sqrt(los)

        return los

    def azimuth(self):
        a = math.sin(self.dlon) * math.cos(self.lat2)
        b = math.cos(self.lat1) * math.sin(self.lat2) - math.sin(self.lat1) * math.cos(self.lat2) * math.cos(self.dlon)
        theta = math.atan2(a, b)
        theta = math.degrees(theta)
        return theta

    def heading(self):
        ht = self.azimuth() - self.gz
        ht = ht % 360
        if ht >= 180:
            ht = ht - 360
        return ht

    def elevation(self):
        elev = math.atan2(self.alt, self.dist())
        elev = math.degrees(elev)
        elev = elev - self.gx
        elev = elev % 360
        if elev >= 180:
            elev = elev - 360
        return elev

    def roll(self):
        ty = self.gy
        ty = ty % 360
        if ty >= 180:
            ty = ty - 360
        return ty


if __name__ == '__main__':
    test = coord(12.0, 100.0, 12.5, 100.0, 20.1, 25600.2, 1.0, -3.0, 8.0)
    print(test.dist())
    print(test.lineofsight())
