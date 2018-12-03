#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Zqf'


import requests


# def add_version(project, version=None):
#     url = target_domain + 'addversion.json'
#     data = {
#         'project': project,
#         'version': version,
#         'egg': egg
#     }
#     response = requests.post(url, data=data)
#     print(response.text)


def schedule(project, spider):
    url = target_domain + 'schedule.json'
    data = {
        'project': project,
        'spider': spider
    }
    response = requests.post(url, data=data)
    print(response.text)


def cancer(project, jobid):
    url = target_domain + 'cancel.json'
    data = {
        'project': project,
        'job': jobid
    }
    response = requests.post(url, data=data)
    print(response.text)
    

def list_project():
    url = target_domain + 'listprojects.json'
    response = requests.get(url)
    print(response.text)


def list_versions(project):
    url = target_domain + 'listversions.json'
    params = {
        'project': project
    }
    response = requests.get(url, params=params)
    print(response.text)
    
    
def list_spiders(project):
    url = target_domain + 'listspiders.json'
    params = {
        'project': project
    }
    response = requests.get(url, params=params)
    print(response.text)
    
    
def list_jobs(project):
    url = target_domain + 'listjobs.json'
    params = {
        'project': project
    }
    response = requests.get(url, params=params)
    print(response.text)
    
    
def del_version(project):
    url = target_domain + 'delversion.json'
    params = {
        'project': project
    }
    data = {
        'version': 1536837235
    }
    response = requests.post(url, params=params, data=data)
    print(response.text)


def del_project(project):
    url = target_domain + 'delproject.json'
    data = {
        'project': project
    }
    response = requests.post(url, data=data)
    print(response.text)

    
if __name__ == '__main__':
    target_domain = 'http://127.0.0.1:6800/'
    project = 'kugouproject'
    spider = 'kugou'
    egg = 'kugoumusic'
    # 开启项目
    # schedule(project, spider)
    # 关闭项目
    jobid = 'a263e9c8b74611e8a058005056c00008'
    # cancer(project, jobid)
    # 查看项目列表
    # list_project()
    # 版本列表
    # list_versions(project)
    # 爬虫名称
    # list_spiders(project)
    # 工作状态
    # list_jobs(project)
    # 删除指定版本号的爬虫
    # del_version(project)
    # 删除项目
    # del_project(project)
    # add_version(project, version=None)