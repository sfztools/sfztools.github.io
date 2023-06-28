# MKDocs issues

## FIXME

- Fix opcodes tables: version not correctly inherited by modulation aliases
- Fix `doxygen.j2` enumerations (L38). See also
  <https://github.com/mkdocs/mkdocs/discussions/3247>
- Fix pages with TOC
- mkdocs/assets/img/sfizz/badge_*.svg
- atom.xml

## TODO

- GitHub issues links in release posts, see
  <https://github.com/theskumar/autolink-references-mkdocs-plugin/issues/7>
- make a theme and move `layout/partials/sfizz/opcodes_table_cards.j2` in `overrides`
- Mermaid without plugin? This thing is a total mess: slow, too many dependenices
  and messages in log

### Create a new "mkdocs-sass-plugin"

references:
- `mkdocs-extra-sass-plugin`
- <https://github.com/mkdocs/mkdocs/issues/2276>

`mkdocs-extra-sass-plugin` seems no more maintained, it requires updates
but anyway it uses the deprecated libsass, now replaced by dart sass.
It also requires `livereload` package, which is not desiderable.

The currently used `pysass` still uses libsass.

### Create a new "mkdocs-uglify-plugin"

- `mkdocs-minify-plugin` decides name and place where to put the minimized asset
- `uglipyjs` and `slimit` seems broken for some reason (missing modules)
- the currently used `css-html-js-minify` doesn't support ES6/ES7 javascript
