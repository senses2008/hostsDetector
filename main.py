#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'To detect hosts file infection'

__author__ = 'Sunnie Chen'

import platform
import detector
from detector.strategy.MutiIP import MutilIP
from detector.strategy.IStrategy import IStrategy
from detector.strategy.MutilLocalhost import MutilLocalhost
from detector.strategy.MutiReturn import MutilReturn
from detector.strategy.SuperBlack import SuperBlack
from detector.HostsReader import HostsReader
from detector.Host import Host
from detector.StrategyList import StrategyList

def makeStrategyList() -> StrategyList:
    slist = StrategyList()
    slist.regist(MutilIP())
    slist.regist(MutilReturn())
    slist.regist(SuperBlack())
    slist.regist(MutilLocalhost())
    return slist

def main():
    slist = makeStrategyList()
    reader = HostsReader()
    for line in reader.ReadLines():
        slist.notify(Host(line))

    if slist.result():
        print("[结果] hosts文件已经被感染")
    else:
        print("[结果] hosts文件未被感染")

    slist.print()
    
    return

if __name__ == '__main__':
    main()