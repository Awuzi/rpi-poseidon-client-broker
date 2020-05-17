# **POSEIDON - RASPBERRY PI - SAUVEGARDE A DISTANCE**
 
Script et base de donn?es permettant la sauvegarde des donn?es du RPI via MQTT

# **Utilisation**
 
T?l?chargez le repository sur la machine qui vous servira de base de donn?es distante. 
Executez le script mqttsub.py : 
```
$ > sudo python3 mqttsub.py
```
Ce script ?coute les donn?es arrivant du broker via MQTT, et les sauvegarde dans la base de donn?es sqlite3 Poseidon.db.

Pour acc?der ? l'interface de gestion, ex?cutez le script interfaceInfo.py : 
```
$ > sudo python3 interfaceInfo.py
```
Le terminal indiquera alors une adresse IP : celle servant ? acc?der ? l'interface de gestion.
