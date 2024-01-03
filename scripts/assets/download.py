#!/usr/bin/env python3

import argparse, os, requests, shutil, tempfile, yaml
from urllib.parse import urlparse

_assets = {}

def _get(url, path, overwrite=False):
  filename = path
  if os.path.isdir(filename):
    filename += '/' + os.path.basename(urlparse(url).path)
  if not overwrite and os.path.isfile(filename):
    return
  print("Downloading " + url + " to " + path)
  headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0"}
  response = requests.get(url, headers=headers)
  with open(filename, "wb") as file:
    file.write(response.content)

def get(args):
  _get(args.url, args.path, args.overwrite)

def get_bs5(dummy):
  if os.path.isfile(".bootstrap/scss/bootstrap.scss"):
    return
  for lib in _assets:
    if lib["name"] == "bootstrap":
      version = lib["version"]
      break
  dest_dir     = ".bootstrap/bootstrap-" + version
  partial      = "/scss"
  partial_dest = dest_dir + partial
  archive_ext  = ".tar.gz"
  archive_url  = "https://github.com/twbs/bootstrap/archive/refs/tags/v" + \
    version + archive_ext
  tmp = tempfile.NamedTemporaryFile(delete=False)
  try:
    _get(archive_url, tmp.name, True)
    shutil.unpack_archive(tmp.name, ".bootstrap/", "gztar")
    shutil.move(partial_dest, ".bootstrap/")
    shutil.rmtree(dest_dir)
  finally:
    tmp.close()
    os.unlink(tmp.name)
"""
def get_forkawesome(dummy):
  if os.path.isfile("docs/assets/fonts/forkawesome-webfont.ttf"):
    return
  for lib in _assets:
    if lib["name"] == "fork-awesome":
      version = lib["version"]
      break
  fa_zip = version + ".zip"
  fa_url = "https://github.com/ForkAwesome/Fork-Awesome/archive/" + fa_zip
  fa_dir = "Fork-Awesome-" + version
  fa_fnt = fa_dir + "/fonts"
  tmp    = tempfile.NamedTemporaryFile(delete=False)
  try:
    _get(fa_url, tmp.name, True)
    shutil.unpack_archive(tmp.name, ".", "zip")
    shutil.move(fa_fnt, "docs/assets/")
    shutil.rmtree(fa_dir)
  finally:
    tmp.close()
    os.unlink(tmp.name)
"""
def get_fa(dummy):
  if os.path.isfile("docs/assets/webfonts/fa-brands-400.ttf"):
    return
  for lib in _assets:
    if lib["name"] == "fontawesome":
      version = lib["version"]
      break
  fa_dir = "fontawesome-free-" + version + "-web"
  fa_zip = fa_dir + ".zip"
  fa_url = "https://use.fontawesome.com/releases/v" \
         + version + '/'  + fa_zip
  fa_fnt = fa_dir + "/webfonts"
  tmp    = tempfile.NamedTemporaryFile(delete=False)
  try:
    _get(fa_url, tmp.name, True)
    shutil.unpack_archive(tmp.name, ".", "zip")
    shutil.move(fa_fnt, "docs/assets/")
    shutil.move(fa_dir + "/css/brands.min.css",       "docs/assets/css/")
    shutil.move(fa_dir + "/css/fontawesome.min.css",  "docs/assets/css/")
    shutil.move(fa_dir + "/css/solid.min.css",        "docs/assets/css/")
    shutil.move(fa_dir + "/css/v4-font-face.min.css", "docs/assets/css/")
    shutil.rmtree(fa_dir)
  finally:
    tmp.close()
    os.unlink(tmp.name)

def get_assets(dummy):
  for library in _assets:
    if "css" in library:
      for asset in library["css"]:
        dest_dir = "docs/assets/css"
        url = library["url_prefix"] + library["version"] + asset
        _get(url, dest_dir)

  for library in _assets:
    if "js" in library:
      for asset in library["js"]:
        dest_dir = "docs/assets/js"
        url = library["url_prefix"] + library["version"] + asset
        _get(url, dest_dir)

def main():
  global _assets
  if not os.path.isfile(os.getcwd() + "/mkdocs.yml"):
    raise SystemExit("Error: You must run this file from the main directory")
  f          = open("data/assets.yml")
  _assets    = yaml.load(f, Loader=yaml.FullLoader)
  parser     = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(
    title = "subcommands",
    help  = "download operations"
  )
  get_parser = subparsers.add_parser("get", help = "download a file.")
  get_parser.set_defaults(func=get)
  get_parser.add_argument("url",       type=str,  help="download url")
  get_parser.add_argument("path",      type=str,  help="file or directory destination path")
  get_parser.add_argument("overwrite", type=bool, help="overwrite if exists", default=False, nargs='?')

  sts_parser = subparsers.add_parser("get_assets", help = "download assets from yaml list.")
  sts_parser.set_defaults(func=get_assets)

  bs5_parser = subparsers.add_parser("get_bs5", help = "download bootstrap 5 library.")
  bs5_parser.set_defaults(func=get_bs5)

  fa_parser = subparsers.add_parser("get_fa", help = "download fontawesome 6 library.")
  fa_parser.set_defaults(func=get_fa)

  args = parser.parse_args()
  args.func(args)

if __name__ == "__main__":
  main()
