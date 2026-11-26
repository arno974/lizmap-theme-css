---
title: Tiroir
description: Clair, façon carte papier. Rail d'outils fin qui s'ouvre en tiroir au survol avec les libellés, panneau collé au rail sur toute la hauteur, titre de carte en bas à gauche.
author: arno974 (Geolab)
created: 2026-10-19
updated: 2026-11-02
version: 1.1.0
lizmap: 3.9
license: MPL-2.0
preview: screenshots/desktop.png
mobile: non testé
external_resources: Google Fonts
tags: clair, papier, rail repliable, tiroir, couleurs personnalisables
---

# Tiroir

Thème clair, façon carte papier : fond crème, encre bleu-vert, accent ocre, titres en serif.

![Aperçu](screenshots/desktop.png)

- **Rail d'outils** fin (56 px), collé au bord gauche sur toute la hauteur. Au survol (ou au clavier),
  il s'ouvre en tiroir et affiche le nom de chaque outil. Les outils sont groupés par type
  (panneaux, outils, tableaux) et séparés par un filet ; Accueil est en bas.
- **Panneau gauche** collé au rail, sur toute la hauteur.
- **Titre du projet** posé sur la carte en bas à gauche, comme le titre d'une carte imprimée.
  Il n'apparaît que sur la carte dégagée : il s'efface dès que le rail s'ouvre ou qu'un panneau est ouvert.
  Le nom du dépôt, qui répète souvent le titre, est masqué.
- **Recherche** centrée dans l'espace libre entre le rail (ou le panneau ouvert) et le bouton de compte.
- **Contrôles de carte** (zoom, déplacement), mini-panneaux et boutons dans les mêmes tons clairs ;
  l'outil ou le bouton actif est repéré en ocre.

Le thème est construit sur la base de [Cartouche, barre verticale](../cartouche-vertical) (compatibilité 3.9,
popups, listes, recherche adaptative), à laquelle s'ajoute la surcouche Tiroir en fin de `map.css`.

## Contenu

```
src/                         sources lisibles : c'est ici qu'on modifie
  main.css                   polices, couleurs, dimensions
  map.css                    base Cartouche, puis bloc « Tiroir : surcouche de la base Cartouche »
  media.css                  écrans tactiles et téléphones : bouton menu, tiroir, panneaux en feuille
media/themes/default/css/    fichiers générés, à installer (ne pas modifier à la main)
screenshots/                 aperçus
```

Après une modification dans `src/`, régénérer depuis la racine du dépôt :

```
python3 tools/build.py themes/tiroir
```

## Installation

1. Dans l'administration Lizmap, sur le dépôt visé, cocher **Autoriser les thèmes utilisateurs**.
2. Copier le dossier **généré** `media/themes/default/` (pas `src/`) dans le dossier `media/` du dépôt,
   ou un niveau au-dessus des dépôts pour l'appliquer à tous.
3. Droits : 755 pour les dossiers, 644 pour les fichiers.
4. Recharger la carte avec Ctrl+Maj+R : Lizmap sert ces CSS avec un cache d'un jour.

Archive prête à décompresser à la racine d'un dépôt : `python3 tools/build.py --zip themes/tiroir`.

## Personnaliser

### Couleurs (`src/main.css`, `:root`)

| Variable | Rôle | Valeur |
|---|---|---|
| `--c-ink` | encre : texte et icônes (doit rester foncée) | `#1f3a3d` |
| `--c-accent` | accent : outil actif, filets, cases cochées, boutons principaux | `#c46a2b` |
| `--c-paper` | papier : rail, panneaux, cartes flottantes | `#fbf8f3` |
| `--c-mist` | survol | `#f1ebe1` |
| `--c-rule` | filets et bordures | `#e3d9c9` |

Pour un seul projet ou depuis l'administration (CSS additionnel), même principe que Cartouche :
`:root:root { --c-ink: ...; --c-accent: ...; }`.

**Exception : les contrôles de zoom.** Leurs icônes sont des images blanches ; le thème inverse tout le bouton
et lui donne des fonds « négatifs » (`#04070c`, `#0e141e`, `#3b95d4` dans `map.css`, bloc « Controles de carte »)
qui deviennent, après inversion, le papier, le survol et l'ocre. Si vous changez `--c-paper`, `--c-mist`
ou `--c-accent`, recalculez ces trois valeurs (couleur inverse : 255 moins chaque composante).

### Dimensions

| Variable | Rôle | Valeur |
|---|---|---|
| `--rail` / `--rail-open` | rail replié / déplié au survol | `56px` / `236px` |
| `--dock-w` | largeur du panneau gauche (réduite sur petit écran, comme Cartouche) | `380px` |
| `--head` | hauteur de la bande du haut (case du logo, recherche, compte) | `64px` |

## Logo

Le thème ne fournit pas de logo : il affiche le logo d'en-tête défini dans l'administration Lizmap (Apparence, « Logo d'en-tête »), dans la case haute du rail.

## Téléphones et tablettes

Sur un écran tactile, Lizmap remplace la barre d'outils par un bouton menu et un tiroir latéral, quelle que soit la
largeur de l'écran. `media.css` (chargé par Lizmap après `map.css`) les habille aux couleurs du thème : outils en liste
avec leur nom, cibles de 48 px de haut, outil actif mis en évidence.

Sur un téléphone (écran tactile de moins de 900 px de large, seuil de l'affichage mobile de Lizmap, ou téléphone à l'horizontale) :
- en-tête : une seule ligne : bouton menu, recherche et compte. Le logo (case du rail) est masqué, le titre reste en bas à gauche.
- boutons de compte réduits à leur icône ; champ de recherche en 16 px (le téléphone ne zoome pas à la saisie) ;
- panneaux (couches, popup, filtre, données) et mini-panneaux (mesure, impression...) en feuille depuis le bas de l'écran :
  la carte reste visible au-dessus ;
- vue d'ensemble et coordonnées masquées.

Sur ordinateur, `media.css` n'a aucun effet (vérifié : captures identiques avec et sans).

## Limites connues

- Affichage tactile vérifié en émulation sur Lizmap 3.9.6 (téléphone 390 × 844 et 844 × 390, tablette 1024 × 768), pas encore sur un vrai téléphone ni en 3.10.
- Testé uniquement en **Lizmap 3.9** (dépôt de test local), en desktop, déconnecté et connecté en administrateur.
  **Non testé en 3.10** ni en affichage mobile.
- **Icônes** : les icônes de Lizmap sont blanches au repos et noires au survol ou à l'état actif ; le thème
  les inverse selon l'état (`filter: invert()`). Une icône qui ne suivrait pas cette règle peut apparaître
  claire sur fond clair.
- Les infobulles des outils du rail sont masquées : les libellés du tiroir les remplacent.
- **Polices** chargées depuis Google Fonts (Source Serif 4, Public Sans, IBM Plex Mono) : à héberger localement
  pour éviter tout appel externe (RGPD, réseau fermé).
- Sélecteurs `:has()` utilisés (Chrome 105+, Firefox 121+, Safari 15.4+).
- Page d'accueil non concernée : Lizmap n'applique les thèmes du dossier `media` qu'aux pages carte.
