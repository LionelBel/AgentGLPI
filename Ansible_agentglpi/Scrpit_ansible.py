#!/usr/bin/python 
# -*- coding: utf-8 -*-

#0. Importation de la classe Ansible module :
from ansible.module_utils.basic import AnsibleModule

#1. Importation du module Python OS pour interagir avec DEBIAN :
import os

#2. Définition fonction install_dependencies :
def install_dependencies():
	os.system("apt install -y dmidecode hwdata ucf hdparm perl libuniversal-require-perl libwww-perl libparse-edid-perl libproc-daemon-perl libfile-which-perl libhttp-daemon-perl libxml-treepp-perl libyaml-perl libnet-cups-perl libnet-ip-perl libdigest-sha-perl libsocket-getaddrinfo-perl libtext-template-perl libxml-xpath-perl libyaml-tiny-perl")

#3. Définition fonction download_agentFI :
def download_agentFI():
	os.system("wget https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.5.2/fusioninventory-agent_2.5.2-1_all.deb")

#4. Définition fonction dpkg_agentFI :
def dpkg_agentFI():
	os.system("dpkg -i fusioninventory-agent_2.5.2-1_all.deb")

#5. Définition fonction config_agent
def config_agent(server_url, delay_time):

	# Modification du fichier agent.cfg en intégrant les paramètres du module : 
	file = open("/etc/fusioninventory/agent.cfg", "r")
	lignes = file.readlines()
	lignes[13] = "server = " + server_url + "\n"
	lignes[32] = "delaytime = " + str(delay_time) + "\n"
	file.close()
	file = open("/etc/fusioninventory/agent.cfg", "w")
	file.writelines(lignes)
	file.close()


#6. Definition fonction envoie information du systeme:
def send_info():

	# Redémarrage du service Fusioninventory_agent :
	os.system("systemctl restart fusioninventory-agent.service")

	# Envoi des informations système au serveur cible :
	os.system("pkill -USR1 -f -P 1 fusioninventory-agent")

#7. Définition du Module Ansible
def main():
	module_args = dict(
		server_url=dict(type='str', required=True)
		delay_time=dict(type='int', required=False, default=3600)
	)

	module = AnsibleModule(argument_spec=module_args)
	server_url = module.params['server_url']
	delay_time = module.params['delay_time']
	
	install_dependencies()
	download_agentFI()
	dpkg_agentFI()
	config_agent(server_url, delay_time)
	send_info()   
	reponse = {"result" : "Agent FusionInventoy installé ;)"}                   
	module.exit_json(changed=False, meta=reponse)

if __name__ == '__main__':
	main()