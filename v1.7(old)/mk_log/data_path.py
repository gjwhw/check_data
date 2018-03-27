# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 文件路径定义
def path(x,day,province):

    error = '/hadoopdata/share/'+ province + '/datacheck/v1.6/error/'+ day +'/'
    log   = '/hadoopdata/share/'+ province + '/datacheck/v1.6/log/'+ day +'/'
    type1 = x
    return error,log,type1
