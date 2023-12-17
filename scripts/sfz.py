import re
import yaml

opcodes = set() # "primary" opcodes only, not the full list
aliases = []
mods_cc = []
mods_vl = []
current_opcode = None

def process_opcode(obj, isPrimary=False):
  global current_opcode, opcodes, aliases, mods_cc, mods_vl
  if isPrimary:
    current_opcode = re.sub(r"\W+", '', obj['name'])
    opcodes.add(current_opcode)
  for a in obj.get('alias', []):
    process_opcode(a)
    aliases += [(a['name'], current_opcode)]
  for m in obj.get('modulation', {}).get('midi_cc', []):
    process_opcode(m)
    mods_cc += [(m['name'], current_opcode)]
  for v in obj.get('modulation', {}).get('velocity', []):
    process_opcode(v)
    mods_vl += [(v['name'], current_opcode)]

def process(data):
  if isinstance(data, dict):
    for k, v in data.items():
      if k == 'opcodes':
        for o in v:
          process_opcode(o, True)
      else:
        process(v)
  elif isinstance(data, list):
    for v in data:
      process(v)

def process_data():
  with open('data/sfz/syntax.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    process(data)

def get_all_opcodes():
  process_data()
  all_opcodes = list(opcodes)
  [all_opcodes.append(alias) for alias, main in aliases]
  [all_opcodes.append(cc)    for cc,    main in mods_cc]
  [all_opcodes.append(vel)   for vel,   main in mods_vl]
  print('\n'.join([x for x in all_opcodes]))
  #return all_opcodes

def prnt(s:str):
  return s
