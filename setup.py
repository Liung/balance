 #-*- coding: cp936 -*-
from distutils.core import setup

import py2exe

excludes = []
includes = ["sip","encodings", "encodings.*",]   
#要包含的其它库文件

options = {
	"py2exe":{
		"compressed": 1, #压缩
		"optimize": 2,
		"ascii": 1,
		"includes":includes,
		"excludes":excludes,
		#"bundle_files": 1 #所有文件打包成一个exe文件
    }
}
setup(    
    options = options, #{'py2exe':{'dll_excludes':['MSVCP90.dll']}},     
    zipfile=None,   #不生成library.zip文件
	windows=[{
		"script": "dataTransMain.py"
		
		}]
    #源文件，程序图标
    ) 
