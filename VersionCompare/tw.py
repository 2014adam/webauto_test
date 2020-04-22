#!/usr/local/bin/python evn
# coding=utf-8

#http://192.168.3.200:9400/tw/index.html

import configure,sys
import time,os
import compare,list
import traceback,copy
import logging,log
import UpDownLoad,zip
import sys

logger = logging.getLogger(__name__)

'''创建文件'''
def createFile(fileName):
    path1 = r'%s\%s' % (configure.outPath, fileName)
    path = path1.replace("\\", "\\\\")
    log_path = os.path.dirname(path)
    if not os.path.isdir(log_path):
        os.makedirs(log_path)
    return path

'''生成结果页面'''
def setResultPage( oldPath, newPath,difFileInfo):
    
    resultUrl = 'http://%s:9400/tw/%s/' % (configure.upIP, configure.outPath.split('\\')[-1])
        
    html = '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><style>a{color:#000000}.AlignLeft 
               { text-align: left; }.AlignCenter { text-align: center; }.AlignRight { text-align: right; }body 
               { font-family: sans-serif; font-size: 11pt; }td { vertical-align: top; padding-left: 4px; padding-right: 4px; }
               tr.SectionGap td { font-size: 4px; border-left: none; border-top: none; border-bottom: 1px solid Black; border-right:
               1px solid Black; }tr.SectionAll td { border-left: none; border-top: none; border-bottom: 1px solid Black; border-right:
               1px solid Black; }tr.SectionBegin td { border-left: none; border-top: none; border-right: 1px solid Black; }tr.SectionEnd 
               td { border-left: none; border-top: none; border-bottom: 1px solid Black; border-right: 1px solid Black; }tr.SectionMiddle
               td { border-left: none; border-top: none; border-right: 1px solid Black; }tr.SubsectionAll td { border-left: none; 
               border-top: none; border-bottom: 1px solid Gray; border-right: 1px solid Black; }
               tr.SubsectionEnd td { border-left: none; border-top: none; border-bottom: 1px solid Gray; border-right: 1px solid Black; }
               table.dc { border-top: 1px solid Black; border-left: 1px solid Black; width: 100%; font-family: sans-serif; font-size: 10pt; }
               table.dc tr.SectionBegin td { border-bottom: 1px solid Silver; }table.dc tr.SectionMiddle td { border-bottom: 1px solid Silver; }
               td.DirColHeader { color: #000000; background-color: #C7EDCC; background-color: #E7E7E7; padding-top: 8px; }
               td.DirDiff { color: #FF0000; }td.DirNewer { color: #FF0000; }td.DirOlder { color: #808080; }td.DirOrphan { color: #0000FF; }
               td.DirSame { color: #000000; }.DirInfo { color: 000000; }.DirInfoBlue { color: #0000FF; }.DirInfoLime { color: #2F4F4F; }.DirInfoRed { color: #FF0000; }.DirInfoGreen { color: #40c020; }.inp8{border:0px;width:100%}</style></head><body><h1 align=center>版本自动比对报告</h1>'''
    html += '<div>旧版本:%s</div><div>新版本:%s</div><di>比对日期:%s</div></br>' % (oldPath.split('\\')[-1], newPath.split('\\')[-1], time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                                                               
    html += '''<h3 align=left>比对结果</h3>
               <table class="dc" cellspacing="0" cellpadding="0"><tr class="SectionAll">
               <td class="DirColHeader">文件名称</td>
               <td class="DirColHeader">变更类型</td>
               <td class="DirColHeader">影响系统</td>
               <td class="DirColHeader">负责人</td>
               <td class="DirColHeader">变更详细</td></tr>'''
  
    
    for k,v  in difFileInfo.items():
        html += '<tr class="SectionMiddle"><td class="AlignLeft"><a class="DirInfo" target="compare" href="%s">%s</a></td>' %(resultUrl + 'particular/' + k.encode('utf-8') + '.html',k.encode('utf-8'))
        
        html += '<td  class="AlignLeft"><span class="DirInfo"> %s</span></td>' % v['changeType']
        html += '<td  class="AlignLeft"><span class="DirInfo"> /</span></td>'
        html += '<td  class="AlignLeft"><span class="DirInfo"> /</span></td>'
        html += '<td class="AlignLeft"><a class="DirInfo" target="compare" href="%s">详细</a></td></tr>' %(resultUrl + 'particular/' + k.encode('utf-8') +'.html')
    html += '</table></br>'
    html += '<h3 align=left>影响系统分析</h3>'
    html += '<a  class="AlignLeft">XX系统---</a><a href="">开启自动化测试</a></br>'
    html += '<a href="">......</a></br>'
    
    html += '<h3 align=left>配置自动检查</h3>'
    html += '<a href="">......</a></br>'
    
    html += '<h3 align=left>协议监控</h3>'
    html += '<a href="">......</a></br>'
    
    html += '</body></html>'
    path = createFile('compare.html')
    htmlPage = open(path, "w")
    #self.html = self.html.decode('UTF-8').encode('gb2312')
    #html = html.encode('gb2312')
    htmlPage.write(html)
    htmlPage.close() 
        

'''压缩上传并解压比对结果文件'''
def upFile():
    if not configure.isUpLoad:return
    list.makeList()
    UpDownLoad.upload(configure.indexpagePath + '\\' + 'list.html', '%s/list.html'%configure.upPatch)
    zip.zip_dir(configure.outPath, configure.outPath + '.zip')
    localpath = configure.outPath + '.zip'
    localpath = localpath.replace('\\','/')
    remotepath = '%s/%s'%(configure.upPatch,localpath.split('/')[-1])
    if configure.outPath.split('\\')[-1] + '\n' in UpDownLoad.ssh('ls ' + configure.upPatch):
        UpDownLoad.ssh('rm -rf  ' +   configure.upPatch + '/' + configure.outPath.split('\\')[-1])
    UpDownLoad.upload(localpath, remotepath)      
    UpDownLoad.ssh('unzip %s -d %s/%s/'%(remotepath,configure.upPatch,configure.outPath.split('\\')[-1]))
    UpDownLoad.ssh('rm -rf  ' + remotepath )

 
def main():
    
    log.configLog()     
    compareOb = compare.Compare()  
    compareOb.doCompare()
    difFileInfo = copy.deepcopy(compareOb.difFileInfo)  
    setResultPage( configure.oldPath, configure.newPath,difFileInfo)
    upFile()
      
if __name__ == '__main__':  
    main()
        

    