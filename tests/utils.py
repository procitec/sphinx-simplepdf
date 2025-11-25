from pdfminer.high_level import extract_text

def extract_pdf_text(pdf_path):
    """Extrahiere gesamten Text aus PDF."""
    return extract_text(str(pdf_path))



def build_and_capture_stdout(sphinx_build, capsys, srcdir, **kwargs):
    """Baue das PDF und liefere das captured stdout zurück."""
    result = sphinx_build(srcdir=srcdir, **kwargs).build()
    captured = capsys.readouterr()
    result.warnings = captured.out.splitlines()
    return result
