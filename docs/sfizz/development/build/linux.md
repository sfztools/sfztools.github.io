---
title: "Linux Build"
---
On this page we specify the required packages on Debian / Ubuntu and Fedora
(based) distributions for reference, but unfortunately we can't cover all systems.

For Archlinux based systems you can check their official [PKGBUILD];
we also provide one for the current development source tree on [AUR].

## Dependencies

In order to build the plugins with the GUI,
you need to install the following dependencies.

For the standalone client and other demos,
you need to install also the [JACK] Audio Connection Kit library.

### Ubuntu / Debian

```sh
sudo apt install \
libcairo2-dev \
libfontconfig1-dev \
libfreetype6-dev \
libglib2.0-dev \
libpango1.0-dev \
libx11-dev \
libx11-xcb-dev \
libxcb-cursor-dev \
libxcb-keysyms1-dev \
libxcb-util-dev \
libxcb-xkb-dev \
libxkbcommon-dev \
libxkbcommon-x11-dev \
zenity \
libjack-jackd2-dev
```

### Fedora

```sh
sudo dnf install \
cairo-devel \
fontconfig-devel \
freetype-devel \
glib2-devel \
libX11-devel \
libxcb-devel \
libxkbcommon-devel \
libxkbcommon-x11-devel \
pango-devel \
xcb-util-cursor-devel \
xcb-util-devel \
xcb-util-keysyms-devel \
zenity \
jack-audio-connection-kit-devel
```

The default build uses the bundled `dr_libs` library for audio samples management.

If building with `libsndfile`, Debian and Ubuntu provide a `libsndfile1-dev`
package, `libsndfile-devel` for Fedora.

### Benchmarks

The benchmarks depend on the [benchmark] library.
If you wish to build the benchmarks you should either build the static library
from source, or use the library from your distribution.
Debian and Ubuntu provide a `libbenchmark-dev` package, `google-benchmark-devel`
for Fedora.

## JACK Standalone Client

You can find the JACK client in `clients/sfizz_jack`.
The JACK client client will forcefully connect to the system output,
and open an event input in JACK for you to connect a midi capable software
or hardware (e.g. `jack-keyboard`).
If no JACK server is already started it will start one with basic options.


[benchmark]: https://github.com/google/benchmark/
[JACK]:      https://jackaudio.org
[PKGBUILD]:  https://gitlab.archlinux.org/archlinux/packaging/packages/sfizz/-/blob/main/PKGBUILD
[AUR]:       https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=sfizz-git
