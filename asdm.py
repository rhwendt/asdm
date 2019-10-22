#!/usr/bin/env python
import argparse
import shlex as s
import re
import os
from subprocess import call

def connect_asdm(ip, port):
    exceptions_path =  '~/.java/deployment/security/exception.sites'
    p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'

    exception_hosts = {}
    if not os.path.exists(os.path.expanduser(exceptions_path)):
        try:
            os.makedirs(os.path.dirname(os.path.expanduser(exceptions_path)))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
        f = open(os.path.expanduser(exceptions_path), 'w')
        f.write()
        f.close()

    with open(os.path.expanduser(exceptions_path), 'r') as file:
        for line in file:
            match = re.search(p, line)
            ehost = match.group('host').strip()
            eport = match.group('port')

            if eport == '':
                eport = '443'

            exception_hosts.update({ ehost: eport })


    # override exception_hosts from user input
    exception_hosts.update({ ip: port })

    file_contents = ''
    for host in sorted(exception_hosts.keys()):
        if exception_hosts[host] == '443':
            file_contents += 'https://' + host + '\n'
        else:
            file_contents += 'https://' + host + ':' +  exception_hosts[host] + '\n'

    f = open(os.path.expanduser(exceptions_path), 'w')
    f.write(file_contents)
    f.close()

    # set the command string
    # javaws "https://1.1.1.1:8443/admin/public/asdm.jnlp"
    if port == '443':
        command = 'javaws https://'+ ip + '/admin/public/asdm.jnlp'
    else:
        command = 'javaws https://'+ ip + ':' + port + '/admin/public/asdm.jnlp'

    call(s.split(command))

def main():
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=200, width=200))

    prog_args = [
        ('-i','--ip-address','ip','hostname or IP address of ASA',
            dict(default='', action='store', required=True)),
        ('-p','--port','port','asdm port - default 8443',
            dict(default='8443', action='store'))
    ]

    for arg1, arg2, dest, help, options in prog_args:
        parser.add_argument(arg1, arg2, dest=dest, help=help, **options)

    options = parser.parse_args()

    if options.ip:
        connect_asdm(options.ip, options.port)


if __name__ == '__main__':
        main()
