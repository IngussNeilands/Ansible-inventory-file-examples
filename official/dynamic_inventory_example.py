#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint


pp = pprint.PrettyPrinter(indent=4)
pp.pprint({
    "databases": {
        "hosts": ["host1.example.com", "host2.example.com"],
        "vars": {
            "a": True
        }
    },
    "webservers": ["host2.example.com", "host3.example.com"],
    "atlanta": {
        "hosts": ["host1.example.com", "host4.example.com", "host5.example.com"],
        "vars": {
            "b": False
        },
        "children": ["marietta", "5points"]
    },
    "marietta": ["host6.example.com"],
    "5points": ["host7.example.com"]
})