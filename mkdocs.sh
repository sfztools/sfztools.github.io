#!/bin/bash

cd $PWD
set -e
script_name=$(basename $0 | sed "s/\.sh$//")

if [ ! -f "mkdocs.yml" ]; then
	echo "Error: This script must be called from the main project directory."
	exit 1
fi

if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
	echo "Setup and run MKDocs"
	echo ""
	echo "Usage: ./${script_name} [option]"
	echo ""
	echo "Options are not mandatory, only one at a time:"
	echo "-a, --assets    Build minimized css styles and js scripts from sources."
	echo "-b, --build     Build the site."
	echo "-d, --db        Update sfz database."
	echo "-h, --help      Show this help message."
	echo "-i, --install   Install poetry' packages (poetry must be already installed)."
	echo ""
	exit 0
fi

if [ ! -f "docs/assets/css/style.min.css" ] || [ "$1" == "-a" ] || [ "$1" == "--assets" ]; then
	poetry run python3 scripts/assets/download.py get_assets
	poetry run python3 scripts/assets/download.py get_bs5
	poetry run python3 scripts/assets/download.py get_fa
	poetry run python3 scripts/assets/uglify.py
	exit 0
fi

if [ "$1" == "-i" ] || [ "$1" == "--install" ]; then
	poetry lock
	poetry install --no-root
	exit 0
fi

if [ "$1" == "-b" ] || [ "$1" == "--build" ]; then
	poetry run mkdocs build
	exit 0
fi

if [ "$1" == "-d" ] || [ "$1" == "--db" ]; then
	poetry run python scripts/assets/download.py get \
		https://raw.githubusercontent.com/sfzformat/sfzformat.github.io/source/data/sfz/syntax.yml \
		data/sfz \
		True
fi

poetry run mkdocs serve
