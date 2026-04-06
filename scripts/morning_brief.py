#!/usr/bin/env python3
from pathlib import Path
import datetime

def summarize_unit(unit_dir, date):
    md=unit_dir / 'SUMMARY.md'
    um=unit_dir / 'UNIT_MAP.md'
    if um.exists():
        text=um.read_text()
        # naive: find Day matching date or Day 7 pattern; here we return first 2 lines
        return '\n'.join(text.splitlines()[:3])
    if md.exists():
        return md.read_text()
    # fallback: list files
    files=[p.name for p in unit_dir.glob('*') if p.is_file()]
    return 'Files: ' + ', '.join(files)

base=Path('/home/mcclurgbm/.openclaw/workspace')
classes={'Engineering':base/'engineering/Engineering Unit Maps/04 Structures',
         'Chemistry':base/'chemistry',
         'Physics':base/'physics'}

today=datetime.date.today()
out=[]
out.append(f"Morning brief for {today.isoformat()}")
for name,path in classes.items():
    out.append(f"\n**{name}**")
    summary=summarize_unit(path, today)
    out.append(summary)

# write brief file
brief_dir=base/'briefs'
brief_dir.mkdir(exist_ok=True)
fn=brief_dir/f"brief-{today.isoformat()}.md"
fn.write_text('\n'.join(out))
print(fn)
