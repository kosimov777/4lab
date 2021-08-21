#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    s = input("Введите слово: ")
    print(s)
    s = s.replace('о', ' ', 1)
    #print(s)
    line = ''.join(reversed(list(s)))
    #print(line)
    line = line.replace('л', ' ',1)
    #print(line)
    e = ''.join(reversed(list(line)))
    print(e)