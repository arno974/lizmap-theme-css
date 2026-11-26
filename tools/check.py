#!/usr/bin/env python3
"""Verifie les themes de themes/ et met a jour le catalogue du README racine.

Pour chaque theme :
  - en-tete du README present, avec les champs obligatoires ;
  - image d'apercu presente ;
  - fichiers generes (media/) a jour par rapport a src/.
Puis le tableau du README racine, entre les balises catalog, doit correspondre aux en-tetes.

Usage :
  python3 tools/check.py            verifie (code de sortie 1 en cas d'erreur)
  python3 tools/check.py --catalog  reecrit le catalogue du README racine, puis verifie
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES = ROOT / 'themes'
REQUIRED = ('title', 'description', 'author', 'created', 'version', 'lizmap', 'license', 'preview')
START, END = '<!-- catalog:start -->', '<!-- catalog:end -->'


def read_front_matter(readme: pathlib.Path) -> dict:
    """En-tete `cle: valeur` entre deux lignes `---` en tete du fichier."""
    lines = readme.read_text().splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    meta = {}
    for line in lines[1:]:
        if line.strip() == '---':
            return meta
        key, sep, value = line.partition(':')
        if sep and key.strip():
            meta[key.strip()] = value.strip()
    return {}  # en-tete non ferme


def themes():
    return sorted(d for d in THEMES.iterdir() if d.is_dir() and not d.name.startswith(('.', '_')))


def check_theme(theme: pathlib.Path) -> list:
    sys.path.insert(0, str(ROOT / 'tools'))
    from build import stale
    readme = theme / 'README.md'
    if not readme.is_file():
        return ['README.md absent']
    meta = read_front_matter(readme)
    if not meta:
        return ["README.md sans en-tete (lignes '---' en tete du fichier)"]
    errors = [f'champ obligatoire vide ou absent : {k}' for k in REQUIRED if not meta.get(k)]
    if meta.get('preview') and not (theme / meta['preview']).is_file():
        errors.append(f"image d'apercu absente : {meta['preview']}")
    for d in ('created', 'updated'):
        if meta.get(d) and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', meta[d]):
            errors.append(f'{d} : format attendu AAAA-MM-JJ')
    if not (theme / 'src').is_dir():
        errors.append('dossier src/ absent')
    else:
        errors += [f'genere pas a jour, lancer tools/build.py : {p}' for p in stale(theme)]
    return errors


def catalog() -> str:
    rows = ['| Aperçu | Thème | Lizmap | Version | Auteur |', '|---|---|---|---|---|']
    for theme in themes():
        m = read_front_matter(theme / 'README.md') if (theme / 'README.md').is_file() else {}
        path = f'themes/{theme.name}'
        img = f'<img src="{path}/{m["preview"]}" width="240">' if m.get('preview') else '-'
        title = f'[{m.get("title", theme.name)}]({path})<br>{m.get("description", "")}'
        rows.append(f'| {img} | {title} | {m.get("lizmap", "-")} | {m.get("version", "-")} | {m.get("author", "-")} |')
    return '\n'.join(rows)


def with_catalog(text: str) -> str:
    before, _, rest = text.partition(START)
    _, _, after = rest.partition(END)
    return f'{before}{START}\n{catalog()}\n{END}{after}'


if __name__ == '__main__':
    readme = ROOT / 'README.md'
    text = readme.read_text()
    if START not in text or END not in text:
        sys.exit(f'README.md racine : balises {START} et {END} absentes')
    if '--catalog' in sys.argv:
        readme.write_text(with_catalog(text))
        text = readme.read_text()
        print('ok catalogue mis a jour')

    failed = False
    for theme in themes():
        errors = check_theme(theme)
        print(('ERREUR ' if errors else 'ok ') + theme.name)
        for e in errors:
            print('   -', e)
        failed |= bool(errors)
    if with_catalog(text) != text:
        print('ERREUR catalogue du README racine pas a jour, lancer : python3 tools/check.py --catalog')
        failed = True
    sys.exit(1 if failed else 0)
