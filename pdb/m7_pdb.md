import pdb 

需要断点的地方加入下句，常规运行脚本，到断点就会进入debug状态<br/>
pdb.set_trace()

debug状态下：<br/>
n: 执行下一句<br/>
s: 进入函数<br/>
c: 前进到下一个断点<br/>
p xxx: 打印变量xxx的值<br/>
q: 退出脚本<br/>
l: 打印附近代码<br/>
!xxx = sth: 给xxx变量赋值sth<br/>
