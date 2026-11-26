# Thèmes CSS pour Lizmap

Thèmes CSS prêts à installer pour les pages carte de [Lizmap Web Client](https://github.com/3liz/lizmap-web-client).
Chaque thème a son propre dossier, avec un aperçu, une fiche descriptive et les fichiers à copier dans le dossier
`media/` d'un dépôt Lizmap.

Documentation Lizmap sur les thèmes : https://docs.lizmap.com/current/fr/publish/customization/themes.html

## Catalogue

<!-- Tableau généré à partir des en-têtes des README des thèmes : python3 tools/check.py --catalog -->
<!-- catalog:start -->
| Aperçu | Thème | Lizmap | Version | Auteur |
|---|---|---|---|---|
| <img src="themes/bandeau/screenshots/desktop.png" width="240"> | [Bandeau](themes/bandeau)<br>Aux couleurs d'une collectivité. Bandeau du haut en couleur pleine avec logo, titre et recherche, rail d'outils dans la même couleur, panneau collé au rail, pied de page pour les sources et mentions. | 3.9 | 1.1.0 | arno974 (Geolab) |
| <img src="themes/cartouche-horizontal/screenshots/desktop.png" width="240"> | [Cartouche, barre horizontale](themes/cartouche-horizontal)<br>Carte plein écran, titre du projet dans un cartouche, barre d'outils horizontale sous le titre, recherche et connexion à droite. | 3.9, 3.10 | 1.1.0 | arno974 (Geolab) |
| <img src="themes/cartouche-vertical/screenshots/desktop.png" width="240"> | [Cartouche, barre verticale](themes/cartouche-vertical)<br>Carte plein écran, titre du projet dans un cartouche, barre d'outils verticale à gauche, recherche au centre. | 3.9, 3.10 | 1.1.0 | arno974 (Geolab) |
| <img src="themes/focus/screenshots/desktop.png" width="240"> | [Focus](themes/focus)<br>La carte d'abord. Au repos, quelques pastilles rondes ; le menu s'ouvre en liste d'outils au survol, la loupe s'allonge en champ de recherche, les panneaux sont des cartes flottantes. | 3.9 | 1.1.0 | arno974 (Geolab) |
| <img src="themes/net/screenshots/desktop.png" width="240"> | [Net](themes/net)<br>Sobre et lisible. Barre de titre blanche pleine largeur avec la recherche au centre, colonne d'outils toujours affichée avec leur nom, panneau collé à la colonne. | 3.9 | 1.1.0 | arno974 (Geolab) |
| <img src="themes/tiroir/screenshots/desktop.png" width="240"> | [Tiroir](themes/tiroir)<br>Clair, façon carte papier. Rail d'outils fin qui s'ouvre en tiroir au survol avec les libellés, panneau collé au rail sur toute la hauteur, titre de carte en bas à gauche. | 3.9 | 1.1.0 | arno974 (Geolab) |
<!-- catalog:end -->

## Versions de Lizmap

L'interface de Lizmap change d'une version à l'autre : un thème n'est garanti que sur les versions indiquées
dans sa fiche (champ `lizmap`), qui sont celles sur lesquelles il a réellement été testé.

## Installer un thème

1. Dans l'administration Lizmap, sur le dépôt visé, cocher **Autoriser les thèmes utilisateurs**.
2. Copier le dossier `media/themes/default/` du thème dans le dossier `media/` du dépôt
   (ou dans `media/themes/<nom_du_projet>/` pour un seul projet).
3. Recharger la carte avec Ctrl+Maj+R.

Le README de chaque thème détaille l'installation et la personnalisation.

## Organisation du dépôt

```
themes/<nom>/
  README.md                  fiche du thème : en-tête descriptif, puis explications
  screenshots/               aperçus (desktop.png obligatoire)
  src/                       sources CSS lisibles : c'est ici qu'on modifie
  media/themes/default/css/  fichiers générés, à installer (ne pas modifier à la main)
tools/
  build.py                   génère media/ à partir de src/, et l'archive .zip
  check.py                   vérifie les thèmes et met à jour le catalogue ci-dessus
```

### Pourquoi une étape de génération

Lizmap sert les CSS du dossier `media` via `view~media:getCssFile`, qui modifie le fichier à la volée :
- il réécrit chaque `url(...)` en lien vers le dossier media, ce qui casse l'`@import` des polices et les icônes SVG intégrées ;
- il supprime tous les guillemets doubles, ce qui casse `content: ""` et les data URI.

`tools/build.py` produit donc des fichiers avec uniquement des guillemets simples, un `@import '...'` sans `url(`,
et des icônes écrites `u\rl(...)` (échappement CSS valide, ignoré par la réécriture). Il copie aussi les images
de `src/` (logo) à côté des CSS, et s'arrête si un `url(...)` risque d'être cassé.

```
python3 tools/build.py                          # tous les thèmes
python3 tools/build.py themes/<nom>             # un thème
python3 tools/build.py --zip themes/<nom>       # + dist/lizmap-theme-<nom>-<version>.zip
python3 tools/check.py                          # vérifications
python3 tools/check.py --catalog                # régénère le catalogue
```

Python 3 seul suffit, sans dépendance.

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[Mozilla Public License 2.0](LICENSE), sauf mention contraire dans la fiche d'un thème.
