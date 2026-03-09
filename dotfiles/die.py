#!/usr/bin/python3

import sys, os, subprocess, json, argparse, pathlib, shutil, re, code

#a = sys.argv[1]
conf = "/home/ff3/git/pigeon/dotfiles/conf.json"

def getjson(conf=conf):
	global storage, root, stored, rules
	with open(conf) as f:
		jason=json.load(f)
	storage = os.path.abspath(os.path.expanduser(jason["storage"]))
	root = os.path.abspath(os.path.expanduser(jason["root"]))
	stored = jason["stored"]
	rules = jason["rules"]
	return [storage, root, stored, rules]
getjson()

"""
# there shouldn't be children of certain saved directories anyways
def fixjson(jasonstored):
	for i in range(len(jasonstored)):
		for j in range(len(jasonstored)-1-i):
			if len(jasonstored[j]) > len(jasonstored[j+1]):
				jasonstored[j], jasonstored[j+1] = jasonstored[j+1], jasonstored[j]
"""
def verbosemsg(msg, verbose):
	if verbose: print(msg); return 1
	return 0
def copytree(src, dst, *v, **k):
	if os.path.isdir(src):
		shutil.copytree(src, dst, *v, **k)
	else:
		os.makedirs(os.path.dirname(dst), exist_ok=True)
		shutil.copy2(src, dst, *v)
def rmtree(src, *v, **k):
	if os.path.isdir(src):
		shutil.rmtree(src, *v, **k)
	else:
		os.remove(src, *v, **k)
def restore(version, verbose=False):
	if not version[0] == "/":
		version = os.path.join(storage, version)
	version = os.path.abspath(version)
	rt = os.path.join(version, "root")
	with open(os.path.join(version, "conf.json")) as f:
		njason = json.load(f)
	nstored = njason["stored"]
	nrules = njason["rules"]
	for store, rule in nrules.items():
		for i in os.listdir(os.path.join(root, store)):
			if re.search(rule, i):
				nstored.append(os.path.join(store, i)) # rel
	for store in nstored:
		rootstore = os.path.join(root, store)
		if os.path.exists(rootstore): rmtree(rootstore)
		copytree(os.path.join(rt, store), rootstore)
	verbosemsg("restore done", verbose)
def save(name, delete=False, verbose=False):
	nstored = stored.copy()
	rt = os.path.abspath(os.path.join(storage, name, "root"))
	if delete and os.path.exists(rt):
		shutil.rmtree(rt)
	os.makedirs(rt) # crash if already saved and not delete
	shutil.copy(conf, os.path.join(rt, ".."))
	for store, rule in rules.items():
		for i in os.listdir(os.path.join(root, store)):
			if re.search(rule, i):
				nstored.append(os.path.join(store, i))
	for store in nstored:
		#os.system(f"mkdir -p {rt}/{store} 2>/dev/null")
		copytree(os.path.join(root, store), os.path.join(rt, store), dirs_exist_ok=True)
	verbosemsg("save done", verbose)
def delete(version, verbose=False):
	try:
		shutil.rmtree(os.path.join(storage, version))
	except:
		return "does not exist"
	verbosemsg("delete done", verbose)
def ls(*v, **k):
	lst = os.listdir(storage)
	return print(lst)

def cmd(argval, python=False, interact=False, *v, **k):
#	print(argval)
	if python:
		return exec(' '.join(argval[0:]))
	argval = argval + list(v) + [f"{i}={j}" for i, j in k.items()]
	argv = [*argval[:1]]
	for i in argval[1:]:
		try:
			exec(f"(lambda x: x)({i})") # can be used in func
			
		except:
			if re.search(rf"^\D+?=.+?$", i): # its a kwarg
				i = i.split("=")
				i[1] = "\"" + i[1].replace('"', r'\"') + "\""
				i = "=".join(i)
			else:
				i = "\"" + i.replace('"', r'\"') + "\""
			argv.append(i)
#	print(argv)
	exec(f"{argv[0]}({','.join(argv[1:])})")
	if interact:
		code.interact(local=dict(globals(), **locals()))

p = argparse.ArgumentParser()
p.add_argument("-p", "--python", action="store_true")
p.add_argument("-i", "--interact", action="store_true")
p.add_argument("-v", "--verbose", action="store_true")
args, argv=p.parse_known_args()
cmd(argv, python=args.python, interact=args.interact, verbose=args.verbose)



