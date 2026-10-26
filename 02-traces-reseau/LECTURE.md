# Retrouver les échanges

| Fichier | Point d’observation | Filtre d’affichage |
|---|---|---|
| fondamentaux/B1-arp.pcapng | SW-SIEGE - R-SIEGE | `arp` |
| fondamentaux/B2-dhcp.pcapng | SW-SIEGE - R-SIEGE | `dhcp` |
| fondamentaux/B3-dns.pcapng | R-FAI - SRV-INTERNET | `dns` |
| fondamentaux/B4-tcp.pcapng | R-FAI - SRV-INTERNET | `tcp.port == 80 || tcp.port == 8080` |
| services/C1-http.pcapng | R-FAI - SRV-INTERNET | `http.authorization` |
| services/C1-https.pcapng | R-FAI - SRV-INTERNET | `tls` |
| services/C2-ftp.pcapng | R-FAI - SRV-INTERNET | `ftp.request.command == "USER" || ftp.request.command == "PASS"` |
| services/C3-telnet.pcapng | SW-SIEGE - R-SIEGE | `telnet`, puis Suivre > Flux TCP |
| services/C3-ssh.pcapng | SW-SIEGE - R-SIEGE | `ssh` |
| services/C4-snmp.pcapng | SW-SIEGE - R-SIEGE | `snmp` |

B1 conserve aussi l’ICMP déclencheur ; B4 conserve le port 8080 fermé pour la comparaison avec le port 80 ouvert. Les numéros de trame cités dans la note correspondent à ces fichiers complets.

Le secret HTTP est masqué avant réencodage Base64 ; FTP PASS et le secret du flux Telnet sont remplacés à longueur constante. La communauté SNMP est masquée. Ces fichiers ne doivent pas être décrits comme des originaux bruts inchangés. Les adresses, dates, ports et résultats applicatifs restent ceux des observations.
