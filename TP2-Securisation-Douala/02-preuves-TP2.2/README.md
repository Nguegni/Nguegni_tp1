# Menace → mesure → preuve — TP2.2

| Test / menace | Mesure | État de référence / avant | Après / journal | Conclusion |
|---|---|---|---|---|
| 1 — DHCP pirate BOX-4G | DHCP Snooping, Gi0/0 trusted | Attaque avant protection non documentée | [Snooping VLAN 10 actif](../preuves/06-dhcp-snooping.png), [deux bindings](../preuves/08-bindings-deux-clients.png). Aucun DHCP_SNOOPING_UNTRUSTED_PORT fourni. | Partiel : les cinq renouvellements avant/après et le rejet du DHCP pirate ne sont pas prouvés. |
| 2 — Usurpation ARP / IP source | DAI et IP Source Guard | [DAI VLAN 10 actif, 410 transmis, 0 rejeté](../preuves/07-dai-etat.png) ; [IPSG actif sur deux ports](../preuves/09-ipsg-active.png) | [Échec du client légitime](../preuves/10-ipsg-client-echec.png), [retour des réponses](../preuves/11-client-retablissement.png), [IPSG retiré](../preuves/12-ipsg-retire.png). Aucun journal de rejet DAI fourni. | Non validé : aucune attaque ARP démontrée ; IPSG retiré après perturbation. Cause non déterminée. |
| 3 — Trois postes derrière SW-PIRATE | Port Security, maximum 2, restrict sur Gi1/3 | [0 MAC et 0 violation, maximum 2](../preuves/13-port-security-avant.png) | [2 MAC, 6 violations et PSECURE_VIOLATION](../preuves/14-port-security-apres-journal.png), [pings des deux postes autorisés](../preuves/15-deux-clients-ping.png) | Limite et rejet démontrés. L’état avant est celui du compteur avant trafic ; une phase sans protection avec trois postes communicants n’a pas été capturée. |
| 4 — BPDU d’un commutateur pirate | Rapid-PVST, PortFast et BPDU Guard sur Gi1/3 | [Configuration et racine avant](../preuves/16-bpduguard-configuration-racine-avant.png) | [BLOCK_BPDUGUARD](../preuves/17-bpduguard-journal.png), [Gi1/3 err-disabled et racine après](../preuves/18-bpduguard-etat-racine-apres.png) | Blocage et racine inchangée démontrés ; récupération automatique 300 s non testée. |

## Précisions test 3

Les deux MAC acceptées sur Gi1/3 sont 0050.7966.680c et 0050.7966.680d ; le journal signale le rejet de 0050.7966.680e. Les deux clients ayant obtenu 10.20.10.197 et 10.20.10.198 reçoivent chacun cinq réponses de 10.20.10.1. L’échec DHCP du troisième poste a été observé dans le chat ; la preuve déterminante conservée est le journal de violation.

## Précisions test 4

Port Security a d’abord signalé la MAC 5000.000a.0000 du commutateur, sans déclenchement BPDU Guard visible. Il a été retiré temporairement de Gi1/3 pour isoler le test BPDU Guard. Le journal de blocage apparaît à 20:46:10 le 1er novembre 2026 selon l’horloge du commutateur. La racine reste 5000.0001.0000, avec les mêmes priorités affichées pour les VLAN 10, 20, 30, 40, 50 et 99. Ce résultat ne prouve pas le fonctionnement simultané des deux protections.

Les journaux sont fournis dans les captures originales : aucun faux fichier de logs n’a été produit. Les dates/horaires sont ceux affichés par les équipements ; leur synchronisation n’a pas été vérifiée.
