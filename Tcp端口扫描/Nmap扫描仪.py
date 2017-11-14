#encoding:utf-8
import optparse;
import nmap;
import socket;
import threading;
Semaphorer = threading.Semaphore();
def PortScan(TarHost,TarPort):
	Scanner = nmap.PortScanner();
	try:
		TarHost = socket.gethostbyname(TarHost);
	except Exception,e:
		None;
	result = Scanner.scan(TarHost,TarPort);
	state = result["scan"][TarHost]["tcp"][int(TarPort)]["state"];
	Semaphorer.acquire();
	print "[+] %s tcp/ %s state:%s"%(TarHost,TarPort,state);
	Semaphorer.release();
	None;

def main():
	parser = optparse.OptionParser("Usage: python ScriptName.py -H <IP> -P <Port...>");
	parser.add_option("-H","--Host",dest="Host",type="string",help=" Host for this argument ");
	parser.add_option("-P","--Port",dest="Port",type="string",help=" Port for this argument ");
	(options,args) = parser.parse_args();
	if(options.Host == None or options.Port == None):
		print "[!]Need arguments is 2";
		exit(0);
	args.append(options.Port);
	for CurPort in args:
		#PortScan(options.Host,CurPort);#这部分表示使用单线程
		#下面的表示使用多线程
		threading.Thread(target=PortScan,args=(options.Host,CurPort)).start();

if __name__ == "__main__":
	main();
	

