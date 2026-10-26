"""Verifie les empreintes de la livraison, sans envoyer de donnees."""
from pathlib import Path
import hashlib,sys
racine=Path(__file__).resolve().parents[1]
erreurs=[];nombre=0
for ligne in (racine/'SHA256SUMS.txt').read_text(encoding='utf-8-sig').splitlines():
    attendu,nom=ligne.split('  ',1);chemin=racine/nom
    if not chemin.is_file():erreurs.append(nom+' absent');continue
    nombre+=1
    if hashlib.sha256(chemin.read_bytes()).hexdigest()!=attendu:erreurs.append(nom+' modifie')
for message in erreurs:print('ECHEC '+message)
print(f'{nombre} fichiers controles ; {len(erreurs)} anomalie(s).')
sys.exit(bool(erreurs))
