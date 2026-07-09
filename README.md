# Web-AppArmor-Manager


Conception, Développement et déploiement d’un gestionnaire web sécurisé pour l’administration et l’audit des profils AppArmor avec détection et mitigation des comportements malveillants

# Fonctinnalités

# 1. Partie technique AppArmor
création de profils 
modes :complain, enforce 
restriction d’accès fichiers/processus

# 2. Partie ATTACK
Exemple concret :
application vulnérable 
tentative :
accès /etc/shadow 
exécution /bin/bash 
reverse shell 

# 3. Partie DEFENSE
Avec AppArmor :
limiter accès fichiers 
bloquer exécution 
sandbox application 

# 4. Analyse
logs AppArmor, comparaison avant/après, impact sécurité 

# 5. Partie Web 
Le web doit servir à : visualiser profils, activer/désactiver, voir les logs
