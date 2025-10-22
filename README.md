# Who Play With Moonlight (WPWM)

Elevage d'Husky Siberien - Application Django

## Configuration Rapide

### 1. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 2. Configuration du fichier .env

Copiez le fichier `.env.example` en `.env` :

```bash
cp .env.example .env
```

Puis modifiez les valeurs dans `.env` selon vos besoins :

- **DEBUG** : `True` en développement, `False` en production
- **SECRET_KEY** : Clé secrète Django (à générer en production)
- **ALLOWED_HOSTS** : Domaines autorisés
- **LANGUAGE_CODE** : Langue du site
- **TIME_ZONE** : Fuseau horaire
- **EMAIL_*** : Configuration email

### 3. Lancer le serveur

```bash
python manage.py runserver
```

Le site sera accessible sur `http://127.0.0.1:8000/`

## Variables d'Environnement Importantes

| Variable | Description | Valeur par défaut |
|----------|-------------|------------------|
| `DEBUG` | Mode débogage | `True` |
| `SECRET_KEY` | Clé Django secrète | (vide) |
| `ALLOWED_HOSTS` | Domaines autorisés | `localhost,127.0.0.1` |
| `LANGUAGE_CODE` | Langue | `fr-fr` |
| `TIME_ZONE` | Fuseau horaire | `Europe/Paris` |
| `STATIC_URL` | URL statiques | `/static/` |

## Structure du Projet

```
WPWM/
├── WPWM/              # Paramètres Django
├── site_WPWM/         # Application principale
│   ├── templates/     # Templates HTML
│   ├── static/        # Fichiers statiques (CSS, JS)
│   │   ├── css/      # Feuilles de style
│   │   └── fonts/    # Polices personnalisées
│   └── views.py      # Vues Django
├── .env               # Variables d'environnement (NE PAS PARTAGER)
├── .env.example       # Exemple de .env
├── manage.py          # Management Django
└── package.json       # Dépendances npm (Tailwind)
```

## Modification des Paramètres

Tous les paramètres importants se trouvent dans le fichier `.env` :

- Changez `DEBUG=False` avant la mise en production
- Modifiez les couleurs avec `PRIMARY_COLOR` et `SECONDARY_COLOR`
- Configurez vos emails avec `EMAIL_*`

## Support

Pour toute question, contactez l'équipe de développement.
