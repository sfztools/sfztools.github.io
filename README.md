# [SFZ Tools] documentation website

This website is built using [Jekyll], using [Node.js] to compile
all static assets including the [Bootstrap] library and built on
along with the [SASS] stylesheets. Most of the content on the website is
written using [Markdown], making it extremely easy to write and maintain.
Icons are provided by [Font Awesome], favicons by [Favicon Generator].
Anchors headings are provided by [AnchorJS], licensed under the MIT license.

## Local Build Quick-start Guide

- Install [rvm] and `yarn`
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

[AnchorJS]:               https://www.bryanbraun.com/anchorjs/
[Bootstrap]:              http://getbootstrap.com/
[Favicon Generator]:      https://realfavicongenerator.net/
[Font Awesome]:           http://fontawesome.io/
[Jekyll]:                 http://jekyllrb.com/
[Markdown]:               https://daringfireball.net/projects/markdown/
[Node.js]:                http://nodejs.org/
[rvm]:                    https://redtide.github.io/dev-docs/en/jekyll/rvm
[SASS]:                   https://sass-lang.com/
[SFZ Tools]:              https://sfztools.github.io/
