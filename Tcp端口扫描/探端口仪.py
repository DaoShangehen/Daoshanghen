#encoding:utf-8
import socket;
socket.setdefaulttimeout(0.1);
ip = raw_input();
exists_port = [];
for port in range(1,65535):
	try:
		socket.socket().connect((ip,port));
		print "[+]exists port:%d"%(port);
		exists_port.append(port);
	except Exception,e:
		print e;
		print "[-]not exists port:%d  ->ip %s"%(port,ip);
	None;

print "Exists port array:"+str(exists_port);
