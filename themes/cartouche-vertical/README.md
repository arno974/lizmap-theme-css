---
title: Cartouche, barre verticale
description: Carte plein écran, titre du projet dans un cartouche, barre d'outils verticale à gauche, recherche au centre.
author: arno974 (Geolab)
created: 2026-10-15
updated: 2026-11-02
version: 1.1.0
lizmap: 3.9, 3.10
license: MPL-2.0
preview: screenshots/desktop.png
mobile: non testé
external_resources: Google Fonts
tags: plein écran, barre verticale, cartouche, couleurs personnalisables
---

# Cartouche, barre verticale

Carte plein écran, instruments flottants, titre du projet dans un cartouche en tête de colonne.
La barre d'outils est verticale, à gauche ; la recherche est au centre de la ligne du haut.

![Aperçu](screenshots/desktop.png)

Variante : [Cartouche, barre horizontale](../cartouche-horizontal).

## Contenu

```
src/                         sources lisibles : c'est ici qu'on modifie
  main.css                   polices, tokens (couleurs, rayons, marges), boutons et champs
  map.css                    interface carte, puis bloc « Compatibilité Lizmap 3.9 »
  media.css                  écrans tactiles et téléphones : bouton menu, tiroir, panneaux en feuille
media/themes/default/css/    fichiers générés, à installer (ne pas modifier à la main)
screenshots/                 aperçus
```

Après une modification dans `src/`, régénérer depuis la racine du dépôt :

```
python3 tools/build.py themes/cartouche-vertical
```

Pourquoi cette étape : voir le [README racine](../../README.md#pourquoi-une-étape-de-génération).

Ce thème est une **surcouche** : Lizmap charge ces fichiers après le thème par défaut de l'instance
(voir `modules/view/controllers/lizMap.classic.php`). Il ne remplace donc ni les images ni les sprites d'icônes.

## Installation

1. Dans l'administration Lizmap, sur le dépôt visé, cocher **Autoriser les thèmes utilisateurs** (`allowUserDefinedThemes`).
2. Copier le dossier `media/themes/default/` dans le dossier `media/` du dépôt :
   - `media/themes/default/` : appliqué à tous les projets du dépôt ;
   - `media/themes/<nom_du_projet>/` : appliqué à un seul projet ;
   - `media/themes/default/` placé un niveau au-dessus des dépôts : appliqué à tous les dépôts.
3. Droits : 755 pour les dossiers, 644 pour les fichiers.
4. Recharger la carte avec Ctrl+Maj+R : Lizmap sert ces CSS avec un cache d'un jour.

Pour obtenir une archive prête à décompresser à la racine d'un dépôt :
`python3 tools/build.py --zip themes/cartouche-vertical` (crée `dist/lizmap-theme-cartouche-vertical-<version>.zip`).

Documentation : https://docs.lizmap.com/current/fr/publish/customization/themes.html

## Personnaliser

### Les couleurs : deux variables

Toute la palette est dérivée de **deux couleurs**, en tête de `src/main.css` :

```css
--c-ink: #14212b;     /* couleur foncée : rail, contrôles, cartouche, texte */
--c-accent: #0a6e8a;  /* accent : état actif, liens, focus, boutons principaux */
```

Les teintes secondaires (survol, filets, texte secondaire) en sont calculées avec `color-mix()`, et les icônes
(loupe, chevrons, croix, flèches) sont des masques colorés par ces variables : tout suit.
`--c-ink` doit rester **foncée** : les icônes du rail et des contrôles sont des images blanches.

Exemples testés : vert `#163a2b` / `#2f855a`, bleu `#1b2a4a` / `#2563c9`.

Trois façons de changer les couleurs, **sans régénérer** pour les deux dernières :

1. Dans `src/main.css`, puis `python3 tools/build.py themes/cartouche-vertical` : change la valeur par défaut du thème.
2. Pour **un seul projet** : créer `media/themes/<nom_du_projet>/css/main.css` contenant uniquement
   ```css
   :root:root { --c-ink: #163a2b; --c-accent: #2f855a; }
   ```
   Lizmap le charge après le thème `default`.
3. Dans l'administration Lizmap, *Thème* > CSS additionnel, la même ligne `:root:root { ... }`.
   Le double `:root` est nécessaire : ce CSS est chargé **avant** le thème, il doit donc être plus spécifique.

Les couleurs des messages (succès, avertissement, erreur) restent fixes : elles ont un sens propre.

### Autres variables (`src/main.css`, `:root`)

| Variable | Rôle | Valeur |
|---|---|---|
| `--r` / `--r-sm` | rayons panneaux / contrôles | `6px` / `4px` |
| `--pad` / `--pad-sm` | marges intérieures panneaux / mini-panneaux | `18px` / `14px` |
| `--dock-w` | largeur du panneau gauche (fixe, quel que soit le contenu) | `420px` |

## Logo

Le logo est le fichier `Geolab-Logo-Verti-Noir.png`, placé à côté des CSS et référencé en relatif dans `map.css`
(bloc « Logo Geolab »). Pour en changer : remplacer le fichier dans `src/` (et le nom dans `map.css` si besoin),
puis régénérer : les images de `src/` sont copiées avec les CSS.

## Téléphones et tablettes

Sur un écran tactile, Lizmap remplace la barre d'outils par un bouton menu et un tiroir latéral, quelle que soit la
largeur de l'écran. `media.css` (chargé par Lizmap après `map.css`) les habille aux couleurs du thème : outils en liste
avec leur nom, cibles de 48 px de haut, outil actif mis en évidence.

Sur un téléphone (écran tactile de moins de 900 px de large, seuil de l'affichage mobile de Lizmap, ou téléphone à l'horizontale) :
- en-tête : en haut, le bouton menu, le cartouche (titre seul) et le bouton de compte ; dessous, la recherche sur toute la largeur.
- boutons de compte réduits à leur icône ; champ de recherche en 16 px (le téléphone ne zoome pas à la saisie) ;
- panneaux (couches, popup, filtre, données) et mini-panneaux (mesure, impression...) en feuille depuis le bas de l'écran :
  la carte reste visible au-dessus ;
- vue d'ensemble et coordonnées masquées.

Sur ordinateur, `media.css` n'a aucun effet (vérifié : captures identiques avec et sans).

## Limites connues

- **Polices** chargées depuis Google Fonts (Archivo, IBM Plex Sans, IBM Plex Mono). Pour éviter tout appel externe (RGPD, réseau fermé), les héberger localement et remplacer l'`@import` en tête de `main.css`.
- **Page d'accueil** non concernée : Lizmap n'applique les thèmes du dossier `media` qu'aux pages carte.
- **Icônes** : sprites PNG du thème par défaut, à couleur figée. C'est pourquoi le rail et les contrôles de carte restent sombres.
- **Petits écrans d'ordinateur** (souris, pas d'écran tactile) : la recherche se place entre le cartouche et les boutons de compte et se rétrécit (180 px au minimum) ; le panneau gauche passe de 420 à 360 px sous 1100 px, puis à 320 px sous 1000 px. Testé de 1534 à 900 px, déconnecté et connecté en administrateur (en 3.9, Lizmap passe en affichage mobile sous 900 px).
- Place réservée aux boutons de compte (`--auth-w`) : 150 px pour un bouton (Connexion ou utilisateur), 290 px pour deux (Administration + utilisateur). L'identifiant est tronqué au-delà de 80 px, le nom complet reste en infobulle.
- Sélecteurs `:has()` utilisés (navigateurs récents : Chrome 105+, Firefox 121+, Safari 15.4+).
- Compatible **Lizmap 3.10** (projet de démonstration « Montpellier - Transports ») et **Lizmap 3.9**, en desktop. Affichage tactile vérifié en émulation sur Lizmap 3.9.6 (téléphone 390 × 844 et 844 × 390, tablette 1024 × 768), pas encore sur un vrai téléphone ni en 3.10.
- En 3.9, les règles spécifiques ne s'activent qu'en présence de `#dock-tabs` (titre de panneau sous forme d'onglet) : elles sont sans effet en 3.10.
- 3.9 : si des composants web (`lizmap-navbar`, `lizmap-overviewmap`...) ne sont pas définis par le JavaScript de l'instance, le thème masque leurs boîtes vides (zoom, vue d'ensemble) au lieu d'afficher des cartes blanches.
- 3.9 : structures différentes prises en charge par le thème : `#dock-tabs` (titre de panneau), `#mini-dock > .tabbable` (mini-panneaux), `ul.nav` (menu de compte Bootstrap 2), `#message` centré par marge négative, `#liz_layer_popup` affichée vide, `h3` imbriqués dans les mini-panneaux, composants web `inline` (sélection, géolocalisation).
