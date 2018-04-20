#!/usr/bin/env python
#coding:utf-8
import json
import re

text = 'fakookfa {{基礎情報 kojfoajfjkaofjoa}}'

matchOB = re.search(r'\{\{基礎情報(.*)\}\}', text)

if matchOB:
    print("DEBUG")
    print(matchOB.group(1))