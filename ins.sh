#!data/data/com.termux/files/etc
#Tool By Noob Hackers 
#ThAnKS For Supporting 
################
cyn='\e[0;36m'

lgrn='\e[1;32m'

r='\e[1;31m'

y='\e[1;33m'
################
echo " "
echo " "
echo " "
echo " "
echo -e "\e[1m\e[33m\nWrite Your \e[31mFirst \e[33mName\e[32m 👇\n\n"
read varbanner
echo
echo -e "\e[1m\e[33m\nWrite Your \e[36mSecond \e[33mName\e[32m 👇\n\n "
read varcowsay
echo  "cowsay -f eyes "$varcowsay" | lolcat" > cowtext.txt
echo "toilet -f big '  $varbanner' -F gay | lolcat" > banner.txt
echo 
echo "clear" > null.txt
cat "null.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
cat "cowtext.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
cat "banner.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
cat "tload.txt"  >> /data/data/com.termux/files/usr/etc/bash.bashrc
echo " "
echo "                   "Ready to go buddy..... | lolcat
echo " "
