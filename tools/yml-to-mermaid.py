import yaml, html, sys
d = yaml.safe_load(open('data/books.yml'))
print('flowchart TD')
for n in d['nodes']:
    label = f"<a href='{n['href']}' class='book-node'>{html.escape(n['label'])}</a>"
    print(f"    {n['id']}[\"{label}\"]")
for e in d['edges']:
    lvl = f"×{e['level']}" if e.get('level',1) > 1 else ''
    txt = html.escape(f"{e['trait']}{lvl}")
    print(f"    {e['from']} --|{txt}| {e['to']}")
