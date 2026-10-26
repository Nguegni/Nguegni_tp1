"""Integre les annexes expurgees a la note PDF, sans acces reseau."""
from pathlib import Path
import hashlib
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject

def integrer_annexes(repo:Path,pdf:Path):
    pieces={}
    for dossier in ['04-configurations','02-traces-reseau','03-elements-de-preuve']:
        for p in sorted((repo/dossier).rglob('*')):
            if p.is_file() and p.suffix in ['.cfg','.rsc','.boot','.pcapng','.txt']:
                assert p.name not in pieces
                pieces[p.name]=p.read_bytes()
    for nom in ['tracabilite-captures.json','validation-captures.json']:
        pieces[nom]=(repo/'06-controles'/nom).read_bytes()
    pieces['LIRE-LES-ANNEXES.txt']='''CAMTRUST BANK - NOTE D'AUDIT
NGUEGNI ONGOLO Antoine Depadoux et NKODA Xavier

Ces annexes proviennent du laboratoire commun CamTrust. La presentation ne constitue pas une nouvelle campagne independante de tests. Essais enregistres le 25 octobre 2026 ; analyse et mise en forme le 26 octobre 2026.

Les captures sensibles sont expurgees ; les originaux restent conserves localement. Les secrets ont ete remplaces a longueur constante et les sommes de controle recalculees. Les empreintes des originaux et des copies figurent dans tracabilite-captures.json. Les figures sont des captures de vues de synthese TShark, pas l'interface native de Wireshark.

Les exports des routeurs sont expurges de leurs secrets d'authentification. Les redefinir avant restauration. Aucune image de machine ni cle privee n'est incluse.

Les modules d'approfondissement HTTPS, SFTP/FTPS et SSH ne sont pas identifies faute de programme detaille ; la reference M3 pour SNMPv3 figure dans le sujet. SFTP/FTPS et SNMPv3 ne sont pas declares deployes. Les six tests A.7 n'ont pas ete integralement relances apres le blocage de stockage.

Depot d'accompagnement : https://github.com/Nguegni/Nguegni_tp1
La publication GitHub ne constitue pas une remise Google Classroom.
'''.encode('utf8')
    pieces['SHA256-ANNEXES.txt']=''.join(hashlib.sha256(b).hexdigest()+'  '+n+'\n' for n,b in sorted(pieces.items())).encode('utf8')
    lecteur=PdfReader(pdf);sortie=PdfWriter();sortie.clone_document_from_reader(lecteur)
    for nom,contenu in pieces.items():sortie.add_attachment(nom,contenu)
    sortie._root_object.update({NameObject('/PageMode'):NameObject('/UseAttachments')})
    temporaire=pdf.with_suffix('.temp.pdf')
    with temporaire.open('wb') as f:sortie.write(f)
    temporaire.replace(pdf)
    controle=PdfReader(pdf)
    assert len(controle.pages)==5
    for nom,contenu in pieces.items():assert list(controle.attachments[nom])[0]==contenu
    print(f'{len(pieces)} annexes integrees et verifiees.')
