import argparse, os, requests, sys
sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime
from new_post import new_post

"""
  Gets GitHub latest release information
  and keep track of version and publishing date in YAML.
"""
def get(repo_slug, dest_dir):
  rqst = requests.get("https://api.github.com/repos/{}/releases/latest".format(repo_slug))
  json = rqst.json()
  date = datetime.strptime(json["published_at"], "%Y-%m-%dT%H:%M:%S%z")
  file = open(dest_dir, "w")
  yaml = "date:    \"{}\"\nversion: \"{}\"\n"\
    .format(date.strftime("%B %d, %Y"), json["tag_name"])
  file.write(yaml)
  return json

"""
  Creates a latest release post.
"""
def post(repo_slug, dest_dir):
  json    = get(repo_slug, dest_dir)
  slug    = repo_slug.split('/')
 #author  = slug[0]
 #appname = slug[1]
  title = "{} {} release".format(slug[1], json["tag_name"])
  content = json["body"].replace("\r\n", '\n') + "\n\n## Download links\n\n"
  for asset in json["assets"]:
    content += "- [{}]({})\n".format(asset["name"], asset["browser_download_url"])
  content +=\
    "- [GitHub Release]({})\n"\
    "- [Downloads](../../{}/downloads.md)\n".format(json["html_url"], slug[1])
  # TODO: downloads page relative path as function parameter
  new_post(title, slug[0], content)
  return True

def main():
  parser     = argparse.ArgumentParser(prog="release")
  subparsers = parser.add_subparsers(
    title = "subcommands",
    help  = "release operations"
  )
  parser.add_argument("repo_slug", type=str, help="repository slug (account name/repo name)")
  parser.add_argument("dest_dir",  type=str, help="relative path from the root directory for YAML")

  get_parser = subparsers.add_parser("get", help = "gets GitHub latest release information and keep track of version and publishing date in YAML.")
  get_parser.set_defaults(func=get)

  post_parser = subparsers.add_parser("post", help = "creates a latest release post.")
  post_parser.set_defaults(func=post)

  args = parser.parse_args()
  args.func(args.repo_slug, args.dest_dir)

if __name__ == "__main__":
  main()
