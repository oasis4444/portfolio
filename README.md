# Création Logiciel Sur Mesure — Portfolio

Portfolio avec démos testables de nos logiciels de gestion (TR Naja, EFA Gestion, Famille Budget, Comptoir, V'lany Gasy, Golden Boutique, Trano).

- `index.html` : la page d'accueil du portfolio
- `demos/` : les logiciels en version démo (données fictives, effacées à la déconnexion)
- `img/` : captures d'écran et logo
- `flask_app.py` : petit serveur pour PythonAnywhere

## Lancer en local

```bash
pip install -r requirements.txt
python flask_app.py
# puis ouvrir http://localhost:5000
```

## Mise en ligne sur PythonAnywhere

1. Console **Bash** : `git clone https://github.com/oasis4444/portfolio.git`
2. Onglet **Web** → *Add a new web app* → *Manual configuration* → Python 3.10 ou plus.
3. Dans le fichier **WSGI**, remplacer le contenu par :

```python
import sys
sys.path.insert(0, '/home/VOTRE_NOM/portfolio')
from flask_app import app as application
```

4. **Reload**. Le site est en ligne sur `https://VOTRE_NOM.pythonanywhere.com`.

Mise à jour : `cd ~/portfolio && git pull`, puis **Reload** dans l'onglet Web.

Contact : WhatsApp +261 34 93 823 59 · oasismdg3434@gmail.com
