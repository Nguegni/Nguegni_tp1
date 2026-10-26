"""Reconstruit la fiche de cinq pages a partir des preuves locales expurgees."""
import pathlib,hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from PIL import Image
from xml.sax.saxutils import escape
repo=pathlib.Path(__file__).resolve().parents[1];out=repo/'01-note-audit'/'Fiche-CamTrust-NGUEGNI-NKODA.pdf'
fontpairs=[(pathlib.Path('C:/Windows/Fonts/georgia.ttf'),pathlib.Path('C:/Windows/Fonts/georgiab.ttf')),(pathlib.Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),pathlib.Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))]
f,b=next((f,b) for f,b in fontpairs if f.exists() and b.exists());pdfmetrics.registerFont(TTFont('Body',str(f)));pdfmetrics.registerFont(TTFont('Bold',str(b)))
W,H=A4;M=39;CW=W-2*M;c=canvas.Canvas(str(out),pagesize=A4);c.setTitle('Ce qui circule en clair - Note d’audit CamTrust Bank');c.setAuthor('NGUEGNI ONGOLO Antoine Depadoux ; NKODA Xavier');c.setSubject('TP0.1 - Remise a niveau TCP/IP orientee securite')
style=ParagraphStyle('body',fontName='Body',fontSize=9.3,leading=12.1,textColor=colors.black)
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
source=[]
ACCENTS={'utilise': 'utilisé', 'decode': 'décodé', 'protege': 'protégé', 'equipement': 'équipement', 'mise a jour': 'mise à jour', 'a verifier': 'à vérifier', 'deployer': 'déployer', 'deploye': 'déployé', 'coupe': 'coupé', 'interne adaptee': 'interne adaptée', 'chiffree': 'chiffrée', 'non autorisees': 'non autorisées', 'usurpee': 'usurpée', 'a jour': 'à jour', 'a l’ecran': 'à l’écran', 'plan de cablage': 'plan de câblage', 'cout': 'coût', 'constitue': 'constitue', 'aider': 'aider', 'pretes': 'prêtes', 'conserve': 'conserve'}
ACCENTS.update({'reellement': 'réellement', 'realises': 'réalisés', 'realise': 'réalisé', 'realisee': 'réalisée', 'realisees': 'réalisées', 'securite': 'sécurité', 'securisation': 'sécurisation', 'binome': 'binôme', 'Resume': 'Résumé', 'resume': 'résumé', 'Perimetre': 'Périmètre', 'perimetre': 'périmètre', 'perimetres': 'périmètres', 'siege': 'siège', 'reseau': 'réseau', 'reseaux': 'réseaux', 'reponses': 'réponses', 'reponse': 'réponse', 'repondu': 'répondu', 'recus': 'reçus', 'recue': 'reçue', 'releve': 'relevé', 'releves': 'relevés', 'revele': 'révèle', 'execute': 'exécuté', 'executes': 'exécutés', 'executee': 'exécutée', 'echange': 'échange', 'echanges': 'échanges', 'entree': 'entrée', 'ete': 'été', 'donnees': 'données', 'communaute': 'communauté', 'supprimee': 'supprimée', 'priorite': 'priorité', 'Priorite': 'Priorité', 'acces': 'accès', 'exposes': 'exposés', 'expose': 'exposé', 'exposee': 'exposée', 'negociation': 'négociation', 'metadonnees': 'métadonnées', 'verifie': 'vérifié', 'verifiee': 'vérifiée', 'verifies': 'vérifiés', 'verifiables': 'vérifiables', 'verification': 'vérification', 'Verification': 'Vérification', 'apres': 'après', 'Apres': 'Après', 'auto-signe': 'auto-signé', 'comparees': 'comparées', 'chiffre': 'chiffré', 'chiffrees': 'chiffrées', 'chiffres': 'chiffrés', 'estime': 'estimé', 'estimes': 'estimés', 'mesures': 'mesurés', 'controle': 'contrôle', 'controles': 'contrôles', 'Controle': 'Contrôle', 'Controles': 'Contrôles', 'critere': 'critère', 'reference': 'référence', 'references': 'références', 'Reference': 'Référence', 'References': 'Références', 'detaille': 'détaillé', 'complementaire': 'complémentaire', 'supplementaire': 'supplémentaire', 'supplementaires': 'supplémentaires', 'identite': 'identité', 'legitimes': 'légitimes', 'necessairement': 'nécessairement', 'concernees': 'concernées', 'fraicheur': 'fraîcheur', 'necessaire': 'nécessaire', 'requetes': 'requêtes', 'precise': 'précise', 'retention': 'rétention', 'reduire': 'réduire', 'defaut': 'défaut', 'maitrisee': 'maîtrisée', 'precis': 'précis', 'communique': 'communiqué', 'presente': 'présenté', 'meme': 'même', 'simule': 'simulé', 'sauvegardees': 'sauvegardées', 'enregistres': 'enregistrés', 'enregistre': 'enregistré', 'limite': 'limité', 'limitee': 'limitée', 'retires': 'retirés', 'retiree': 'retirée', 'depot': 'dépôt', 'cles': 'clés', 'privees': 'privées', 'expurges': 'expurgés', 'expurgees': 'expurgées', 'expurgee': 'expurgée', 'expurge': 'expurgé', 'recalculees': 'recalculées', 'Integrite': 'Intégrité', 'Traçabilite': 'Traçabilité', 'tracabilite': 'traçabilité', 'traçabilite': 'traçabilité', 'lisibilite': 'lisibilité', 'retestes': 'retestés', 'reteste': 'retesté', 'actualite': 'actualité', 'affiches': 'affichés', 'systeme': 'système', 'controlees': 'contrôlées', 'preparation': 'préparation', 'realite': 'réalité', 'synthetique': 'synthétique', 'intermediaire': 'intermédiaire', 'Synthese': 'Synthèse', 'synthese': 'synthèse', 'fonctionnalite': 'fonctionnalité', 'demonstration': 'démonstration', 'metier': 'métier', 'definir': 'définir', 'redefinir': 'redéfinir', 'securises': 'sécurisés', 'debit': 'débit', 'Etat': 'État', 'edition': 'édition', 'Edition': 'Édition', 'Enonce': 'Énoncé', 'enonce': 'énoncé', 'estimates': 'estimations', 'fiabilite': 'fiabilité', 'confidentialite': 'confidentialité'})
def fr(t):
 import re
 for a,b in ACCENTS.items():t=re.sub(r'\b'+re.escape(a)+r'\b',b,t)
 return t.replace('Binome','Binôme').replace('Resultat','Résultat').replace('Resultats','Résultats').replace('Remplacement sur','Remplacement sûr').replace('protocole sur','protocole sûr').replace('a ete','a été').replace('a partir','à partir').replace(' a la ',' à la ').replace(' a un ',' à un ').replace(' a une ',' à une ').replace(' a redefinir',' à redéfinir').replace(' a la ',' à la ').replace(' a longueur',' à longueur').replace(' a l’',' à l’').replace('a l’','à l’')

def p(text,y,size=9.3,x=M,width=CW):
 text=fr(text)
 a=Paragraph(text,ParagraphStyle('p',parent=style,fontSize=size,leading=size*1.32));_,h=a.wrap(width,900);a.drawOn(c,x,H-y-h);assert y+h<792,('Overflow',y+h,text[:55]);return y+h+6

def head(text,y):return p('<b>'+text+'</b>',y,11)
def page(n,title):
 c.setFillColor(colors.black);c.setStrokeColor(colors.black)
 c.setFont('Helvetica',8);c.drawString(M,H-24,'CAMTRUST BANK  /  NOTE D’AUDIT TCP/IP')
 c.setFont('Helvetica',7.5);c.drawRightString(W-M,H-24,'26 OCTOBRE 2026')
 c.setLineWidth(1.6);c.line(M,H-34,M+40,H-34)
 c.setLineWidth(.3);c.line(M+49,H-34,W-M,H-34)
 c.setFont('Bold',16);c.drawString(M,H-61,fr(title))
 c.setLineWidth(.35);c.line(M,36,W-M,36)
 c.setFont('Helvetica',7);c.drawString(M,23,'NGUEGNI ONGOLO Antoine Depadoux  /  NKODA Xavier')
 c.setFont('Helvetica-Bold',8);c.drawRightString(W-M,23,f'{n:02d}  /  05')
 source.append('\n## '+title+'\n')

def text(t,y,*args,**kw):source.append(fr(t).replace('<br/>','\n'));return p(t,y,*args,**kw)
def table(rows,y,widths,size=8.1):
 st=ParagraphStyle('t',parent=style,fontSize=size,leading=size*1.3)
 sh=ParagraphStyle('th',parent=st,fontName='Helvetica-Bold',textColor=colors.white,fontSize=size)
 cells=[[Paragraph(fr(str(v)),sh if i==0 else st) for v in row] for i,row in enumerate(rows)]
 a=Table(cells,colWidths=widths)
 a.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.black),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.Color(.965,.965,.965)]),('LINEBELOW',(0,0),(-1,-1),.3,colors.Color(.65,.65,.65)),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)]))
 _,h=a.wrap(CW,900);assert y+h<785,('Table overflow',y+h);a.drawOn(c,M,H-y-h)
 source.append('\n'+'\n'.join(' | '.join(map(str,r)) for r in rows)+'\n')
 return y+h+9

def image(name,x,y,w):
 # PDF DeviceGray embedding changes display colors only; recorded evidence is retained unchanged.
 im=Image.open(repo/'03-elements-de-preuve'/'illustrations'/name).convert('L');iw,ih=im.size;h=w*ih/iw;c.drawImage(ImageReader(im),x,H-y-h,w,h,mask='auto');return h

def code(txt,x,y,width,size=8):
 for line in txt.strip().splitlines():
  c.setFont('Courier',size);c.drawString(x,H-y-size,line);y+=size*1.23
 return y+5
page(1,'Ce qui circule en clair')
y=86;y=text('<b>Auteurs :</b> NGUEGNI ONGOLO Antoine Depadoux et NKODA Xavier.<br/><b>Objet :</b> justifier la securisation du siege et de l’agence de Douala a partir de preuves de laboratoire.',y)
y=head('1. Resume pour la direction',y+3)
summary=["Le laboratoire CamTrust a satisfait les six controles reseau A.7 lors des essais du 25 octobre.","HTTP, FTP et Telnet exposent des identifiants ; SNMPv2c revele sa communaute et l’inventaire.","HTTPS et SSH rendent les donnees applicatives illisibles dans les captures comparees.","La migration Telnet vers SSH est effective ; la communaute SNMP temporaire a ete supprimee.","La priorite est de fermer les acces en clair, renouveler les secrets et deployer SFTP et SNMPv3."]
for line in summary:y=text(line,y,9.1)
y=head('2. Perimetre et autorisation',y+5)
y=text('Autorisation : travaux realises a la demande du proprietaire de l’environnement, dans son labo EVE-NG <b>TP1</b>. Aucun scan ni capture sur un reseau tiers. Les captures datent du <b>25 octobre 2026</b> ; cette fiche est analysee et mise en forme le <b>26 octobre</b>. Le poste graphique de navigation Internet est distinct et exclu des preuves du TP.',y)
y=text('Huit noeuds : R-SIEGE (IOSv), SW-SIEGE (IOSvL2), R-DLA (CHR 7), R-FAI (VyOS), deux VPCS et deux Ubuntu 24.04. LAN siege 10.10.10.0/24 ; agence 10.20.10.0/24 ; liaison privee 172.16.12.0/30 ; FAI 198.51.100.0/30 ; serveur simule 203.0.113.10. Outils : consoles, tcpdump, Wireshark/TShark 4.6.5, dig, curl, telnet, OpenSSH et snmpwalk.',y)
y=table([['Controle A.7 execute','Resultat conserve dans preuves/'],['DHCP PC-SIEGE','10.10.10.102/24 ; GW 10.10.10.1 ; DNS 203.0.113.10'],['DHCP PC-DLA','10.20.10.199/24, dans la plage .100-.200'],['Douala vers siege','5 reponses au ping 10.10.10.1'],['CLIENT-LINUX vers serveur','3 paquets recus sur 3 vers 203.0.113.10'],['DNS','www.camtrust.lab = 203.0.113.10'],['HTTP','Page Apache recue par CLIENT-LINUX']],y+3,[155,CW-155],8.6)
y=text('<b>Points de capture :</b> SW-SIEGE - R-SIEGE pour ARP, DHCP, Telnet/SSH et SNMP ; R-FAI - SRV-INTERNET pour DNS, TCP, HTTP/HTTPS et FTP. Les adresses dites Internet sont des plages de documentation ; elles ne prouvent aucun acces au reseau reel.',y,8.5)
y=text('<b>Etat observe :</b> les six tests A.7 ont reussi le 25 octobre. Le nouvel etat de fonctionnement apres l’interruption de stockage n’est pas presente comme reteste. Les exports et les preuves enregistres restent disponibles.',y,8.4)
c.showPage()
page(2,'3. Constats : synthese C.5')
y=85;y=table([['Service','Protocole utilise','Visible en clair','Remplacement sur','Effort entreprise'],['Espace agents','HTTP / TCP 80','URL, contenu, utilisateur et secret Basic decode','HTTPS / TLS, certificat valide','4-8 h ; certificat selon PKI'],['Fichiers','FTP / TCP 21','USER, PASS et commandes ; contenu non protege par FTP','SFTP ou FTPS','1-2 jours ; migration des clients'],['Administration','Telnet / TCP 23','Utilisateur, mot de passe et commandes','SSH v2, algorithmes modernes','2-4 h ; mise a jour IOS si besoin'],['Supervision','SNMP v2c / UDP 161','Communaute, nom et version de l’equipement','SNMPv3 authPriv','0,5-1 jour ; outil compatible']],y,[82,83,133,113,CW-411],8)
y=text('Une vue par ligne du tableau : releves d’analyse TShark issus des captures reelles, affiches puis captures a l’ecran. Ce sont des <b>vues de synthese</b>, pas des captures de l’interface Wireshark. Les secrets sont masques ; les PCAPNG expurges permettent de controler les champs et les trames.',y,8.8)
gap=13;w=(CW-gap)/2;top=y+3
for i,(name,label) in enumerate([('C1-releve.png','Figure 1 - Web : HTTP / HTTPS'),('C2-releve.png','Figure 2 - FTP : USER / PASS'),('C3-releve.png','Figure 3 - Telnet / SSH'),('C4-releve.png','Figure 4 - SNMP : exposition / retrait')]):
 x=M+(i%2)*(w+gap);yy=top+(i//2)*147;hh=image(name,x,yy,w);p(label,yy+hh+3,8,x,w)
y=top+2*147
y=text('<b>HTTP :</b> Basic est un encodage Base64, pas un chiffrement. Le secret a ete retrouve et verifie dans l’original. En TLS, seuls la negociation, les metadonnees reseau et le SNI restent visibles ici ; le contenu applicatif est chiffre. Le serveur a repondu 200 en HTTP et HTTPS.',y,8.8)
y=text('<b>Limites :</b> HTTPS utilise le certificat auto-signe du labo (curl -k seulement pour ce test). FTP n’a pas ete migre. Le retrait SNMPv2c ne constitue pas une migration SNMPv3. Ces corrections restent au plan d’action.',y,8.8)
c.showPage()
page(3,'Analyse des captures et enjeux entreprise')
y=86;y=text('Les captures B.1 a B.4 sont conservees sans modification. Les filtres ci-dessous sont des filtres d’affichage Wireshark. B1 contient aussi l’ICMP declencheur ; B4 conserve les deux ports afin de comparer service ouvert et ferme.',y,9)
y=table([['Exercice / filtre','Valeurs reellement relevees'],['B.1 : arp','Requete vers ff:ff:ff:ff:ff:ff ; reponse de 50:00:00:09:00:00 vers le poste ; EtherType 0x0806.'],['B.2 : dhcp','RELEASE puis DORA, DISCOVER retransmis. UDP 68 vers 67, retour 67 vers 68. Offre : /24 ; GW 10.10.10.1 ; DNS 203.0.113.10 ; domaine camtrust.lab ; bail 86 400 s.'],['B.3 : dns','Requete A en UDP : ID 0xab53, port client 51517. En TCP : ID 0x76a1, port client 41799. Reponse 203.0.113.10 ; TTL 300 s.'],['B.4 : tcp.port == 80 || tcp.port == 8080','Trames 1-3 : SYN, SYN-ACK, ACK. HTTP 200 puis FIN-ACK (22-23). Port 80 : 24 trames, environ 12 kB et 0,1002 s. Port 8080 : SYN (25), RST-ACK (26).']],y+3,[137,CW-137],8.7)
y=head('Reponses aux quatre questions entreprise',y+2)
answers=[('B.1 - Retrouver le port d’un poste','Executer show ip arp 10.10.10.157 sur le routeur, puis show mac address-table address &lt;MAC&gt; sur le switch. Si la MAC se trouve sur un lien inter-switch, suivre ce lien jusqu’au port d’acces. Verifier la fraicheur de l’entree ARP et le plan de cablage : une association absente ou usurpee ne suffit pas a identifier un poste.'),('B.2 - Bloquer un serveur DHCP pirate','Activer DHCP snooping sur les VLAN concernes. Declarer de confiance uniquement les ports menant aux serveurs DHCP legitimes, ici la liaison vers R-SIEGE ; les ports des postes restent non fiables. Un OFFER est une reponse de protocole, pas une preuve d’identite du serveur.'),('B.3 - Visibilite DNS et resolveur interne','Le DNS classique expose les noms demandes a un tiers sur le chemin, sans reveler necessairement une page precise ni prouver qu’une visite a abouti. Un resolveur interne applique une politique commune et conserve des traces utiles a l’investigation. Limiter l’acces et la retention des journaux ; DNSSEC ne chiffre pas les requetes.'),('B.4 - RST ou silence a la frontiere','Un RST confirme qu’un hote ou un filtre repond et facilite la reconnaissance. Pour les connexions entrantes non autorisees, un refus par defaut silencieux peut reduire cette indication, sans remplacer la reduction de la surface exposee. Journaliser les refus utiles avec limitation de debit pour detecter les scans sans saturer les traces.')]
for title,answer in answers:
 y=text('<b>'+title+'</b> - '+answer,y+3,9)
c.showPage()
page(4,'4. Plan d’action et controles apres correction')
y=85;y=text('Les efforts ci-dessous sont des estimations pour un petit perimetre, hors attente de changement. Ils ne sont pas des temps mesures pendant le TP. P1 : identifiants exposes et acces d’administration ; P2 : supervision et traitement durable de la dette technique.',y,9)
y=table([['Priorite / service','Correction et critere de recette','Effort / achat','Reference au cours'],['P1 - Web','Certificat valide, HTTPS obligatoire, redirection ou fermeture HTTP ; verifier chaine et nom du certificat. Renouveler les secrets exposes.','4-8 h ; pas d’achat impose si PKI interne adaptee','TP0.1 C.1 ; module d’approfondissement non fourni'],['P1 - Fichiers','Migrer vers SFTP (ou FTPS selon les clients), revoir comptes/droits et couper FTP ; valider un transfert et l’absence de PASS en clair.','1-2 jours ; outils existants a verifier','TP0.1 C.2 ; module d’approfondissement non fourni'],['P1 - Routeur','Conserver SSH v2 et le refus Telnet. Mettre a jour IOS pour les algorithmes modernes, renouveler secret et cles ; retester sans option de compatibilite.','2-4 h ; licence/support seulement si requis par la mise a jour','TP0.1 C.3 ; module d’approfondissement non fourni'],['P2 - Supervision','Deployer SNMPv3 authPriv, limiter les sources de supervision et supprimer v2c ; verifier authentification, chiffrement et refus v2c.','0,5-1 jour ; achat seulement si supervision incompatible','M3 : SNMPv3, explicitement cite par le sujet']],y+3,[80,223,106,CW-409],8.2)
y=text('Les references C.1-C.3 sont verifiables dans l’enonce. Aucun numero de module supplementaire n’est invente : le programme detaille correspondant n’a pas ete fourni.',y,8.5)
y=head('Ce qui a effectivement ete verifie',y+3)
y=table([['Avant / apres','Preuve et limite'],['HTTP / HTTPS','C1-http et C1-https : secret lisible apres decodage Basic dans l’original ; TLS Application Data dans la comparaison. Codes 200 cote client.'],['Telnet / SSH','C3-telnet : identifiants et show version visibles dans l’original. C3-ssh : echange de cles puis paquets chiffres ; show version execute. Apres migration, port Telnet : Connection refused.'],['SNMP v2c / retrait','C4-snmp : communaute et inventaire lisibles. Apres suppression : Timeout: No Response. Pas de preuve SNMPv3, car non deploye.']],y,[113,CW-113],8.4)
y=text('<b>Point technique :</b> cet IOSv ancien exige des options ssh-rsa / diffie-hellman-group14-sha1 pour le seul test OpenSSH. Aucun reglage global du client n’a ete affaibli. Le chiffrement observe ne rend pas ces algorithmes anciens acceptables en production.',y,8.6)
y=text('<b>Etat final enregistre :</b> transport VTY limite a SSH ; communaute de test retiree ; configurations sauvegardees. HTTP et FTP restent disponibles uniquement dans le labo isole pour les exercices.',y,8.7)
c.showPage()
page(5,'5. Annexes : configurations finales')
y=85;y=text('Les exports complets de <b>R-SIEGE.cfg</b>, <b>R-DLA.rsc</b> et <b>R-FAI-config.boot</b> sont integres aux pieces jointes de ce PDF. Les extraits ci-dessous couvrent adressage, DHCP, routage et acces final. Les secrets et empreintes d’authentification sont expurges dans les exports partages ; les redefinir avant toute restauration.',y,8.8)
w=(CW-15)/2;left=M;right=M+w+15;top=y+7
p('<b>A. R-SIEGE - IOSv</b>',top,10,left,w)
rs='''hostname R-SIEGE
ip domain name camtrust.lab
ip dhcp excluded-address
  10.10.10.1 10.10.10.99
ip dhcp pool LAN-SIEGE
 network 10.10.10.0 255.255.255.0
 default-router 10.10.10.1
 dns-server 203.0.113.10
 domain-name camtrust.lab
interface GigabitEthernet0/0
 ip address 10.10.10.1
   255.255.255.0
interface GigabitEthernet0/1
 ip address 198.51.100.2
   255.255.255.252
interface GigabitEthernet0/2
 ip address 172.16.12.1
   255.255.255.252
ip route 0.0.0.0 0.0.0.0
  198.51.100.1
ip route 10.20.10.0 255.255.255.0
  172.16.12.2
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
! Compte admin : secret expurge
! Aucune communaute SNMP de test'''
end=code(rs,left,top+25,w,8.1)
p('Les retours a la ligne dans les commandes longues sont uniquement typographiques. Les valeurs VyOS sont une lecture compacte de l’export. Pour restaurer, utiliser l’export texte complet et definir les acces.',end+8,8.2,left,w)
p('<b>B. R-DLA - RouterOS 7</b>',top,10,right,w)
mt='''/system identity set name=R-DLA
/ip pool add name=pool-dla
 ranges=10.20.10.100-10.20.10.200
/ip address add address=172.16.12.2/30
 interface=ether1 network=172.16.12.0
/ip address add address=10.20.10.1/24
 interface=ether2 network=10.20.10.0
/ip dhcp-server add
 address-pool=pool-dla
 interface=ether2 name=dhcp-dla
/ip dhcp-server network add
 address=10.20.10.0/24
 dns-server=203.0.113.10
 domain=camtrust.lab gateway=10.20.10.1
/ip route add dst-address=0.0.0.0/0
 gateway=172.16.12.1'''
end2=code(mt,right,top+25,w,8.1)
p('<b>C. R-FAI - VyOS</b>',end2+14,10,right,w)
vy='''interfaces ethernet eth0
 address 198.51.100.1/30
interfaces ethernet eth1
 address 203.0.113.1/24
protocols static route 10.0.0.0/8
 next-hop 198.51.100.2
protocols static route 172.16.0.0/12
 next-hop 198.51.100.2
system host-name R-FAI
! Identifiant vyos : secret expurge'''
end2=code(vy,right,end2+41,w,8.1)
y=max(end+55,end2)+18
y=text('<b>Integrite et traçabilite.</b> Le manifeste SHA256-ANNEXES.txt couvre les pieces jointes ; tracabilite-captures.json relie les captures expurgees a leurs originaux locaux. Les copies C1 HTTP, C2 FTP, C3 Telnet et C4 SNMP sont expurgees a longueur constante, avec sommes de controle recalculees. Ni les dates, ni les adresses, ni les resultats applicatifs n’ont ete inventes.',y,8.5)
y=text('<b>Document autonome.</b> Les exports, les dix PCAPNG et les journaux sont integres comme pieces jointes (panneau Pieces jointes d’un lecteur PDF compatible). Cette presentation reprend les preuves du laboratoire commun, sans constituer une nouvelle campagne d’essais. Depot d’accompagnement : github.com/Nguegni/Nguegni_tp1. Cette fiche ne constitue pas une remise Classroom.',y,8.4)
c.save()
(repo/'01-note-audit'/'Note-source.md').write_text('# Ce qui circule en clair - CamTrust Bank\n\nNGUEGNI ONGOLO Antoine Depadoux et NKODA Xavier\n\n'+'\n'.join(source),encoding='utf8')
print(out)


from pieces_jointes import integrer_annexes
integrer_annexes(repo,out)
