# /usr/bin/env python
# Update script to build database of updatable ports
#
#
import re
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT

pkg_cmd = "pkg_version -v"

DEBUG = False

ports = {}
class port:
    name = ""
    status = "" # holds <, >, !, * which gives easy information 
    version = "" # version numbers
    human = "" # pkg_version "human readable" upgrade procedure
    info = "" # the result of the pkg_info command
    updating = "" # any relevant updating info
    


def pkg_version():
    
    cmd = "pkg_version -Iv"
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    if DEBUG:
        print 'Building ports list from pkg_version\n'
    for x in output.split('\n'):
        try:    
            key, status, human  = re.split(pattern='\s{1,}', string=x, maxsplit=2)
            if DEBUG:
                print ' ... ',
            name, version = key.rsplit('-',1)
            thisport = port()
            thisport.name = name
            thisport.version = version
            thisport.status = status
            thisport.human = human
            ports[key] = thisport   
        except ValueError:
            if DEBUG:
                print "\nParse error:"+name

def pkg_info():
    
    cmd = "pkg_info " + ' && pkg_info '.join(ports.keys())
    print '\n' + cmd
    print '\nLooking up some extra info\n'
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    for x in re.split(pattern='\n{4,}', string=output):
        for key in ports.keys():
            if x.find(key) >= 0:
                print ' ... ',
                if DEBUG:
                    print x
                ports[key].info = x
             
def UPDATING():
    
    path = "/usr/ports/UPDATING"
    file_handler = open(path, 'r')
    port_list = re.split(pattern='\d{8}:',string=file_handler.read())
#    print port_list
# get info from pkg_version to build list
pkg_version()

# run pkg_info to get a nice human readable info text
#pkg_info()

#UPDATING()

