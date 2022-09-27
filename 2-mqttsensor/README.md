# test de connexion au serveur MQTT
établissement d'une connexion Wifi sur le point d'accès de la Raspberry et ensuite connexion au serveur MQTT, pour finir par envoyer une valeur aléatoire

L'usage des fichiers est :
- modifier ou vérifier la configuration Wifi "configMQTT.py"
- injecter l'adresse IP du serveur MQTT (celle de la passerelle du reseau Wifi) ainsi que le user/password autorisé sur le serveur mqtt 
- penser au upload du projet
- executer "testMQTT.py" après l'avoir ouvert
- vérifier l'arrivée des messages sur le serveur avec un client