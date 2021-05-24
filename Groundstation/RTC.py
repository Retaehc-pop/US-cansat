from datetime import datetime
import time

start_time = time.time()


class GetTime:
    def __init__(self):
        self.set_time()

    def set_time(self):
        global start_time
        self.start_time = time.time()

    @staticmethod
    def time_pc():
        stime = datetime.now().time()
        if stime.second % 2 == 0:
            timestp = str('%02d' % stime.hour) + ' ' + str('%02d' % stime.minute) + \
                      ' ' + str('%02d' % stime.second) + '.' + str(stime.microsecond)[0:2]
        else:
            timestp = str('%02d' % stime.hour) + ':' + str('%02d' % stime.minute) + \
                      ':' + str('%02d' % stime.second) + '.' + str(stime.microsecond)[0:2]
        time.sleep(0.01)
        return timestp

    def time_elapsed(self):
        delta = time.time() - self.start_time
        second = delta % 60
        microsecond = str(datetime.now().time().microsecond)[0:2]
        minute = delta / 60
        minute = minute % 60
        hour = minute / 60

        if int(second) % 2 == 0:
            timestp = str('%02d' % hour) + ' ' + str('%02d' % minute) + \
                      ' ' + str('%02d' % second) + '.' + microsecond
        else:
            timestp = str('%02d' % hour) + ':' + str('%02d' % minute) + \
                      ':' + str('%02d' % second) + '.' + microsecond
        time.sleep(0.01)

        return timestp
