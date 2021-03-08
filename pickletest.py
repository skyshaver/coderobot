import pickledb
import code_snippets as cs


db = pickledb.load('snippets.db', False)

for key, value in cs.snippets.items():
    db.set(key, value)
        
db.dump()
# cinval = db.get("cin")
# print(cinval)