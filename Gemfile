source "https://rubygems.org"

if Gem::Platform.local.os == "darwin"
  gem "webrick"
else
  ruby "~> 2.7.1"
end

# Uncomment to build our site in Travis-CI and force gh-pages compatibility
# in RVM without gh-pages installed, see:
# - https://pages.github.com/versions/
# - https://docs.travis-ci.com/user/languages/ruby/#default-build-script
# - https://github.com/travis-ci/travis-web/blob/master/Gemfile

#group :development, :test do
#  gem "rake", "~> 12"
#end

gem "jekyll", "3.9.0"

group :jekyll_plugins do
  gem "jekyll-sitemap", "1.4.0"
  gem "jemoji", "0.11.1"
  gem "kramdown-parser-gfm", "1.1.0"
end
