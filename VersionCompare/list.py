#!/usr/local/bin/python evn
# coding=utf-8

import fileinput,os
import configure
import linecache

listMode = '''
<html >
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>比对历史记录</title>
<style type="text/css">
.blockcont4 {
height:277px;
border: 0px #becbcb solid;}
.olleft {
margin:6px 16px 6px 38px;
list-style-type:circle;
width:auto;}
.olleft li {
height:22px;
line-height:22px;
white-space:nowrap;
overflow:hidden;}
.olleft li a:link {
display: block;
height:22px;}
.olleft li a:hover {
background-color: red;}
</style>
</head>
<body>
<div class="blockcont4">
<ol class="olleft">
</ol>
</div>
</body>
</html>
'''

frame = '''
<html>
<frameset cols="25%,75%">
<frame src="list.html">
<frame name="compare" src="">
</frameset>
</html>
'''
    
def file_insert(fname,linenos=[],strings=[]):   
        if os.path.exists(fname):   
            lineno = 0  
            i = 0  
            for line in fileinput.input(fname,inplace=1):   
                lineno += 1  
                line = line.strip()   
                if i<len(linenos) and linenos[i]==lineno:   
                    if i>=len(strings):   
                        print "\n",line   
                    else:   
                        print strings[i]   
                        print line   
                    i += 1  
                else:   
                    print line    
         
def makeList():
    if not os.path.exists(configure.indexpagePath):
        os.makedirs(configure.indexpagePath)
        
    if not os.path.isfile(configure.indexpagePath + r'\list.html'):
         listPage = open(configure.indexpagePath + r'\list.html', "w")
         #self.html = self.html.decode('UTF-8').encode('gb2312')
         listPage.write(listMode)
         listPage.close() 
         
    if not os.path.isfile(configure.indexpagePath + r'\index.html'):
         listPage = open(configure.indexpagePath + r'\index.html', "w")
         #self.html = self.html.decode('UTF-8').encode('gb2312')
         listPage.write(frame)
         listPage.close()
    
    count = linecache.getline(configure.indexpagePath + r'\list.html',28)
    if configure.newPath.split('\\')[-1] not in count:
        a = '<li><span><a href="http://%s:9400/tw/%s/compare.html" target="compare">%s版本</a></span></li>'%(configure.upIP,configure.newPath.split('\\')[-1],configure.newPath.split('\\')[-1])
        file_insert(configure.indexpagePath + r'\list.html',[28],[a]) 
  
if __name__ == '__main__':
    makeList()

   


   


    
    
    
    
    
    
    
    
    
    