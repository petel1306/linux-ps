#!/usr/bin/python
import os
def filter_processes():
    '''filter all subdirectories of /proc,
    in order to find all the processes
    '''
    pids=[]
    for process in os.listdir('/proc'):
        try:
            int(process)
            pids.append(process)
        except ValueError:
            pass
    return pids
def ps():
    '''print this information for all running processes:
        1. pid
        2. ppid
        3. comm
        4. utime
        5. num_threads
        6. processor
        7. vsize
    '''
    for pid in filter_processes():
        proc_file = open('/proc/{}/stat'.format(pid))
        stat = proc_file.read().split()
        proc_file.close()
        print ('pid: {},  ppid: {},  comm:s {},  utime: {},  '
        + 'num_threads: {},  processor: {},  vsize: {}').format(pid, stat[3], stat[1][1:-1], stat[13], stat[19], stat[38], stat[22])
ps()
