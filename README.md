# AgentGLPI
Script Python d'installation de l'agent fusioninventory et script pour module Ansible sur Debian 10.

## Objectif
L'objectif est d'installer l'agent FusionInventory, sur différents serveurs de notre infrastructure via un module Ansible ou par un script Python.

### Description
Le module "agentglpi" installera les différents packages nécessaires à l'installation et enverra les informations système des différents sur le
serveur de contrôle.
Dans le répertoire Scrypt_Install se trouve le script d'installation de l'agent fusioninventory.
Dans le répertoire Ansible_agentglpi se trouve le script pour le module Ansible. 