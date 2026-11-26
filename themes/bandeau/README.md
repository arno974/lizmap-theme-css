---
title: Bandeau
description: Aux couleurs d'une collectivité. Bandeau du haut en couleur pleine avec logo, titre et recherche, rail d'outils dans la même couleur, panneau collé au rail, pied de page pour les sources et mentions.
author: arno974 (Geolab)
created: 2026-10-20
updated: 2026-11-02
version: 1.1.0
lizmap: 3.9
license: MPL-2.0
preview: screenshots/desktop.png
mobile: non testé
external_resources: Google Fonts
tags: clair, institutionnel, collectivité, bandeau, pied de page, couleur personnalisable
---

# Bandeau

Thème institutionnel, pensé pour décliner une carte aux couleurs de chaque client :
une seule couleur à changer. Police Source Sans 3.

![Aperçu](screenshots/desktop.png)

- **Bandeau** en couleur pleine sur toute la largeur : logo sur une tuile blanche, titre du projet en blanc,
  champ de recherche blanc au centre, boutons de compte à droite. Le nom du dépôt est masqué.
- **Rail d'outils** dans une nuance plus foncée de la même couleur, collé au bord gauche, du bandeau au pied de page.
- **Panneau gauche** collé au rail ; son titre est souligné dans la couleur de la collectivité.
- **Contrôles de zoom** dans la couleur du rail.
- **Pied de page** blanc sur toute la largeur, pour les sources, les mentions ou un contact.
  Le logo « Powered by 3Liz » et l'attribution y sont rangés à droite.

Le thème est construit sur la base de [Cartouche, barre verticale](../cartouche-vertical) (compatibilité 3.9,
popups, listes, messages), à laquelle s'ajoute la surcouche Bandeau en fin de `map.css`.

## Contenu

```
src/                         sources lisibles : c'est ici qu'on modifie
  main.css                   couleur de la collectivité, texte du pied de page, dimensions
  map.css                    base Cartouche, puis bloc « Bandeau : surcouche de la base Cartouche »
  media.css                  écrans tactiles et téléphones : bouton menu, tiroir, panneaux en feuille
media/themes/default/css/    fichiers générés, à installer (ne pas modifier à la main)
screenshots/                 aperçus
```

Après une modification dans `src/`, régénérer depuis la racine du dépôt :

```
python3 tools/build.py themes/bandeau
```

## Installation

1. Dans l'administration Lizmap, sur le dépôt visé, cocher **Autoriser les thèmes utilisateurs**.
2. Copier le dossier **généré** `media/themes/default/` (pas `src/`) dans le dossier `media/` du dépôt,
   ou un niveau au-dessus des dépôts pour l'appliquer à tous.
3. Droits : 755 pour les dossiers, 644 pour les fichiers.
4. Recharger la carte avec Ctrl+Maj+R : Lizmap sert ces CSS avec un cache d'un jour.

Archive prête à décompresser à la racine d'un dépôt : `python3 tools/build.py --zip themes/bandeau`.

## Personnaliser

### Couleur de la collectivité (`src/main.css`, `:root`)

| Variable | Rôle | Valeur |
|---|---|---|
| `--brand` | bandeau, titres de panneau, accent (cases cochées, boutons principaux) | `#1e4d8c` |
| `--brand-dark` | rail d'outils et contrôles de zoom (nuance plus foncée) | `#163b6c` |
| `--brand-soft` | outil ou bouton actif sur le rail et le zoom (nuance plus claire) | `#3a6fb5` |

Le texte du bandeau est blanc : choisir une couleur assez foncée pour qu'il reste lisible.
Les icônes du rail et du zoom sont blanches : `--brand-dark` doit rester foncée.

Pour un seul projet ou depuis l'administration (CSS additionnel) :
`:root:root { --brand: ...; --brand-dark: ...; --brand-soft: ...; }`.

### Pied de page

Le texte est dans la variable `--footer-text`, entre guillemets simples (Lizmap supprime les guillemets doubles).

- **Pour tous les projets du dépôt** : modifier `--footer-text` dans `src/main.css`, régénérer, réinstaller.
- **Pour un seul projet** : sans toucher au thème, créer dans le dépôt le fichier
  `media/themes/<nom du projet>/css/main.css` (même nom que le `.qgs`, sans l'extension) contenant :

  ```css
  :root:root { --footer-text: 'Donn\e9 es : DGFiP, IGN - R\e9 alisation : Geolab'; }
  ```

  Lizmap charge ce fichier après le thème du dépôt, uniquement pour ce projet.

Lettres accentuées : les écrire en code CSS (`\e0` = à, `\e9` = é, `\e8` = è, `\ea` = ê, `\e7` = ç).
Le code avale l'espace qui le suit : une espace pour coller la lettre suivante (`Donn\e9 es` donne « Données »),
deux espaces pour garder un vrai espace (`texte \e0  personnaliser`).
Pour masquer le pied de page : `--footer-text: '';` ne suffit pas, ajouter `#content::after { display: none; }`
et `--foot: 0px;`.

### Autres couleurs et dimensions

| Variable | Rôle | Valeur |
|---|---|---|
| `--c-ink` | texte (doit rester foncé) | `#1d2733` |
| `--c-paper` | panneaux, pied de page | `#ffffff` |
| `--c-mist` / `--c-rule` | survol / filets | `#eef2f7` / `#d7dee8` |
| `--bar` | hauteur du bandeau | `64px` |
| `--foot` | hauteur du pied de page | `30px` |
| `--dock-w` | largeur du panneau gauche (réduite sur petit écran, comme Cartouche) | `380px` |

## Logo

`Geolab-Logo-Verti-Noir.png`, sur une tuile blanche à gauche du bandeau. Pour le logo d'une collectivité :
remplacer le fichier dans `src/` (et le nom dans `map.css`, bloc « Logo Geolab »), puis régénérer.

## Téléphones et tablettes

Sur un écran tactile, Lizmap remplace la barre d'outils par un bouton menu et un tiroir latéral, quelle que soit la
largeur de l'écran. `media.css` (chargé par Lizmap après `map.css`) les habille aux couleurs du thème : outils en liste
avec leur nom, cibles de 48 px de haut, outil actif mis en évidence.

Sur un téléphone (écran tactile de moins de 900 px de large, seuil de l'affichage mobile de Lizmap, ou téléphone à l'horizontale) :
- en-tête : le bandeau passe sur deux lignes : bouton menu, logo, titre et compte, puis la recherche sur toute la largeur. Le pied de page tient sur une ligne, tronquée.
- boutons de compte réduits à leur icône ; champ de recherche en 16 px (le téléphone ne zoome pas à la saisie) ;
- panneaux (couches, popup, filtre, données) et mini-panneaux (mesure, impression...) en feuille depuis le bas de l'écran :
  la carte reste visible au-dessus ;
- vue d'ensemble et coordonnées masquées.

Sur ordinateur, `media.css` n'a aucun effet (vérifié : captures identiques avec et sans).

## Limites connues

- Affichage tactile vérifié en émulation sur Lizmap 3.9.6 (téléphone 390 × 844 et 844 × 390, tablette 1024 × 768), pas encore sur un vrai téléphone ni en 3.10.
- Testé uniquement en **Lizmap 3.9** (dépôt de test local), en desktop, déconnecté.
  **Non testé connecté**, ni en 3.10, ni en affichage mobile.
- Les infobulles des outils du rail sont celles de Lizmap : pas de libellés visibles.
- **Polices** chargées depuis Google Fonts (Source Sans 3, IBM Plex Mono) : à héberger localement
  pour éviter tout appel externe (RGPD, réseau fermé).
- Sélecteurs `:has()` utilisés (Chrome 105+, Firefox 121+, Safari 15.4+).
- Page d'accueil non concernée : Lizmap n'applique les thèmes du dossier `media` qu'aux pages carte.
