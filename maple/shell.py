#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: shell.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-09 18:39:51 (CST)
# Last Update: Tuesday 2019-07-09 20:20:13 (CST)
#          By:
# Description:
# ********************************************************************************


class TablePrint(object):
    def __init__(self, data, header=None):
        self.data = data


class Shell(object):
    def __init__(self):
        self._exit = False
        self._action = [
            i.split("do_")[1] for i in dir(self) if i.startswith('do_')
        ]
        self._help = [
            i.split("help_")[1] for i in dir(self) if i.startswith('help_')
        ]

    def echo(self, message, color=None):
        print(message)

    def prompt(self):
        return ">> "

    def default(self, args):
        self.echo("*** Unknown syntax: " + args)

    def emptyline(self):
        pass

    def do_exit(self, args):
        "Exit shell"
        self._exit = True

    def do_help(self, args):
        "Show help"
        for action in self._action:
            hp = getattr(self, "do_" + action).__doc__
            if action in self._help:
                hp = getattr(self, "help_" + action)
            self.echo("{0}\t{1}".format(action, hp))

    def start(self):
        while self._exit == False:
            message = input(self.prompt())
            message = message.strip()
            if not message:
                self.emptyline()
                continue

            s = message.split(" ")
            keyword = s[0]
            if keyword == "?":
                keyword = "help"

            args = ""
            if len(s) > 1:
                args = " ".join(s[1:])

            if keyword in self._action:
                getattr(self, "do_" + keyword)(args)
            else:
                self.default(message)


if __name__ == '__main__':
    Shell().start()
