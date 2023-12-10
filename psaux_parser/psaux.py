#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import subprocess as sp
from datetime import datetime


class Process:
    def __init__(self, proc_data):
        self.user = proc_data[0]
        self.pid = int(proc_data[1])
        self.cpu_percent = float(proc_data[2])
        self.mem_percent = float(proc_data[3])
        self.vsz = int(proc_data[4])
        self.rss = int(proc_data[5])
        self.tty = proc_data[6]
        self.stat = proc_data[7]
        self.start = proc_data[8]
        self.time = proc_data[9]
        self.command = proc_data[10]

    def __repr__(self):
        return f'Process(' \
               f'pid={self.pid}, ' \
               f'command={self.command[:20]}, ' \
               f'user={self.user}, ' \
               f'vsz={self.vsz}, ' \
               f'cpu={self.cpu_percent})'

class PsAux:
    def __init__(self):
        self.process_list = None

        proc = sp.Popen(
            'ps aux',
            shell=True,
            stdout=sp.PIPE,
            stderr=sp.PIPE,
            universal_newlines=True
        )
        stdout, stderr = proc.communicate()
        stdout_list = stdout.splitlines()
        headers = stdout_list[0].split(None)
        proc_data_list = [s.strip().split(None, len(headers) - 1) for s in stdout_list[1:]]
        self.process_list = [Process(p) for p in proc_data_list]

    def users(self):
        return sorted(list(set(p.user for p in self.process_list)))

    def count_process(self):
        return len(self.process_list)

    def count_process_by_user(self, user):
        return len([p for p in self.process_list if p.user == user])

    def total_virtual_memory_size(self):
        return round(sum(p.vsz for p in self.process_list) / 2**10, 2)

    def total_resident_set_size(self):
        return round(sum(p.rss for p in self.process_list) / 2**10, 2)

    def total_cpu_percent(self):
        return round(sum(p.cpu_percent for p in self.process_list), 2)

    def total_mem_percent(self):
        return round(sum(p.mem_percent for p in self.process_list), 2)

    def max_memory_process(self):
        return max(self.process_list, key=lambda p: p.vsz).command[:20]

    def max_cpu_process(self):
        return max(self.process_list, key=lambda p: p.cpu_percent).command[:20]


def save_report(ps_aux, path_to_dir='.', show_report=True):
    now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
    report_name = f'{now}_scan'

    with open(f'{path_to_dir}/{report_name}', 'w') as report:
        report.write('Пользователи системы: ')
        report.write(', '.join(ps_aux.users()) + '\n')
        report.write(f'Количество процессов: {ps_aux.count_process()}\n')
        report.write('Пользовательских процессов:\n')

        for user in ps_aux.users():
            report.write(f'  {user}: {ps_aux.count_process_by_user(user)}\n')

        report.write(f'Всего памяти используется (VSZ): {ps_aux.total_virtual_memory_size()} Mb\n')
        report.write(f'Всего памяти используется (RSS): {ps_aux.total_resident_set_size()} Mb\n')
        report.write(f'Всего CPU используется: {ps_aux.total_cpu_percent()}%\n')
        report.write(f'Всего MEM используется: {ps_aux.total_mem_percent()}%\n')
        report.write(f'Больше всего памяти использует: {ps_aux.max_memory_process()}\n')
        report.write(f'Больше всего CPU использует: {ps_aux.max_cpu_process()}\n')

    if show_report:
        sp.run(f'cat {path_to_dir}/{report_name}', shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='ps aux parser')
    parser.add_argument('-d', '--path-to-dir', default='.')
    args = parser.parse_args()

    ps_aux = PsAux()
    save_report(ps_aux, path_to_dir=args.path_to_dir)
