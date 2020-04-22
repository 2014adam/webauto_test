#!/usr/local/bin/python evn
# coding=utf-8

import os,os.path
import zipfile

def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
        
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()

def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.makedirs(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')  
        if name.endswith('/'):
            if not os.path.exists(os.path.join(unziptodir, name)):os.makedirs(os.path.join(unziptodir, name))
        else:            
            ext_filename = os.path.join(unziptodir, name)
            ext_filename = ext_filename.replace('\\','/')  
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.makedirs(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
       
'''
if __name__ == '__main__':
    
    #os.makedirs(r'F:\compare\wap20130702\jarPag\META-INF/')
    #os.makedirs('F:/compare/V2.5.0/javaDecompiler/dynastyBackup',0777)
    #zip_dir(r'E:/V2.1.0patch20121224',r'E:/V2.1.0patch20121224.zip')
    #unzip_file('F:\compare\V2.5.0patch20130514\dynasty\WEB-INF\lib\dynastyBackup.jar','F:\compare\V2.5.0patch20130514\jarPage')
    unzip_file(r'F:\test\dynasty_patch_20140212_on_v3.3.0.zip',r'F:\test\v3.3.0patch20140212')
    #os.remove(r'F:\compare\config\data.youxigu')  
    #path = 'F:\compare'
    #os.system('rd /s /q ' + path + '\\' + 'test')  

'''