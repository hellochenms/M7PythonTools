使用python自带的web服务器

cd my_web_dir<br/>
python -m SimpleHTTPServer 8080

资源放在my_web_dir下，比如m2_72@2x.png；<br/>
GET请求http://localhost:8080/m2_72@2x.png就可以了；

当然更常用的是返回json，json直接写到test.txt，<br/>
http://localhost:8080/test.txt就OK了


如果需要执行脚本<br/>
python -m CGIHTTPServer 8686<br/>
脚本文件放在my_web_dir目录的cgi-bin目录下，<br/>
并且chmod +x test.py使脚本有执行权限<br/>
脚本内容如下，注意header结束时的换行<br/>
#!/usr/bin/python<br/>
print "Content-Type: text/json\n"<br/>
print '{"a":"aa", "b":["bb", "bbb", "bbbb"]}'<br/>
http://localhost:8686/cgi-bin/test.py就OK了