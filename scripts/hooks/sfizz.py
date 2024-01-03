

def get_opcode_url_as_html(opcode):
  if "url" in opcode:
    return '<a href="' + opcode.url + '">'+ opcode["name"] + '</a>'

  opcode_name = opcode["name"].replace('#', '').replace('*', '')
  return '<a href="https://sfzformat.com/opcodes/' + opcode_name + '">' + opcode["name"] + '</a>'

def emoji_name_from_opcode(opcode):
  if not opcode:
    return 'x'
  elif not "support" in opcode:
    return "heavy_check_mark"
  elif opcode["support"] == "wip":
    return "construction"
  return opcode["support"]

def on_env(env, **kwargs):
  env.globals["emoji_name_from_opcode"] = emoji_name_from_opcode
  env.globals["get_opcode_url_as_html"] = get_opcode_url_as_html
