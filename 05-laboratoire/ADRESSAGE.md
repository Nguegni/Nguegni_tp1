# Implantation du laboratoire

| Équipement | Interface | Adresse |
|---|---|---|
| R-SIEGE | Gi0/0 | 10.10.10.1/24 |
| R-SIEGE | Gi0/1 | 198.51.100.2/30 |
| R-SIEGE | Gi0/2 | 172.16.12.1/30 |
| R-DLA | ether1 | 172.16.12.2/30 |
| R-DLA | ether2 | 10.20.10.1/24 |
| R-FAI | eth0 | 198.51.100.1/30 |
| R-FAI | eth1 | 203.0.113.1/24 |
| SRV-INTERNET | ens3 | 203.0.113.10/24 ; GW 203.0.113.1 |

DHCP siège : 10.10.10.100-254, GW 10.10.10.1, DNS 203.0.113.10. DHCP Douala : 10.20.10.100-200, GW 10.20.10.1, même DNS.

Le switch relie les deux clients du siège et Gi0/0 de R-SIEGE. Gi0/2 joint R-DLA ; Gi0/1 joint R-FAI. R-FAI joint SRV-INTERNET. R-DLA dessert PC-DLA. Tous les ports du siège restent en VLAN 1 pour la situation initiale du sujet.

Le fichier CamTrust-TP.unl décrit les huit équipements et leurs liens. Il ne transporte pas les images ni les disques configurés. Leur disponibilité et leurs droits d’utilisation doivent être vérifiés dans l’EVE-NG de destination. Les configurations jointes sont expurgées et nécessitent la définition de nouveaux secrets avant restauration.

Le réseau Internet du TP est simulé avec les plages de documentation. Le poste graphique réel est séparé de ce périmètre.
