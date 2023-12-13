#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from pprint import pprint

class Log:
    IP = 'ip'
    DATETIME = 'datetime'
    METHOD = 'method'
    URL = 'url'
    HTTP_VERS = 'http_vers'
    HTTP_STATUS = 'http_status'
    RESPONSE_BYTES = 'response_bytes'
    SOURCE_URL = 'source_url'
    USER_AGENT = 'user_agent'
    MS = 'ms'

    def __init__(self, log_data):
        self.ip = log_data[Log.IP]
        self.datetime = log_data[Log.DATETIME]
        self.method = log_data[Log.METHOD]
        self.url = log_data[Log.URL]
        self.http_vers = log_data[Log.HTTP_VERS]
        self.http_status = int(log_data[Log.HTTP_STATUS])
        self.response_bytes = log_data[Log.RESPONSE_BYTES]
        self.source_url = log_data[Log.SOURCE_URL]
        self.user_agent = log_data[Log.USER_AGENT]
        self.ms = int(log_data[Log.MS])

    def __repr__(self):
        return f'{self.method} ' \
               f'{self.url}, ' \
               f'{self.http_status}, ' \
               f'{self.ms}ms, ' \
               f'{self.datetime}, ' \
               f'{self.ip} ' \

class LogParser:
    def __init__(self, path_to_log):
        self.logs = []

        log_template = re.compile(
            f'^(?P<{Log.IP}>\S*)' \
            '.*' \
            f'\[(?P<{Log.DATETIME}>.*)\]\s+' \
            f'\"(?P<{Log.METHOD}>\S*)\s+' \
            f'(?P<{Log.URL}>\S*)\s+' \
            f'(?P<{Log.HTTP_VERS}>\S*)\"\s+' \
            f'(?P<{Log.HTTP_STATUS}>\d*)\s+' \
            f'(?P<{Log.RESPONSE_BYTES}>\S*)\s+' \
            f'\"(?P<{Log.SOURCE_URL}>.*)\"\s+' \
            f'\"(?P<{Log.USER_AGENT}>.*)\"\s+' \
            f'(?P<{Log.MS}>\d*)$'
        )

        with open(path_to_log, 'r') as log_file:
            for log in log_file:
                try:
                    log_data = log_template.match(log).groupdict()
                except AttributeError:
                    print(f'Can not parse [{log}]')
                    continue

                self.logs.append(Log(log_data))

    def count_requests(self):
        return len(self.logs)

    def count_requests_by_http_method(self, method):
        return len([log for log in self.logs if log.method == method])

    def total_requests_by_http_methods(self):
        res = {}

        for log in self.logs:
            res[log.method] = res[log.method] + 1 if log.method in res else 1

        return res

    def top_ip(self, top=3):
        res = {}

        for log in self.logs:
            res[log.ip] = res[log.ip] + 1 if log.ip in res else 1

        return {ip: res[ip] for ip in sorted(res, key=res.get, reverse=True)[:top]}

    def top_long_requests(self, top=3):
        return sorted(self.logs, key=lambda l: l.ms, reverse=True)[:top]


class Report:
    def __init__(self, log_parser):
        self.log_parser = log_parser

    def save_to_json(self, name):
        out = {
            'total_requests': self.log_parser.count_requests(),
            'requests_by_methods': self.log_parser.total_requests_by_http_methods(),
            'top_ip': self.log_parser.top_ip(),
            'top_long_requests': []
        }

        for req in self.log_parser.top_long_requests():
            r = {
                'method': req.method,
                'url': req.url,
                'http_status': req.http_status,
                'ms': req.ms,
                'datetime': req.datetime,
                'ip': req.ip
            }
            out['top_long_requests'].append(r)

        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')
        report_name = f'{now}_{name}.json'

        with open(report_name, 'w') as report:
            json.dump(out, report, indent=4)

    def print(self):
        print(f'Количество запросов: {self.log_parser.count_requests()}')
        print('Количество запросов по методам:')

        methods = self.log_parser.total_requests_by_http_methods()

        for method in sorted(methods, key=methods.get, reverse=True):
            print(f'  {method}: {methods[method]}')

        print('Топ ip-адресов по количеству запросов:')

        for ip, count in self.log_parser.top_ip().items():
            print(f'  {ip}: {count}')

        print('Топ долгих запросов:')

        for req in self.log_parser.top_long_requests():
            print(f'  {req}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='log_parser.py')
    actions = parser.add_subparsers(dest='actions')

    file_parser = actions.add_parser('file')
    file_parser.add_argument('log_file')

    dir_parser = actions.add_parser('dir')
    dir_parser.add_argument('log_dir')

    args = parser.parse_args()

    if args.actions is None:
        parser.print_help()
        sys.exit(1)

    if 'log_file' in args:
        file = Path(args.log_file)

        if not file.exists():
            print(f'[{args.log_file}] is not exists')
            sys.exit(1)

        file = file.resolve()

        if not file.is_file():
            print(f'[{args.log_file}] is not a file')
            sys.exit(1)

        print(f'file: {file.name}')
        log_parser = LogParser(args.log_file)
        report = Report(log_parser)
        report.print()
        report.save_to_json(file.name)

    if 'log_dir' in args:
        directory = Path(args.log_dir)

        if not directory.exists():
            print(f'[{args.log_dir}] is not exists')
            sys.exit(1)

        directory = directory.resolve()

        if not directory.is_dir():
            print(f'[{args.log_dir}] is not a directory')
            sys.exit(1)

        for file in directory.iterdir():
            file = file.resolve()

            if not file.is_file():
                continue

            if file.name.endswith('.log'):
                print(f'file: {file.name}')
                log_parser = LogParser(str(file))
                report = Report(log_parser)
                report.print()
                report.save_to_json(file.name)
                print('-----------------')
