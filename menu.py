print("***************************************************************************")
print("     JUST FOR TRIAL MENU DRIVEN PROGRAM FOR LOCAL AND REMOTE EXECUTION")
print("***************************************************************************")
import getpass
import os
password=getpass.getpass()
if password=='s':
    print("where do you want to run the command in local/remote")
    print("press r for remote and l for local execution: ",end='')
    x=input()
    if x=='local' or x=="l":
        print('''                 TYPE: date for date
             	 TYPE: cal for calender 
             	 TYPE: mount for memory mounting 
             	 TYPE: ip for checking ip
             	 TYPE: ram for checking free ram
                 TYPE: httpd for httpd server configuration by using ansible
             	 TYPE: check ip or ping for pinging an ip
             	 TYPE: file or folder for making a file/folder 
             	 TYPE: add for adding a user
             	 TYPE: terminate for exit''')
        switcher=input("Press for input::")
        if 'date' in switcher:
                 os.system("date") 
        if 'cal' in switcher:
                 os.system("cal")
        if 'mount' in switcher or 'memory' in switcher:
                 l_name1=input("enter mounting folder:")
                 l_name2=input("enter target folder:")
                 os.system("mount {0} {1}".format(l_name1,l_name2)) 
        if 'ip' in switcher or 'ifconfig' in switcher:
                 os.system("ifconfig enp0s3")  
        if 'ram' in switcher:
                 os.system("free -m")  
        if 'httpd' in switcher:
                 os.system("yum install -q httpd -y")
                 test=input("if you have a html file for server press 0:")
                 if test=='0':
                      file_path=input("enter file path:")
                      os.system("cp {} /var/www/html".format(file_path))
                 os.system("systemctl start httpd")
                 os.system("systemctl stop firewalld")  
        if 'pinging' in switcher or 'ping' in switcher or 'check ip' in switcher:
                 ip=input("enter ip: ")
                 os.system("ping -w 4 {}".format(ip))  
        if 'making a file' in switcher or 'file' in switcher or 'folder' in switcher:
                 typo=input("what do you want to make 'file' or 'folder'")
                 if typo=='folder':
                     name=input("enter folder path+name:")
                     os.system("mkdir -v -p {} ".format(name))
                 if typo=='file':
                     name=input("enter file path+name:")
                     os.system("touch {} ".format(name))  
        if 'add' in switcher or 'add user' in switcher or 'useradd' in switcher or 'adding user' in switcher:
                 u_name=input("enter user name:")
                 os.system("useradd {}".format(u_name))  
        if switcher=='10' or 'exit' in switcher:
                 exit()              
    elif x=='remote' or x=='r':
         checking_ip=input("Enter the ip for remote system: ")
         checker=os.system("ping -q -w 3 {}".format(checking_ip))
         if checker==0:
            user_check=input("enter user name: ")  
            print('''                 TYPE: date for date
             	 TYPE: cal for calender 
             	 TYPE: mount for memory mounting 
             	 TYPE: ip for checking ip
             	 TYPE: ram for checking free ram
                 TYPE: httpd for httpd server configuration by using ansible
             	 TYPE: check ip or ping for pinging an ip
             	 TYPE: file or folder for making a file/folder 
             	 TYPE: add for adding a user
             	 TYPE: terminate for exit''')
            switche=input("Press for input::  ")
            if 'date' in switche:
                 os.system("ssh {0} -l {1} date".format(checking_ip,user_check)) 
            if 'calender' in switche or 'calendar' in switche or 'calender' in switche:
                 os.system("ssh {0} -l {1} cal".format(checking_ip,user_check)) 
            if 'mount' in switche or 'mounting' in switche:
                 name1=input("enter mounting folder:")
                 name2=input("enter target folder:")
                 os.system("ssh {0} -l {1} mount {2} {3} ".format(checking_ip,user_check,name1,name2)) 
            if 'ip' in switche or 'ifconfig' in switche:
                 os.system("ssh {0} -l {1} ifconfig enp0s3".format(checking_ip,user_check))  
            if 'ram' in switche:
                 os.system("ssh {0} -l {1} free -m".format(checking_ip,user_check)) 
            if 'httpd' in switche:
                 os.system("ansible-playbook sarthak.yml")   
            if 'pinging' in switche or 'ping' in switche or 'check ip' in switche:
                 r_ip=input("enter ip:  ")
                 os.system("ssh {0} -l {1} ping -w 4 {2}".format(checking_ip,user_check,r_ip)) 
            if 'making a file' in switche or 'file' in switche or 'folder' in switche:
                  typor=input()
                  if typor=='folder':
                     namer=input("enter folder path+name: ")
                     os.system("ssh {0} -l {1} mkdir -v -p {2}".format(checking_ip,user_check,namer))  
                  if typor=='file':
                     namer=input("enter file path+name: ")
                     os.system("ssh {0} -l {1} touch {2}".format(checking_ip,user_check,namer))  
            if 'add' in switche or 'add user' in switcher or 'useradd' in switche or 'adding user' in switche:
                 r_name=input("enter user name for adding : ")
                 os.system("ssh {0} -l {1} useradd {2}".format(checking_ip,user_check,r_name))  
            if switche=='1' or switche=='exit' or switche=="terminate":
                 exit()    
else:
     print("you can not accesss")
     exit()
r=input("press any key for exit")
