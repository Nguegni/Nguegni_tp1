# CamTrust Bank | Note d’audit TCP/IP

**NGUEGNI ONGOLO Antoine Depadoux · NKODA Xavier**

> « Ce qui circule en clair » : une note de décision et les preuves techniques du TP0.1.

## Le document à lire

[**Ouvrir la note d’audit - PDF autonome de cinq pages**](01-note-audit/Fiche-CamTrust-NGUEGNI-NKODA.pdf)

La note suit le plan imposé : résumé pour la direction en cinq lignes, périmètre et autorisation, tableau C.5 illustré, plan d’action et annexes des trois routeurs. La présentation adopte une typographie classique, des tableaux à filets horizontaux et une composition monochrome.

Les PCAPNG, les exports et les journaux sont également embarqués en pièces jointes du PDF. Un lecteur prenant en charge les pièces jointes permet de les extraire.

## Parcours de lecture

| Repère | Utilité |
|---|---|
| [01 - Note d’audit](01-note-audit/) | Rapport final et version textuelle |
| [02 - Traces réseau](02-traces-reseau/) | Fondamentaux ARP/DHCP/DNS/TCP et comparaisons des services |
| [03 - Éléments de preuve](03-elements-de-preuve/) | Six journaux A.7, lectures de protocoles, après-correction et illustrations |
| [04 - Configurations](04-configurations/) | R-SIEGE, R-DLA et R-FAI, avec secrets expurgés |
| [05 - Laboratoire](05-laboratoire/) | Topologie EVE-NG et plan d’adressage |
| [06 - Contrôles](06-controles/) | Traçabilité, validation et correspondance avec la grille de notation |
| [Outils](outils/) | Reconstruction du PDF et vérification locale de l’intégrité |

## Ce que les preuves établissent

Les essais du **25 octobre 2026** ont validé les **six contrôles A.7**. Les captures montrent les échanges ARP, DHCP, DNS et TCP, les différences HTTP/HTTPS et Telnet/SSH, ainsi que les informations exposées par FTP et SNMPv2c. La migration vers SSH a été testée, Telnet a ensuite été refusé et la communauté SNMP de test a été retirée.

**SFTP/FTPS et SNMPv3 sont des corrections proposées, pas des migrations réalisées.** La vérification complète A.7 n’a pas été relancée après l’interruption de stockage. Le document distingue les résultats historiques des limites de validation.

Cette version reprend les preuves du **laboratoire commun CamTrust**. Les différences de présentation et d’organisation ne signifient pas que les mêmes essais ont été exécutés indépendamment une seconde fois. La navigation Google sur le poste graphique séparé ne constitue pas une preuve de ce TP et n’est pas incluse dans les captures.

## Utiliser les fichiers de capture

Ouvrir les PCAPNG dans Wireshark. Les [filtres et points de capture](02-traces-reseau/LECTURE.md) permettent de retrouver les observations de la fiche. Les captures B sont inchangées. HTTP Basic, FTP, Telnet et SNMP sont fournis sous forme de copies expurgées ; les originaux sont conservés localement, hors dépôt. Les [empreintes et transformations](06-controles/tracabilite-captures.json) documentent cette distinction.

Les figures du PDF sont des captures de **vues de synthèse TShark issues des enregistrements**, et non des captures de l’interface Wireshark reconstituées. Les fichiers joints permettent de contrôler les trames et les champs.

## Reproduire les documents et vérifier la livraison

```text
python -m pip install -r outils/requirements.txt
python outils/generer_note.py
python outils/verifier_livraison.py
```

La génération requiert Python 3 et Arial/Georgia sous Windows ou DejaVu Sans sous Linux. Le contrôle d’intégrité utilise uniquement la bibliothèque standard de Python. Une reconstruction volontaire du PDF peut modifier ses octets ; dans ce cas les empreintes de la livraison initiale ne correspondent plus au nouveau document.

Les disques, ISO, clés privées et fichiers d’identifiants restent hors dépôt. Les exports partagés sont des références expurgées : redéfinir les accès avant restauration. Le fichier `.unl` n’inclut pas les images des équipements.

Le dépôt accompagne le livrable ; la remise Google Classroom et la notation restent des étapes distinctes.
