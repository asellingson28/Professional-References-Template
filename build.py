# This project uses only Python standard library modules.
# No requirements.txt is needed.

import subprocess
from pathlib import Path

tex_file = Path("references.tex")  # your .tex file

# Run pdflatex in the directory where the .tex file lives
result = subprocess.run(
    ["pdflatex", "-interaction=nonstopmode", tex_file.name],
    cwd=tex_file.parent,
    capture_output=True,
    text=True,
)

if result.returncode != 0:
    print("LaTeX compile failed!\n")
    print(result.stdout)
    print(result.stderr)
    raise SystemExit(result.returncode)

pdf_file = tex_file.with_suffix(".pdf")
print(f"Built: {pdf_file.resolve()}")
