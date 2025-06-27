import yaml, html, sys

d = yaml.safe_load(open("data/books.yml"))

print("flowchart TD")
for n in d["nodes"]:
    label = (
        f"<a href='{n['href']}' class='book-node'>"
        f"{html.escape(n['label'])}</a>"
    )
    print(f"    {n['id']}[\"{label}\"]")

for e in d["edges"]:
    lvl  = f"×{e.get('level')}" if e.get("level", 1) > 1 else ""
    text = html.escape(f"{e['trait']}{lvl}")
    print(f"    {e['from']} --|{text}| {e['to']}")
