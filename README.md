# JADEGUARD

![JadeGuardLogo](https://raw.githubusercontent.com/tamrinotte/jadeguard/main/app_images/JadeGuard.png)

<br>

JadeGuard is a firewall manager which, users' can use to enhance their cyber security.

<br>

## COMMANDS

__edit:__ Opens the regular firewall scripst in a file editor.

__show:__ Displays the firewall rules that have been set.

__set:__ Sets the firewall rules.

__delete:__ Delete all the firewall rules.

__restore:__ Restores the scripts.

__godmode:__ Opens the original firewall scripts in a file editor.

<br>

## OPTIONS

__--help:__ Shows the help message and exits.

<br>

## INSTALLATION

1) Install the dependencies
	
       sudo apt install nano netfilter-persistent iptables-persistent -y

2) Download the installer
	
       curl -L https://github.com/tamrinotte/jadeguard/releases/download/firewall/jadeguard.deb -o jadeguard.deb

3) Start the installer

       sudo dpkg -i jadeguard.deb

4) Open a new terminal and type

       sudo jadeguard set

<br>

---

<br>

![JadeGuardLogo](https://raw.githubusercontent.com/tamrinotte/jadeguard/main/app_images/JadeGuard.png)

<br>

JadeGuard kullancıların siber güvenliklerini arttırmalarını sağlayan bir güvenlik duvarı yöneticisidir.

<br>

## COMMANDS

__edit:__ Normal güvenlik duvarı kodlarını dosya editöründe açar.

__show:__ Ayarlanmış olan güvenlik duvarı kurallarını görüntüler.

__set:__ Güvenlik duvarı kurallarını uygular.

__delete:__ Var olan güvenlik kurallarını siler.

__restore:__ Normal kodları orjinal kodlara kurtarır.

__godmode:__ Orjinal güvenlik duvarı kodlarını dosya editöründe açar.

<br>

## OPTIONS

__--help:__ Yardım mesajını görüntüler.

<br>

## INSTALLATION

1) Bağımlılıkları yükle
	
       sudo apt install nano netfilter-persistent iptables-persistent -y

2) Yükleyici indir
	
       curl -L https://github.com/tamrinotte/jadeguard/releases/download/firewall/jadeguard.deb -o jadeguard.deb

3) Yükleyiciyi başlat

       sudo dpkg -i jadeguard.deb

4) Terminali aç ve uygulamayı başlat

       sudo jadeguard set
