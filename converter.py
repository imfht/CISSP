from pathlib import Path
import os

work_dir = Path.cwd()

export_pdf_dir = work_dir / 'pdf'
if not export_pdf_dir.exists():
    export_pdf_dir.mkdir()

for md_file in list(work_dir.glob('*.md')):
    md_file_name = md_file.name.split('/')[-1]
    cmd = "docker run --rm -v $(pwd):/data lwabish/mdout:chinese \"{}\"".format(md_file_name, )
    print(cmd)
    os.system(cmd)
