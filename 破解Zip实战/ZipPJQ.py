#encoding:utf-8
import zipfile;
def CheckPwd(ZipObj,Pwd):
	try:
		ZipObj.extractall(pwd=Pwd);#尝试解压 如果解压没有抛异常那么就证明密码正确
		return Pwd;
	except:
		return None;

def Main():
	ZipName= raw_input("Input zip file name:");
	ZipObj = zipfile.ZipFile(ZipName);
	DicFN = raw_input("Input Dictionary file name :"); # request user input dictionary file name
	PwdLines = open(DicFN,"r").readlines();
	Pwd_exists_dic = False;
	for tmp_pwd in PwdLines:
		RetResult= CheckPwd(ZipObj,tmp_pwd.strip("\n"));
		if(RetResult):
			print "[+]Password is :%s"%(RetResult);
			Pwd_exists_dic = True;
			break;
		else:
			print "[-]Password not is :%s"%(tmp_pwd.strip("\n"));
		
		None;
	None;
	if( not Pwd_exists_dic):
		print "Password not in dictionary";
	else:
		print "Password exists dictuonary";

if __name__ == "__main__":
	Main();
