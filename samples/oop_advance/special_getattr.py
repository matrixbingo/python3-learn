#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from samples.utils import console as util

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
util.console('-')
print(s.score)
util.console('-')
print(s.age())
util.console('-')
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)
