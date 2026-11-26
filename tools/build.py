#!/usr/bin/env python3
"""Genere des CSS compatibles avec view~media:getCssFile de Lizmap.

getCssFile (modules/view/controllers/media.classic.php) :
  - reecrit chaque `url(...)` en `url(<getMedia>/...)`  -> casse @import et data URI ;
  - supprime tous les guillemets doubles               -> casse content: "" et les data URI.
On produit donc : guillemets simples partout, @import sans url(),
et `u\\rl(...)` (echappement CSS valide) que l'expression reguliere ne reconnait pas.
Les images relatives (url(logo.png)) restent telles quelles : getCssFile les sert via getMedia.

Usage :
  python3 tools/build.py                       tous les themes de themes/
  python3 tools/build.py themes/<nom>          un theme
  python3 tools/build.py --zip themes/<nom>    genere puis cree dist/lizmap-theme-<nom>-<version>.zip
"""
import re, sys, pathlib, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES = ROOT / 'themes'
OUT = pathlib.Path('media/themes/default/css')
IMAGES = ('.png', '.svg', '.jpg', '.jpeg', '.webp', '.gif')


def media_safe(css: str) -> str:
    # @import url("x") -> @import 'x'
    css = re.sub(r'@import\s+url\(\s*"([^"]+)"\s*\)', r"@import '\1'", css)
    # url("data:...") -> u\rl('data:...') avec les ' internes encodes
    def data_uri(m):
        return "u\\rl('" + m.group(1).replace("'", "%27") + "')"
    css = re.sub(r'url\(\s*"(data:[^"]+)"\s*\)', data_uri, css)
    # tout autre guillemet double -> simple (font-family, content, selecteurs)
    css = css.replace('"', "'")
    # Seules les images relatives (ex. url(logo.png)) peuvent rester en url( :
    # getCssFile les reecrit justement vers getMedia. Le reste casserait.
    for m in re.finditer(r'(?<!\\)url\(([^)]*)\)', css):
        target = m.group(1).strip()
        if re.match(r"^['\"]|^(https?:|data:|//)", target):
            raise SystemExit('url(' + target[:40] + ') serait casse par getCssFile')
    return css


SOURCE_HEADER = re.compile(r'\A/\* SOURCE .*?\*/\n', re.S)
GENERATED_HEADER = ('/* FICHIER GENERE par tools/build.py depuis src/{name} : c est ce fichier qu on installe dans Lizmap.\n'
                    '   Ne pas le modifier a la main : modifier src/{name} puis relancer le build. */\n')


def outputs(theme: pathlib.Path) -> dict:
    """Fichiers a installer : {chemin relatif au theme: contenu en octets}."""
    src = theme / 'src'
    files = {}
    for f in sorted(src.glob('*.css')):
        css = SOURCE_HEADER.sub('', f.read_text())  # l'avertissement des sources ne doit pas etre installe
        files[OUT / f.name] = (GENERATED_HEADER.format(name=f.name) + media_safe(css)).encode()
    # Images referencees en relatif par les CSS (logo...) : copiees a cote
    for f in sorted(p for p in src.iterdir() if p.suffix.lower() in IMAGES):
        files[OUT / f.name] = f.read_bytes()
    return files


def stale(theme: pathlib.Path) -> list:
    """Fichiers generes absents, differents de src/, ou en trop."""
    expected = outputs(theme)
    problems = [str(p) for p, data in expected.items()
                if not (theme / p).is_file() or (theme / p).read_bytes() != data]
    out = theme / OUT
    if out.is_dir():
        problems += [str(OUT / f.name) + ' (absent de src/)'
                     for f in sorted(out.iterdir()) if OUT / f.name not in expected]
    return problems


def build(theme: pathlib.Path):
    for path, data in outputs(theme).items():
        (theme / path).parent.mkdir(parents=True, exist_ok=True)
        (theme / path).write_bytes(data)
        print('ok', theme.name / path)


def package(theme: pathlib.Path):
    sys.path.insert(0, str(ROOT / 'tools'))
    from check import read_front_matter
    version = read_front_matter(theme / 'README.md').get('version', '0')
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    archive = dist / f'lizmap-theme-{theme.name}-{version}.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted((theme / 'media').rglob('*')):
            if f.is_file():
                z.write(f, f.relative_to(theme))
    print('ok', archive.relative_to(ROOT))


if __name__ == '__main__':
    args = sys.argv[1:]
    make_zip = '--zip' in args
    args = [a for a in args if a != '--zip']
    themes = [pathlib.Path(a).resolve() for a in args] or \
        sorted(d for d in THEMES.iterdir() if (d / 'src').is_dir())
    for theme in themes:
        build(theme)
        if make_zip:
            package(theme)
