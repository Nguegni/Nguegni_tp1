# Traçabilité et limites de validation

Auteurs de cette note : NGUEGNI ONGOLO Antoine Depadoux et NKODA Xavier.

Les sources techniques sont les observations enregistrées dans le laboratoire commun CamTrust le 25 octobre 2026. La note du 26 octobre est une présentation distincte de ces sources, pas une nouvelle expérience indépendante.

- Les captures B1-B4, HTTPS et SSH sont inchangées.
- Les copies HTTP, FTP, Telnet et SNMP sont expurgées à longueur constante, avec sommes de contrôle recalculées ; la correspondance des SHA-256 figure dans tracabilite-captures.json.
- Les empreintes d’authentification des exports Cisco et VyOS sont retirées. Le journal d’administration et les configurations ne doivent pas être confondus avec un fichier d’identifiants.
- Les quatre images sont des captures de vues de synthèse issues de TShark, explicitement désignées dans la note. Les images sont converties en niveaux de gris uniquement lors de leur intégration au PDF.
- Les originaux sensibles restent conservés hors dépôt, avec leurs empreintes. Aucun test n’a été effectué sur un réseau tiers pour produire ces preuves.
- Les six tests A.7 ont réussi le 25 octobre. Ils n’ont pas tous été relancés après l’interruption de stockage ; aucun nouveau succès en fonctionnement n’est inventé.
- SFTP/FTPS et SNMPv3 ne sont pas déployés. Le sujet donne M3 pour SNMPv3 ; pour les trois autres services, la note cite C.1-C.3 faute de numéros de modules d’approfondissement disponibles.

Les fichiers SHA256SUMS.txt et controle-livraison.json documentent les vérifications de cette livraison. Une publication GitHub ne remplace pas la remise Classroom demandée par l’enseignant.
