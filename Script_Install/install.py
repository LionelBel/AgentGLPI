#!/usr/bin/python 
# -*- coding: utf-8 -*-

## Installation de l'agent Fusioninventory sur serveur Debian

#1. Installation des dépendances utilent à l'éxecution de FusionInventory agent
install_dependencies()

#2. Téléchargement de l'agent FusionInventory
download_agentFI()

#3. Installation de l'agent FusionInventory
dpkg_agentFI()

#4. Configuration de l'agent FusionInventory
config_agent()

#5. Envoi information système au serveur cible
send_info()