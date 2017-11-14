#encoding:utf-8
import optparse;
parser= optparse.OptionParser("Script -f <ZipFile> -d <dictionaryfile>");
parser.add_option("-f","--file",dest="ZipFile",type="string",help="Zip file name");
parser.add_option("-d","--dictionary",dest="DicFile",help="dictionary file name");
(options,args) = parser.parse_args();
"""
print options.ZipFile;
print options.DicFile;
print  "其余无用Args"+str(args);
print options;"""

def CheckPassword(ZipObj,Password):
	try:
		ZipObj.extractall(pwd=Password);
		print "\033[1;33;40m"
		print "Password :",(Password);
		return;
		#return Password;
	except Exception,e:
		#print e,"===",Password;
		#print "[-] Password mismatching ! ->%s"%(Password);
		#return None;
		None;
	None;

def Main():
	import zipfile;
	import threading;
	import thread;
	zipobj = zipfile.ZipFile(  options.ZipFile);
	diclines = open(options.DicFile,"r").readlines();
	print "\033[1;31;40m"
	a=0;
	for CurrentLine in diclines:
		"""注释这些是没有用多线程的 也要将上面的取消注释 return 那个
		Password= CheckPassword(zipobj,CurrentLine.strip("\n"));
		if(Password):
			print "[*]Password matching! ";
			print "\033[1;33;40m"
			print "[!]Password is :%s"%(Password);
			break;
		else:
			print "[-]%d Password mismatching !"%(a);
		a+=1;"""
		pwd=CurrentLine.strip("\n");
		t=threading.Thread(target=CheckPassword,args=(zipobj,pwd));
		t.start();


	None;

if __name__ == "__main__":
	Main();



