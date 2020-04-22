#!/usr/local/bin/python evn
# coding=utf-8

import configure, log
import logging,os,re
from xml.dom import minidom
import traceback


logger = logging.getLogger(__name__)

class Compare:
    def __init__(self):
        self.difFileInfo = {}  
        self.filePath = ''
        self.fileKey = ''
        configure.outPath = configure.outPath + '\\' + configure.newPath.split('\\')[-1]
            
    '''调用bc获取差异list信息'''
    def getDifList(self): 
        path = self.createFile('temp.txt')
        scriptTxt = open(path, "w")
        strWrite = 'load ' + configure.oldPath + ' ' + configure.newPath
        strWrite += '\ncriteria attrib:sh timestamp:2sec;IgnoreDST CRC'
        strWrite += '\nexpand all'
        strWrite += '\nfolder-report layout:xml options:display-%s title:AutoCompare output-to:' % configure.displayType + configure.outPath + r"\report.xml"
        #strWrite = strWrite.decode('UTF-8').encode('gb2312')
        scriptTxt.write(strWrite)
        scriptTxt.close()
        self.callBC('temp.txt')
        
    '''转换文件编码'''
    def changeFileType(self, xml):
        file_xml = open(xml, 'r').read()
        file_xml = file_xml.replace('<?xml version="1.0" encoding="gb2312"?>', '<?xml version="1.0" encoding="UTF-8"?>')  
        file_xml = unicode(file_xml, encoding='gb2312').encode('UTF-8') 
        
        os.remove(xml)
        self.createFile('report.xml')
        scriptTxt = open(xml, "w")
        scriptTxt.write(file_xml)
        scriptTxt.close()
        
    '''解析差异文件信息'''
    def analyseFileInfo(self): 
        self.filePath = ''
        xmldoc = minidom.parse(configure.outPath + '\\' + 'report.xml')
        root = xmldoc.documentElement
        folder = root.getElementsByTagName('foldercomp')[0]
        if(folder):
            for node in folder.getElementsByTagName('filecomp'):
                fileInfo = {}
                changeType = '修改'
                fileName = ''
                lfileName = ''
                rfileName = ''
                if node.getAttribute('status') == 'rtonly':
                    rfileName = node.getElementsByTagName('name')[0].childNodes[0].nodeValue
                    changeType = '新增'
                elif node.getAttribute('status') == 'ltonly':
                    lfileName = node.getElementsByTagName('name')[0].childNodes[0].nodeValue
                    changeType = '删除'
                else:
                    lfileName = node.getElementsByTagName('name')[0].childNodes[0].nodeValue
                    rfileName = node.getElementsByTagName('name')[1].childNodes[0].nodeValue
                    
                if lfileName :
                    fileName = lfileName
                else:
                    fileName = rfileName
                
                                                                                                              
                fileInfo['fileName'] = fileName      
                fileInfo['changeType'] = changeType 
                                      
                self.analyseFilePth(node.parentNode)
                fileInfo['path'] = self.filePath + fileName
                
                self.fileKey = fileName.split('.')[0].lower()
                self.rename(self.fileKey)
                
                self.difFileInfo[self.fileKey] = fileInfo
                self.fileKey = ''
                self.filePath = ''
    
    '''给同名称的文件重新命名''' 
    def rename(self,fileKey):
        if fileKey not in self.difFileInfo.keys():pass
        else:
            self.fileKey += '1'
            self.rename(self.fileKey)
         
    '''解析出文件路径'''
    def analyseFilePth(self, node):             
        if node.parentNode.nodeName == 'bcreport' :pass     
        else:
            self.filePath = node.getElementsByTagName('name')[0].childNodes[0].nodeValue + '\\' + self.filePath
            node = node.parentNode 
            self.analyseFilePth(node) 
                                           
                           
    '''创建文件'''
    def createFile(self, fileName):
        path1 = r'%s\%s' % (configure.outPath, fileName)
        path = path1.replace("\\", "\\\\")
        log_path = os.path.dirname(path)
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        return path
            
    '''构建比对脚本,获取比对结果'''  
    def makeScript(self, displayType): 
        self.createFile('\\particular\\')
        path = self.createFile('comp.txt')
        scriptTxt = open(path, "w")
        
        for k, file in self.difFileInfo.items():
            baseName = os.path.basename(file['path']) 
            if baseName.split('.')[-1] not in configure.fileType :continue
            if displayType == 'all':
                strWrite = '\nfile-report layout:side-by-side options:display-all,line-numbers output-to:' + configure.outPath + '\\particular\\' + k + '.html'
            elif displayType == 'context':
                strWrite = '\nfile-report layout:side-by-side options:display-context,line-numbers output-to:' + configure.outPath + '\\' + k + '.html'
                
            strWrite += ' output-options:wrap-word,html-color '  
            if  file['changeType'] == '修改':
                strWrite += configure.oldPath + '\\' + file['path'] + ' '
                strWrite += configure.newPath + '\\' + file['path'] 
            elif file['changeType'] == '新增':
                strWrite += configure.newPath + '\\' + file['path'] 
            else:
                strWrite += configure.oldPath + '\\' + file['path'] 
            #strWrite = strWrite.encode('UTF-8')          
            scriptTxt.write(strWrite)     
            
        scriptTxt.close()
        self.callBC('comp.txt')
      
    '''调用bc比对控件'''
    def callBC(self, cmdfile):
        os.chdir(configure.bcPath)   
        os.system('BCompare.exe /silent @' + configure.outPath + '\\' + cmdfile)
        #os.system('BCompare.exe @' + configure.outPath + '\\' + cmdfile)
   
    '''比对'''  
    def doCompare(self):     
        #print u'获取差异文件列表\n'
        self.getDifList()
       
        #print u'修改文件类型以便支持xml解析\n'
        self.changeFileType(r'%s\report.xml' % configure.outPath)
       
        #print u'提取差异文件信息\n'
        self.analyseFileInfo()
        
        #print u'构建比对脚本并开始比对\n'
        self.makeScript('context')
        self.makeScript('all')
        #print u'比对结束\n'

'''
if __name__ == '__main__':   
  
    compareOb = Compare()  
    compareOb.doCompare()
'''




