#encoding:utf-8
import threading;
Semaphore = threading.Semaphore();
List = [];
def Test(p_i=0):
	
	for j in range(10):
		Semaphore.acquire();
		print str(p_i),"-",str(j);
		Semaphore.release();#如果这行被注释 那么只会输出 0-0 然后程序就卡主了

	None;
	

import time;
start = time.clock();
for i in range(10):
	WeiTuo =threading.Thread(target=Test,args=(i,));
	WeiTuo.start();
end = time.clock();
Test();
time.sleep(1);
Semaphore.acquire();
print str(List);
print str( (end - start) )+"S";
Semaphore.release();
