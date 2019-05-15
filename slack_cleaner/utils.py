# -*- coding: utf-8 -*-

import time


class Colors():
    HEADER = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    ENDC = ''
    BOLD = ''
    UNDERLINE = ''


class TimeRange():
    def __init__(self, start_time, end_time):
        def parse_ts(t):
            try:
                _time = time.mktime(time.strptime(t, "%Y%m%d"))
                return str(_time)
            except:
                return '0'
        self.start_ts = parse_ts(start_time)
        # Ensure we have the end time since slack will return in different way
        # if no end time supplied
        self.end_ts = parse_ts(end_time)
        if self.end_ts == '0':
            self.end_ts = str(time.time())


class Counter():
    def __init__(self):
        self.total = 0

    def increase(self):
        self.total += 1
