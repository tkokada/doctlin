"""Generate the code reference pages and navigation."""

from pathlib import Path
from os.path import exists
from griffe.loader import GriffeLoader

import mkdocs_gen_files

griffe = GriffeLoader()
nav = mkdocs_gen_files.Nav()


def add(module):
    for member, item in module.members.items():
        if member in ['migrations']:
            # avoiding unwanted modules
            continue
        item_path = item._filepath

        if '__init__.py' in str(item_path):
            # adding submodule
            add(item)
            continue

        doc_path = item_path.with_suffix(".md")
        full_doc_path = Path("reference", doc_path)

        parts = tuple(item_path.with_suffix("").parts)

        nav[parts] = str(doc_path)

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            fd.write(f"::: {ident}")

        mkdocs_gen_files.set_edit_path(full_doc_path, path)


for path in sorted(Path('').iterdir()):
    if not path.is_dir():
        # skip files
        continue
    if not exists(path / '__init__.py'):
        # skip simple directories
        continue

    module = griffe.load_module(path)
    add(module)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
