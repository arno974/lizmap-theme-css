# Contribuer un thème

Toute contribution est bienvenue : nouveau thème, variante, correction ou test sur une autre version de Lizmap.

## Ajouter un thème

1. Créer un dossier `themes/<nom>/` : nom court, en minuscules, mots séparés par des tirets
   (ex. `cartouche-horizontal`). Une variante de disposition est un nouveau dossier ; une évolution
   du même thème change son numéro de version.
2. Mettre les CSS lisibles dans `src/` (`main.css`, `map.css`...) ainsi que les images qu'ils référencent en relatif.
3. Générer les fichiers à installer : `python3 tools/build.py themes/<nom>`.
4. Ajouter au moins une capture `screenshots/desktop.png` (voir plus bas).
5. Écrire `README.md` en commençant par l'en-tête ci-dessous.
6. Mettre à jour le catalogue puis vérifier : `python3 tools/check.py --catalog`.

## En-tête du README

Copier ce modèle en tout début de `README.md`, entre les deux lignes `---`.
Une information par ligne, sous la forme `clé: valeur`. Les clés restent en anglais ; les valeurs peuvent être en français.

```markdown
---
title: Nom affiché du thème
description: Une ou deux phrases sur ce qui caractérise le thème.
author: Prénom Nom (Organisme)
created: 2026-10-15
updated: 2026-10-15
version: 1.0.0
lizmap: 3.9, 3.10
license: MPL-2.0
preview: screenshots/desktop.png
mobile: non testé
external_resources: Google Fonts
tags: plein écran, sombre
---
```

| Clé | Obligatoire | Contenu |
|---|---|---|
| `title` | oui | nom affiché dans le catalogue |
| `description` | oui | une ou deux phrases |
| `author` | oui | auteur et, si besoin, organisme |
| `created` | oui | date de création, `AAAA-MM-JJ` |
| `updated` | non | date de dernière modification, `AAAA-MM-JJ` |
| `version` | oui | version du thème : `1.0.0`, puis `1.0.1` pour une correction, `1.1.0` pour un ajout, `2.0.0` si l'installation ou la personnalisation change |
| `lizmap` | oui | versions de Lizmap **réellement testées**, séparées par des virgules |
| `license` | oui | `MPL-2.0` (licence du dépôt) sauf raison particulière |
| `preview` | oui | chemin de l'image d'aperçu, relatif au dossier du thème |
| `mobile` | non | `testé` ou `non testé` |
| `external_resources` | non | services externes appelés par le CSS (polices, images) ; important pour le RGPD et les réseaux fermés |
| `tags` | non | mots-clés séparés par des virgules |

Le reste du README est libre ; on y attend au moins : installation, personnalisation (variables), limites connues.

## Captures d'écran

- `screenshots/desktop.png` obligatoire : carte entière, en 1440 × 900 environ, avec un panneau ouvert (couches par exemple).
- Facultatif : d'autres vues (`panel-data.png`, `search.png`, `mobile.png`...) ou une variante de couleurs.
- Utiliser un projet public (démonstration Lizmap, données ouvertes) : pas de données clients ni de noms de clients.
- PNG de moins de 500 Ko si possible.

## Bonnes pratiques CSS

- Regrouper les couleurs, rayons et marges dans des variables `:root` documentées dans le README.
- Si le thème cible plusieurs versions de Lizmap, isoler les règles propres à une version dans un bloc commenté.
- Ne pas modifier `media/` à la main : il est régénéré depuis `src/`, et `tools/check.py` signale tout écart.
- Signaler dans `external_resources` tout appel externe, ou héberger les ressources dans `src/`.
- Logos et images : uniquement ceux que l'on a le droit de diffuser sous la licence du thème.
