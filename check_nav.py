import os, re
path = r'C:\Users\dasku\OneDrive\Documents\GitHub\veritas-hospitality-advisors-site'
for fn in ['index.html','founder.html','clients.html','diagnostic.html','insights.html','legal.html']:
    fp = os.path.join(path, fn)
    if not os.path.exists(fp):
        print(fn + ': FILE MISSING'); continue
    txt = open(fp, encoding='utf-8', errors='ignore').read()
    nav_m = re.search(r'<nav[^>]*>(.*?)</nav>', txt, re.DOTALL)
    if nav_m:
        nav = nav_m.group(1).replace('\n',' ').strip()[:300]
        print(fn + ':\n  ' + nav + '\n')
    else:
        print(fn + ': NO NAV FOUND\n')
