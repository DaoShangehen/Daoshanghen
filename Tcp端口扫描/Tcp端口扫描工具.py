#encoding:utf-8
import socket;
import threading;
import optparse;
parser = optparse.OptionParser("Usage: python Script.py -H Host -P Port ");
parser.add_option("-H","--Host",dest="tarHost",type="string",help="Need a ip or hostname");
parser.add_option("-P","--Port",dest="tarPort",type="int",help="Need port array");
(options,args)=parser.parse_args();
Target_Host = options.tarHost;
Target_Port =  options.tarPort;
if(Target_Host == None or Target_Port == None):
	print "[!]Parameters must 2 argument ";
	exit(0);
args.append(Target_Port);
Print_LOCK = threading.Semaphore(value=1);
def ConScan(TarHost,TarPort):
	try:
		SOCK = socket.socket();
		SOCK.connect((TarHost,TarPort));
		SOCK.send("daosdkoaskdoas\r\n");
		Result = SOCK.recv(1024);
		Print_LOCK.acquire();
		print "[+]%d Tcp connect success !!!"%(TarPort);
		print "[+]Result :",Result;
	except Exception ,e:
		#print e;
		Print_LOCK.acquire();
		print "[-]%s Tcp connect close!!!"%(TarPort);
	finally:
		SOCK.close();
	Print_LOCK.release();

	return 0;

def PortScan(TarHost,TarPorts):
	
	try:
		TarHost = socket.gethostbyname(TarHost);
	except:
		print "[-] not exists host";
		return 0;
	try:
		infos = socket.gethostbyaddr(TarHost);
		print "[+]Scan result for :",infos[0];
	except:
		print "[+]Scan result for :",TarHost;
	socket.setdefaulttimeout(1);
	for CurPort in TarPorts:
		print "Current scan port is:",str(CurPort);
		#ConScan(TarHost,int( CurPort));
		threading.Thread(target=ConScan,args=(TarHost,int(CurPort),)).start();		


	return 0;

def main():
	PortScan(Target_Host,args);
	return 0;

#print str(args);
if __name__ == "__main__":
	main();
exit(0);


