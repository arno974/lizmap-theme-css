---
title: Net
description: Sobre et lisible. Barre de titre blanche pleine largeur avec la recherche au centre, colonne d'outils toujours affichée avec leur nom, panneau collé à la colonne.
author: arno974 (Geolab)
created: 2026-10-20
updated: 2026-11-02
version: 1.1.0
lizmap: 3.9
license: MPL-2.0
preview: screenshots/desktop.png
mobile: non testé
external_resources: Google Fonts
tags: clair, sobre, barre de titre, libellés visibles, accessibilité
---

# Net

Thème clair et sobre, pensé pour une prise en main immédiate : rien ne se replie, chaque outil est nommé.
Police Inter, un seul accent bleu.

![Aperçu](screenshots/desktop.png)

- **Barre de titre** blanche sur toute la largeur : logo, titre du projet, grand champ de recherche au centre,
  boutons de compte à droite. Le nom du dépôt est masqué.
- **Colonne d'outils** blanche à gauche, sous la barre, avec le nom de chaque outil toujours visible.
  Les outils sont groupés par type (panneaux, outils, tableaux) et séparés par un filet ; Accueil est en bas.
  L'outil actif est en bleu, avec un trait à gauche.
- **Panneau gauche** collé à la colonne, sous la barre, sur toute la hauteur.
- **Contrôles de zoom**, mini-panneaux et tableau de données en cartes blanches à bords légèrement arrondis.

Le thème est construit sur la base de [Cartouche, barre verticale](../cartouche-vertical) (compatibilité 3.9,
popups, listes, messages), à laquelle s'ajoute la surcouche Net en fin de `map.css`.

## Contenu

```
src/                         sources lisibles : c'est ici qu'on modifie
  main.css                   police, couleurs, dimensions
  map.css                    base Cartouche, puis bloc « Net : surcouche de la base Cartouche »
  media.css                  écrans tactiles et téléphones : bouton menu, tiroir, panneaux en feuille
media/themes/default/css/    fichiers générés, à installer (ne pas modifier à la main)
screenshots/                 aperçus
```

Après une modification dans `src/`, régénérer depuis la racine du dépôt :

```
python3 tools/build.py themes/net
```

## Installation

1. Dans l'administration Lizmap, sur le dépôt visé, cocher **Autoriser les thèmes utilisateurs**.
2. Copier le dossier **généré** `media/themes/default/` (pas `src/`) dans le dossier `media/` du dépôt,
   ou un niveau au-dessus des dépôts pour l'appliquer à tous.
3. Droits : 755 pour les dossiers, 644 pour les fichiers.
4. Recharger la carte avec Ctrl+Maj+R : Lizmap sert ces CSS avec un cache d'un jour.

Archive prête à décompresser à la racine d'un dépôt : `python3 tools/build.py --zip themes/net`.

## Personnaliser

### Couleurs (`src/main.css`, `:root`)

| Variable | Rôle | Valeur |
|---|---|---|
| `--c-ink` | encre : texte et icônes (doit rester foncée) | `#1b2533` |
| `--c-accent` | accent : outil actif, focus de la recherche, cases cochées, boutons principaux | `#1a56db` |
| `--c-paper` | fond de la barre, de la colonne et des panneaux | `#ffffff` |
| `--c-mist` | survol, fond du champ de recherche | `#f2f5f9` |
| `--c-rule` | filets et bordures | `#d8dee6` |

Pour un seul projet ou depuis l'administration (CSS additionnel), même principe que Cartouche :
`:root:root { --c-ink: ...; --c-accent: ...; }`. Le fond de l'outil actif (`#e8effd`) est un bleu très pâle
écrit en dur dans `map.css` : à adapter si vous changez l'accent.

**Exception : les contrôles de zoom.** Leurs icônes sont des images blanches ; le thème inverse tout le bouton
et lui donne des fonds « négatifs » (`#000`, `#0d0a06`, `#e5a924` dans `map.css`, bloc « Zoom »)
qui deviennent, après inversion, le blanc, le survol et l'accent. Si vous changez `--c-paper`, `--c-mist`
ou `--c-accent`, recalculez ces trois valeurs (couleur inverse : 255 moins chaque composante).

### Dimensions

| Variable | Rôle | Valeur |
|---|---|---|
| `--bar` | hauteur de la barre de titre | `60px` |
| `--side` | largeur de la colonne des outils | `208px` |
| `--dock-w` | largeur du panneau gauche (réduite sur petit écran, comme Cartouche) | `380px` |
| `--r` | arrondi des cartes et boutons | `8px` |

## Logo

`Geolab-Logo-Verti-Noir.png`, à gauche de la barre de titre. Pour en changer : remplacer le fichier dans `src/`
(et le nom dans `map.css`, bloc « Logo Geolab »), puis régénérer.

## Téléphones et tablettes

Sur un écran tactile, Lizmap remplace la barre d'outils par un bouton menu et un tiroir latéral, quelle que soit la
largeur de l'écran. `media.css` (chargé par Lizmap après `map.css`) les habille aux couleurs du thème : outils en liste
avec leur nom, cibles de 48 px de haut, outil actif mis en évidence.

Sur un téléphone (écran tactile de moins de 900 px de large, seuil de l'affichage mobile de Lizmap, ou téléphone à l'horizontale) :
- en-tête : la barre de titre passe sur deux lignes : bouton menu, logo, titre et compte, puis la recherche sur toute la largeur.
- boutons de compte réduits à leur icône ; champ de recherche en 16 px (le téléphone ne zoome pas à la saisie) ;
- panneaux (couches, popup, filtre, données) et mini-panneaux (mesure, impression...) en feuille depuis le bas de l'écran :
  la carte reste visible au-dessus ;
- vue d'ensemble et coordonnées masquées.

Sur ordinateur, `media.css` n'a aucun effet (vérifié : captures identiques avec et sans).

## Limites connues

- Affichage tactile vérifié en émulation sur Lizmap 3.9.6 (téléphone 390 × 844 et 844 × 390, tablette 1024 × 768), pas encore sur un vrai téléphone ni en 3.10.
- Testé uniquement en **Lizmap 3.9** (dépôt de test local), en desktop, connecté en administrateur.
  **Non testé en 3.10** ni en affichage mobile.
- La colonne d'outils prend 208 px en permanence : moins de place pour la carte que les thèmes à rail replié.
- **Icônes** : les icônes de Lizmap sont blanches au repos et noires au survol ou à l'état actif ; le thème
  les inverse selon l'état (`filter: invert()`). Une icône qui ne suivrait pas cette règle peut apparaître
  claire sur fond clair.
- Les infobulles des outils sont masquées : les libellés de la colonne les remplacent.
- **Polices** chargées depuis Google Fonts (Inter, IBM Plex Mono) : à héberger localement
  pour éviter tout appel externe (RGPD, réseau fermé).
- Sélecteurs `:has()` utilisés (Chrome 105+, Firefox 121+, Safari 15.4+).
- Page d'accueil non concernée : Lizmap n'applique les thèmes du dossier `media` qu'aux pages carte.
