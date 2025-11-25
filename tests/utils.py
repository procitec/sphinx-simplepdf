import re
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup

# ANSI_ESCAPE_RE = re.compile(r'\x1b\\[[;?0-9]*[A-Za-z]?')
#
# def strip_ansi(text):
#     return ANSI_ESCAPE_RE.sub('', text)

def extract_pdf_text(pdf_path):
    """Extrahiere gesamten Text aus PDF."""
    return extract_text(str(pdf_path))


def prettify_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return str(soup.prettify(formatter="html"))


def build_and_capture_stdout(sphinx_build, capsys, srcdir, build_kwargs=None, **sphinx_kwargs):
    """Baue das PDF und liefere das captured stdout zurück."""
    build_kwargs = build_kwargs or {}
    result = sphinx_build(srcdir=srcdir, **sphinx_kwargs).build(**build_kwargs)
    captured = capsys.readouterr()
    result.warnings += captured.out.splitlines()
    return result
