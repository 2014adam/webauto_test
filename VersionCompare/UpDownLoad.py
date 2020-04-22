#!/usr/local/bin/python evn
# coding=utf-8

import paramiko
import threading
import zip,configure

def ssh(cmd):
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(configure.upIP,configure.upPort,configure.upUsername, configure.upPassword)
   stdin, stdout, stderr = ssh.exec_command(cmd)
   result = stdout.readlines()
   ssh.close()
   return result

def upload(localpath,remotepath):
    t = paramiko.Transport((configure.upIP,configure.upPort))
    t.connect(username = configure.upUsername, password = configure.upPassword)
    sftp = paramiko.SFTPClient.from_transport(t)
    #remotepath='/home/test123.txt'
    #localpath='E:/test123.txt'
    print sftp.put(localpath,remotepath)
    t.close()

def download(remotepath,localpath):
    t = paramiko.Transport((configure.upIP,configure.upPort))
    t.connect(username = configure.upUsername, password = configure.upPassword)
    sftp = paramiko.SFTPClient.from_transport(t)
    #remotepath='/data/Python-2.7.2.tar.bz2'
    #localpath='E:/Python-2.7.2.tar.bz2'
    sftp.get(remotepath, localpath)
    t.close()


#if __name__=='__main__':
#    upload(r'F:\compare\index.html',r'/home/ceshi/tw/index.html')
    
'''
if __name__=='__main__':
    
    print type([1,2])
    a = ssh('rm -rf   /usr/local/apache2/htdocs/VerComRult/testdir')
    print a

    if 'testdir\n' in a :
        print 'ok'
    
  
    ssh('unzip /usr/local/apache2/htdocs/VerComRult/V2.1.0patch20121224.zip  -d /usr/local/apache2/htdocs/VerComRult/V2.1.0patch20121224/')

    cmd = ['sz /home/curl-7.18.1']#你要执行的命令列表
    username = "root"  #用户名
    passwd = "niunian#2009"    #密码
    print "Begin......"
    ip = '10.6.221.69'
    a=threading.Thread(target=ssh,args=(ip,username,passwd,cmd)) 
    a.start() 
    

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ssh.connect('192.168.3.200',22,'ceshi1','ceshi1')
#stdin, stdout, stderr = ssh.exec_command('svn checkout http://tc-scm.tencent.com/ied/ied_angel_rep/angel_doc_proj/trunk/CommonConfig/TimeReports /data/img/res/bak/TimeReports')
stdin, stdout, stderr = ssh.exec_command('mkdir /home/ceshi/tw/test')
result = stdout.readlines()
ssh.close()
print result
'''



