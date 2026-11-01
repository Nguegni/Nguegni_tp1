# Audit avant/après — relevé limité aux preuves

La grille officielle du support et la politique M1 n’ont pas été fournies. Cette matrice de travail ne prétend pas remplacer intégralement la grille officielle. « Avant » désigne le début des observations de ce chat, et non un état historique reconstitué sans protection.

| Contrôle | Avant / référence | Dernière observation documentée | Limite |
|---|---|---|---|
| VLAN / affectation | VLAN 10,20,30,40,50,99,998,999 présents (preuve 02) | Pas de modification VLAN démontrée | SALLE-ATTENTE sur Gi2/0 dans VLAN 10 ; conformité à vérifier |
| Trunk | Gi0/0, natif 998, liste 10,20,30,40,50,99 (03–04) | Même trunk observé après redémarrage dans le chat | Connectivité inter-VLAN complète non testée |
| DHCP Snooping | Actif sur VLAN 10 (06) | Deux liaisons, Gi0/1 et Gi0/2 (08) | Blocage BOX-4G et journal absents |
| DAI | Actif VLAN 10, validations MAC source/destination et IP (07) | Aucun rejet démontré | VLAN 40, liste ARP caméra et attaque non validés |
| IP Source Guard | Aucune interface dans la table initialement | Activation sur Gi0/1–2 (09), échec client (10), retrait (12) | Non validé, cause non déterminée |
| Port Security Gi0/1 | Activé, restrict, une sticky (05) | Pas de changement Port Security démontré | Maximum observé 1 ; énoncé demandant 2 à contrôler |
| Port Security Gi1/3 | Absent du bloc initial ; port shutdown | Maximum 2, compteur 6, journal (13–14), puis retrait pour isoler test 4 | Réactivation finale demandée sans preuve d’exécution |
| STP / BPDU Guard | PVST, valeurs globales PortFast/BPDU Guard désactivées | Rapid-PVST et BPDU Guard Gi1/3 configurés (16), err-disabled (18) | Autres ports d’accès, storm-control et priorité gabarit non validés |
| Racine STP | 5000.0001.0000 pour les six VLAN (16) | Même racine après BPDU (18) | Récupération 300 s non testée |
| 802.1X / MAB / invités | Aucune session prouvée | Aucune session prouvée | TP2.3 non validé |

Le dernier état prouvé de Gi1/3 est err-disabled. La commande finale shutdown et la sauvegarde ne sont pas considérées comme exécutées sur la seule base d’une instruction proposée.
