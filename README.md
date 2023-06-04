# [SFZ Tools] documentation website

The website is built using the following software and technologies:

- [AnchorJS] anchors headings, MIT license
- [Bootstrap] UI toolkit, code under MIT license, docs under [Creative Commons]
- [Favicon Generator] for favicons
- [Font Awesome] for icons, [SIL OFL 1.1] license
- [highlight.js] for syntax highlighting, BSD 3-Clause license
- [Jekyll] static website generator, MIT license
- [Markdown] markup language
- [Node.js] to compile all static assets, including the Bootstrap library, [see license]
- [SASS] for stylesheets, MIT license

## Local Build Quick-start Guide

- Install `ruby` and `yarn`
- Use the automatic setup via `setup.sh`

or manually:

```bash
$ gem update --user-install
$ gem install bundler --user-install
$ bundle config set path '.bundle'
$ bundle install
$ yarn --no-bin-links
$ yarn dist
$ bundle exec jekyll serve --watch --host 0.0.0.0
```

The local website should be available at <http://localhost:4000/>

## Creating posts

This can be done either manually by creating a new .md file
in the [_posts] directory, paying attention for a correct filename, date and
[front-matter], or by running the following command:

```bash
$ ./new_post.sh "New post title" "<author_name>"
```


[SFZ Tools]:              https://sfztools.github.io/
[AnchorJS]:               https://www.bryanbraun.com/anchorjs/
[Bootstrap]:              https://getbootstrap.com/
[Creative Commons]:       https://creativecommons.org/licenses/by/3.0/
[Favicon Generator]:      https://realfavicongenerator.net/
[Font Awesome]:           https://fontawesome.io/
[front-matter]:           https://jekyllrb.com/docs/front-matter/
[highlight.js]:           https://highlightjs.org/
[Jekyll]:                 https://jekyllrb.com/
[Markdown]:               https://daringfireball.net/projects/markdown/
[Node.js]:                https://nodejs.org/
[_posts]:                 https://github.com/sfztools/sfztools.github.io/tree/master/_posts/
[SASS]:                   https://sass-lang.com/
[see license]:            https://github.com/nodejs/node/blob/main/LICENSE
[SIL OFL 1.1]:            https://scripts.sil.org/cms/scripts/page.php?item_id=OFL
