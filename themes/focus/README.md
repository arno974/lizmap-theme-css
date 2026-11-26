---
title: Focus
description: La carte d'abord. Au repos, quelques pastilles rondes ; le menu s'ouvre en liste d'outils au survol, la loupe s'allonge en champ de recherche, les panneaux sont des cartes flottantes.
author: arno974 (Geolab)
created: 2026-10-20
updated: 2026-11-02
version: 1.1.0
lizmap: 3.9
license: MPL-2.0
preview: screenshots/desktop.png
mobile: non testé
external_resources: Google Fonts
tags: clair, minimaliste, pastilles, menu repliable, carte plein écran
---

# Focus

Thème clair et minimaliste : la carte occupe tout l'écran, les commandes se réduisent à des pastilles rondes
qui ne s'ouvrent qu'à la demande. Police Inter, accent vert-bleu.

![Aperçu](screenshots/desktop.png)

- **Menu** : une pastille ☰ en haut à gauche. Au survol (ou au clavier), elle s'ouvre en liste « Outils »
  avec le nom de chaque outil, groupés par type et séparés par un filet. L'outil actif est teinté d'accent.
- **Recherche** : une pastille loupe à côté du menu, qui s'allonge en champ au survol et reste ouverte
  tant qu'un texte est saisi.
- **Messages** (mesure, erreurs...) : une pastille au centre de la ligne du haut. Une petite pastille de couleur
  indique le type : accent pour une information, vert, orange ou rouge pour un succès, un avertissement, une erreur.
- **Compte** : une pastille en haut à droite.
- **Panneaux** : cartes flottantes arrondies sous les pastilles ; mini-panneaux à gauche des contrôles de zoom.
- **Titre du projet** posé sur la carte en bas à gauche, comme le titre d'une carte imprimée.
  Il n'apparaît que sur la carte dégagée et s'efface dès qu'un panneau est ouvert.
  Le nom du dépôt est masqué. Le logo est masqué.

Le thème est construit sur la base de [Cartouche, barre verticale](../cartouche-vertical) (compatibilité 3.9,
popups, listes), à laquelle s'ajoute la surcouche Focus en fin de `map.css`.

## Contenu

```
src/                         sources lisibles : c'est ici qu'on modifie
  main.css                   police, couleurs, dimensions
  map.css                    base Cartouche, puis bloc « Focus : surcouche de la base Cartouche »
  media.css                  écrans tactiles et téléphones : bouton menu, tiroir, panneaux en feuille
media/themes/default/css/    fichiers générés, à installer (ne pas modifier à la main)
screenshots/                 aperçus
```

Après une modification dans `src/`, régénérer depuis la racine du dépôt :

```
python3 tools/build.py themes/focus
```

## Installation

1. Dans l'administration Lizmap, sur le dépôt visé, cocher **Autoriser les thèmes utilisateurs**.
2. Copier le dossier **généré** `media/themes/default/` (pas `src/`) dans le dossier `media/` du dépôt,
   ou un niveau au-dessus des dépôts pour l'appliquer à tous.
3. Droits : 755 pour les dossiers, 644 pour les fichiers.
4. Recharger la carte avec Ctrl+Maj+R : Lizmap sert ces CSS avec un cache d'un jour.

Archive prête à décompresser à la racine d'un dépôt : `python3 tools/build.py --zip themes/focus`.

## Personnaliser

### Couleurs (`src/main.css`, `:root`)

| Variable | Rôle | Valeur |
|---|---|---|
| `--c-ink` | encre : texte et icônes (doit rester foncée) | `#1c2430` |
| `--c-accent` | accent : outil actif, pastille des messages, cases cochées, boutons principaux | `#0f766e` |
| `--c-paper` | fond des pastilles, panneaux et cartes flottantes | `#ffffff` |
| `--c-mist` | survol | `#f2f4f7` |
| `--c-rule` | filets et bordures | `#e1e5ea` |

Pour un seul projet ou depuis l'administration (CSS additionnel), même principe que Cartouche :
`:root:root { --c-ink: ...; --c-accent: ...; }`.

**Exception : les contrôles de zoom.** Leurs icônes sont des images blanches ; le thème inverse tout le bouton
et lui donne des fonds « négatifs » (`#000`, `#0d0b08`, `#f08991` dans `map.css`, bloc « Zoom »)
qui deviennent, après inversion, le blanc, le survol et l'accent. Si vous changez `--c-paper`, `--c-mist`
ou `--c-accent`, recalculez ces trois valeurs (couleur inverse : 255 moins chaque composante).

### Dimensions

| Variable | Rôle | Valeur |
|---|---|---|
| `--pill` | diamètre des pastilles (menu, loupe, compte, messages) | `44px` |
| `--edge` | marge des pastilles au bord de l'écran | `16px` |
| `--menu-open` | largeur du menu déplié | `240px` |
| `--dock-w` | largeur du panneau gauche (réduite sur petit écran, comme Cartouche) | `380px` |
| `--r` | arrondi des panneaux | `16px` |

## Téléphones et tablettes

Sur un écran tactile, Lizmap remplace la barre d'outils par un bouton menu et un tiroir latéral, quelle que soit la
largeur de l'écran. `media.css` (chargé par Lizmap après `map.css`) les habille aux couleurs du thème : outils en liste
avec leur nom, cibles de 48 px de haut, outil actif mis en évidence.

Sur un téléphone (écran tactile de moins de 900 px de large, seuil de l'affichage mobile de Lizmap, ou téléphone à l'horizontale) :
- en-tête : une seule ligne : bouton menu, recherche (toujours ouverte sur téléphone) et compte. Le titre reste en bas à gauche.
- boutons de compte réduits à leur icône ; champ de recherche en 16 px (le téléphone ne zoome pas à la saisie) ;
- panneaux (couches, popup, filtre, données) et mini-panneaux (mesure, impression...) en feuille depuis le bas de l'écran :
  la carte reste visible au-dessus ;
- vue d'ensemble et coordonnées masquées.

Sur ordinateur, `media.css` n'a aucun effet (vérifié : captures identiques avec et sans).

## Limites connues

- Affichage tactile vérifié en émulation sur Lizmap 3.9.6 (téléphone 390 × 844 et 844 × 390, tablette 1024 × 768), pas encore sur un vrai téléphone ni en 3.10.
- Testé uniquement en **Lizmap 3.9** (dépôt de test local), en desktop, connecté en administrateur.
  **Non testé en 3.10** ni en affichage mobile.
- Le menu et la recherche s'ouvrent au **survol** : sur écran tactile, il faut toucher la pastille.
- Sur un écran étroit (vers 1200 px), la recherche dépliée peut passer sur le message du haut le temps de la saisie.
- **Icônes** : les icônes de Lizmap sont blanches au repos et noires au survol ou à l'état actif ; le thème
  les inverse selon l'état (`filter: invert()`). Une icône qui ne suivrait pas cette règle peut apparaître
  claire sur fond clair.
- Les infobulles des outils du menu sont masquées : les libellés de la liste les remplacent.
- **Polices** chargées depuis Google Fonts (Inter, IBM Plex Mono) : à héberger localement
  pour éviter tout appel externe (RGPD, réseau fermé).
- Sélecteurs `:has()` utilisés (Chrome 105+, Firefox 121+, Safari 15.4+).
- Page d'accueil non concernée : Lizmap n'applique les thèmes du dossier `media` qu'aux pages carte.
