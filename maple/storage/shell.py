#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: shell.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-09 01:32:22 (CST)
# Last Update: Wednesday 2019-07-10 00:11:03 (CST)
#          By:
# Description:
# ********************************************************************************
from maple.shell import Shell as _Shell
import requests
import os


class Shell(_Shell):
    def __init__(self, host, token, bucket, path="/"):
        self.host = host
        self.token = token
        self.bucket = bucket
        self.path = path
        super(Shell, self).__init__()

    def _headers(self):
        return {
            'MapleToken': self.token,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        }

    def prompt(self):
        return "[{0}]-{1}: ".format(self.bucket, self.path)

    def do_pwd(self, args):
        self.echo(self.path)

    def do_ls(self, args):
        url = self.host + "/api/file/" + self.bucket
        r = requests.get(
            url,
            params={"path": self.path},
            headers=self._headers(),
        )
        if r.status_code != 200:
            return self.echo(r.json()["message"])
        data = r.json()["data"]
        for f in data["paths"]:
            print("{0}\t{1}\t{2}".format(
                f["name"],
                f["size"],
                f["updated_at"],
            ))

        for f in data["files"]:
            print("{0}\t{1}\t{2}".format(
                f["name"],
                f["size"],
                f["updated_at"],
            ))

    def do_cd(self, args):
        if args == "..":
            self.path = os.path.dirname(self.path)
            return
        self.path = os.path.join(self.path, args)

    def do_select(self, args):
        url = self.host + "/api/bucket"
        r = requests.get(
            url,
            params={"name": args},
            headers=self._headers(),
        )
        if r.status_code != 200:
            return self.echo(r.json()["message"])
        if len(r.json()["data"]) > 0:
            self.bucket = args
            self.echo("switch bucket to {0}: success".format(args))
        else:
            self.echo("switch bucket to {0}: {0} is not exists".format(args))

    def do_rm(self, args):
        pass

    def do_upload(self, args):
        self.echo(self.path)

    def do_refresh(self, args):
        self.echo(self.path)
