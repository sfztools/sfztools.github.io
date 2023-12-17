---
title: Downloads
---
{# TODO: Get these values from GitHub REST API #}
`sfizz` {{ sfizz_release.version }} - [released] on {{ sfizz_release.date }}

<h2><i class="fa fa-linux"> Linux</i></h2>

Packages for a wide variety of Linux distributions.

<a
  class="btn btn-primary"
  href="https://software.opensuse.org/download.html?project=home%3Asfztools%3Asfizz&package=sfizz"
  role="button">
  64-bit Stable
</a>
<a
  class="btn btn-warning"
  href="https://software.opensuse.org/download.html?project=home%3Asfztools%3Asfizz%3Adevelop&package=sfizz"
  role="button">
  64-bit Current
</a>

<h2><i class="fa fa-windows"> Windows</i></h2>

Installers for Microsoft Windows 7 and up, all 64-bit and 32-bit editions.

<a
  class="btn btn-primary"
  href="https://github.com/sfztools/sfizz-ui/releases/download/{{ sfizz_release.version }}/sfizz-{{ sfizz_release.version }}-win64.exe"
  role="button">
  64-bit
</a>
<a
  class="btn btn-primary"
  href="https://github.com/sfztools/sfizz-ui/releases/download/{{ sfizz_release.version }}/sfizz-{{ sfizz_release.version }}-win32.exe"
  role="button">
  32-bit
</a>

<h2><i class="fa fa-apple"> macOS</i></h2>

Universal macOS package, for 64-bit Intel and Apple Silicon.

<a
  class="btn btn-primary"
  href="https://github.com/sfztools/sfizz-ui/releases/download/{{ sfizz_release.version }}/sfizz-{{ sfizz_release.version }}-macos.pkg"
  role="button">
  Universal
</a>

<h2><i class="fa fa-github"> Source code</i></h2>

Archive of the source code, available under a free software license.

<a
  class="btn btn-primary"
  href="https://github.com/sfztools/sfizz/releases/download/{{ sfizz_release.version }}/sfizz-{{ sfizz_release.version }}.tar.gz"
  role="button">
  Library source archive
</a>

<a
  class="btn btn-primary"
  href="https://github.com/sfztools/sfizz-ui/releases/download/{{ sfizz_release.version }}/sfizz-{{ sfizz_release.version }}.tar.gz"
  role="button">
  Plugins source archive (library included)
</a>

[released]: https://github.com/sfztools/sfizz/releases/tag/{{ sfizz_release.version }}
