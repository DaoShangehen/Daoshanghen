#encoding:utf-8
import socket;
IPs=[];
socket.setdefaulttimeout(0.1);
port = input("input port number:");

for ipw in range(1,255):
	try:
		ip="192.168.0."+str(ipw);
		print "[+] Check form ip:"+ip;
		socket.socket().connect((ip,port));
		IPs.append(ip);
	except:
		None;
		
print  str(IPs);
print "\033[1;31;40m"+("没有人开启端口" if len(IPs)==0 else "有人开启端口" ) ;

