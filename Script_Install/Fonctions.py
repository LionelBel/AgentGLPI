# Définition des Fonctions utilisées par install.py

#1. Importation du module Python OS pour interagir avec DEBIAN
import os

#2. Définition de la fonction install_dependencies :
def install_dependencies():
	os.system("apt install -y dmidecode hwdata ucf hdparm perl libuniversal-require-perl libwww-perl libparse-edid-perl libproc-daemon-perl libfile-which-perl libhttp-daemon-perl libxml-treepp-perl libyaml-perl libnet-cups-perl libnet-ip-perl libdigest-sha-perl libsocket-getaddrinfo-perl libtext-template-perl libxml-xpath-perl libyaml-tiny-perl")

#3. Définition de la fonction download_agentFI :
def download_agentFI():
	os.system("wget https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.5.2/fusioninventory-agent_2.5.2-1_all.deb")

#4. Définition de la fonction dpkg_agentFI :
def dpkg_agentFI():
	os.system("dpkg -i fusioninventory-agent_2.5.2-1_all.deb")

#5. Définition de la fonction config_agent :
def config_agent():
	file = open("/etc/fusioninventory/agent.cfg" , "r")
	lignes = file.readlines()
	lignes[13]= "server = http://10.0.1.188/glpi/plugins/fusioninventory/\n"
	file.close()
	file = open("/etc/fusioninventory/agent.cfg", "w")
	file.writelines(lignes)
	file.close()

#6 Définition de la fonction send_Info :
def send_info():
	# Redémarrage du service Fusioninventory-agent :
	os.sytem( "systemctl restart fusioninventory-agent.service")

	# Envoi des informations système au serveur cible : 
	os.system("pkill -USR1 -f -P 1 fusioninventory-agent")
