import re 
vals = {"z" : "a",  "g" : "t", "t" : "g", "x" : "c" }
pattern = (r'[0-9]+[zgtx]|[zgtx]')
matches = re.findall(pattern, message)
return "".join([vals[p] if len(p) == 1 else int(re.findall(r'[0-9]+', p)[0])*vals[re.findall(r'[zgtx]', p)[0]] for p in matches])

"100% solution"
