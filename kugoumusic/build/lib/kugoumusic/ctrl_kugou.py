#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Zqf'


import requests


def start_project_kugou(project, spider):
    url = target_domain + 'schedule.json'
    
    data = {
        project: project,
        spider: spider
    }
    response = requests.post(url, data)
    print(response.text)
    
    
if __name__ == '__main__':
    target_domain = 'http://127.0.0.1:6800/'
    project = 'kugouproject'
    spider = 'kugou'
    start_project_kugou(project, spider)