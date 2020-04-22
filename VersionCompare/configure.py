#!/usr/local/bin/python evn
# coding=utf-8
'''
   系统的配置部分，一般配置请修改本文件，勿要直接修改主程序代码
'''
import os, logging.handlers

'''功能控制开关'''
isConnectDb = True     #DB开关
isMail = False          #邮件开关
isUpLoad = True        #文件上传开关

'''数据库配置'''
CompareDB = {'host':"10.6.221.69", 'db':"AutoCompare", 'user':"QXautoTest", 'passwd':"123456", "charset":"utf8"}

'''邮件配置'''
mailServer = 'tsmtp.tencent.com' #'smtp.qq.com'
mailFrom = 'QxAuto_guest@tencent.com'
mailTo =['insistwu@tencent.com', 'tinxu@tencent.com','bonnieli@tencent.com','kernzhou@tencent.com']
mailUser = 'QxAuto_guest'
mailPassword = 'qxzb4autoTest'

'''bc安装配置'''
bcPath = r'C:\Program Files\Beyond Compare 3' 

'''比较的文件类型'''
#生成比对页面的文件类型
fileType = ['ini', 'conf', 'xml', 'sql','java', 'c', 'cpp', 'h', 'txt', 'html', 'py','jsp','php','properties','sh','proto']
#flash资源文件类型
clientFileType = ['swf']      
#图片文件类型
picFileType = ['jpg','gif','png']    
#配置文件类型                                              
configFileType = ['ini', 'conf', 'xml', 'sql','properties','sh']       
#后台server文件类型                                             
serverFileType = ['java', 'c', 'cpp', 'h',  'txt', 'html', 'py','jsp','php']       
#其他特殊文件类型
otherFileType =  ['youxigu', 'jar', 'db','class']                                                 

'''比对结果展示显示配置'''
displayType = 'mismatches' #mismatches只显示差异，all全部显示  context显示差异部分上下文 

'''文件上传配置'''
upIP = '192.168.3.200'
upPort = 22
upUsername = 'ceshi1'
upPassword = 'ceshi1'
upPatch = '/home/ceshi/tw'  #文件上传路径

'''比对路径设置'''
oldPath = r'F:\twVersion\tw20160602'
newPath = r'F:\twVersion\tw20160612'
outPath = r'F:\compareResult'

'''比对结果展示结构配置'''
indexpagePath = r'F:\compareResult\indexpage'




