# [SFZ Tools] documentation website

This website is built using [Jekyll], using [Node.js] to compile
all static assets including the [Bootstrap] library and built on
along with the [SASS] stylesheets. Most of the content on the website is
written using [Markdown], making it extremely easy to write and maintain.
Icons are provided by [Font Awesome], favicons by [Favicon Generator].
Anchors headings are provided by [AnchorJS], licensed under the MIT license.
Syntax highlighting is provided by [highlight.js], BSD 3-Clause License.

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
[Bootstrap]:              https://getbootstrap.com/
[Favicon Generator]:      https://realfavicongenerator.net/
[Font Awesome]:           https://fontawesome.io/
[Jekyll]:                 https://jekyllrb.com/
[Markdown]:               https://daringfireball.net/projects/markdown/
[Node.js]:                https://nodejs.org/
[rvm]:                    https://redtide.github.io/notepad/en/jekyll/rvm
[SASS]:                   https://sass-lang.com/
[SFZ Tools]:              https://sfztools.github.io/
[highlight.js]:           https://highlightjs.org/
