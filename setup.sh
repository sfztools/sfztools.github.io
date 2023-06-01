#!/bin/bash

set -e

cd $PWD

if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
	echo "Setup and run Jekyll"
	echo ""
	echo "Usage: ${0} [option]"
	echo ""
	echo "Options are not mandatory, only one at a time."
	echo "-a, --assets      Build minimized css style and js script from sources."
	echo "-i, --install     Install Bundler and node modules using Yarn."
	echo "-I, --incremental Runs Jekyll in incremental mode."
	echo ""
	exit 0
fi

# Install or update ruby and yarn packages
if [ "$1" == "-i" ] || [ "$1" == "--install" ]; then
	gem update
	gem install bundler
	bundle install
	yarn --no-bin-links
fi

# Rebuild minimized assets
if [ ! -f "assets/css/style.min.css" ] || [ "$1" == "-a" ] || [ "$1" == "--assets" ]; then
	yarn dist
fi

# Enable Jekyll incremental build
if [ "$1" == "-I" ] || [ "$1" == "--incremental" ]; then
	incremental="-I"
fi

bundle exec jekyll serve --watch --host=0.0.0.0 $incremental
