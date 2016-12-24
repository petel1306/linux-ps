#!/usr/bin/python
import os
def filter_pid():
    '''filter all subdirectories of /proc, in
    order to find all the processes
    '''
    pids=[]
    for pid in os.listdir('/proc'):
        try:
            int(pid)
            pids.append(pid)
        except ValueError:
            pass
    return pids
