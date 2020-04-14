name={"name":"Osama","Class":12,"Chapter":"Physics"}
print(name)
print(name["Class"])
for a in name.values():
	print(a)
for a in name.keys():
	print(a)
for a in name.items():
	print(a)
for a,b in name.items():
	print(a,b)
if "name" in name:
	print("Name")
if "Osama" in name.values():
	print("Osama")
name.clear()
print(name)
name={"name":"Osama","Class":12,"Chapter":"Physics"}
c=name.copy()
print(c)
print(c.get("name"))
name.fromkeys(['ok'],'when')
print(name)