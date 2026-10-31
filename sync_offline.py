from pathlib import Path
r = Path(__file__).resolve().parent
assets = r.parent / "app/src/main/assets"
if not assets.is_dir():
    raise SystemExit("Place this repository in the Draw Music Android project first.")
css = (r / "styles.css").read_text()
for source, target in (("index.html", "privacy-local.html"), ("terms.html", "terms-local.html")):
    content = (r / source).read_text().replace('<link rel="stylesheet" href="styles.css">', '<style>' + css + '</style>')
    content = content.replace('href="index.html"', 'href="privacy-local.html"').replace('href="terms.html"', 'href="terms-local.html"')
    (assets / target).write_text(content)
    print("Updated", target)
