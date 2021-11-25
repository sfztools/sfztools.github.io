---
title: "Build"
---

[![Travis CI Build Status]](https://travis-ci.com/sfztools/sfizz)
[![AppVeyor Build Status]](https://ci.appveyor.com/project/sfztools/sfizz)

## Dependencies

In order to build the VST3 plugin or the LV2 plugin with a GUI, you need to
install dependencies:

- Ubuntu/Debian: `sudo apt install libx11-dev libx11-xcb-dev libxcb-util-dev libxcb-cursor-dev libxcb-keysyms1-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev libfontconfig1-dev libcairo2-dev libpango1.0-dev libfreetype6-dev`
- Fedora: `sudo dnf install libX11-devel libxcb-devel xcb-util-devel xcb-util-cursor-devel xcb-util-keysyms-devel libxkbcommon-devel libxkbcommon-x11-devel fontconfig-devel cairo-devel pango-devel freetype-devel`

In order to build also the standalone client and other demos, you need to
install also the [JACK] Audio Connection Kit library.

- Ubuntu/Debian: `sudo apt install libjack-jackd2-dev`
- Fedora: `sudo dnf install jack-audio-connection-kit-devel`

The benchmarks depend on the [benchmark] library.
If you wish to build the benchmarks you should either build it from source and
install the static library, or use the library from your distribution.
Debian and Ubuntu provide a `libbenchmark-dev` package that does this.

## Build System

We use [CMake] as build system. 
The basic process is to create a build directory, `cd` into it, configure and build it using cmake:
```
mkdir build
cd build
cmake ..
make
```

Current configuration switches for CMake are:

```null
ENABLE_LTO                Enable Link Time Optimization                 [default: ON]
SFIZZ_JACK                Enable JACK stand-alone build                 [default: ON]
SFIZZ_RENDER              Enable renderer of SMF files                  [default: ON]
SFIZZ_LV2                 Enable LV2 plug-in build                      [default: ON]
SFIZZ_LV2_UI              Enable LV2 GUI build                          [default: ON]
SFIZZ_VST                 Enable VST plug-in build                      [default: ON]
SFIZZ_AU                  Enable AU plug-in build                       [default: OFF]
SFIZZ_PUREDATA            Enable Puredata plug-in build                 [default: OFF]
SFIZZ_BENCHMARKS          Enable benchmarks build                       [default: OFF]
SFIZZ_DEMOS               Enable feature demos build                    [default: OFF]
SFIZZ_DEVTOOLS            Enable developer tools build                  [default: OFF]
SFIZZ_TESTS               Enable tests build                            [default: OFF]
SFIZZ_SHARED              Enable shared library build                   [default: ON]
SFIZZ_USE_VCPKG           Assume that sfizz is build using vcpkg        [default: OFF]
SFIZZ_USE_SNDFILE         Build with libsndfile                         [default: OFF]
SFIZZ_USE_SYSTEM_ABSEIL   Use Abseil libraries preinstalled on system   [default: OFF]
SFIZZ_USE_SYSTEM_SIMDE    Use SIMDe libraries preinstalled on system    [default: OFF]
SFIZZ_USE_SYSTEM_KISS_FFT Use KISS libraries preinstalled on system     [default: OFF]
SFIZZ_USE_SYSTEM_PUGIXML  Use pugixml libraries preinstalled on system  [default: OFF]
SFIZZ_USE_SYSTEM_CXXOPTS  Use CXXOPTS libraries preinstalled on system  [default: OFF]
SFIZZ_RELEASE_ASSERTS     Forced assertions in release builds           [default: OFF]
```

By default this builds and installs:
- The shared library version of sfizz with both C and C++ interfaces
- The JACK client
- The offline rendering client
- The LV2 plugin and its UI
- The VST3 plugin

See the relates sections for building details for:
- [Linux]
- [macOS]
- [Windows]

## JACK

You can find the JACK client in `clients/sfizz_jack`.
The JACK client client will forcefully connect to the system output,
and open an event input in JACK for you to connect a midi capable software
or hardware (e.g. `jack-keyboard`).
If no JACK server is already started it will start one with basic options.

## Rendering MIDI files

You can find `sfizz_render` in `clients/sfizz_render`.
From your `build` directory, type `clients/sfizz_render --help` for more information.

## Notes

If you already cloned the repository without the `--recursive` option,
update the submodules manually with

```bash
git submodule update --init --recursive
```

All targets but the GUI-less LV2 plugin can be disabled using:

```bash
cmake -DSFIZZ_JACK=OFF -DSFIZZ_SHARED=OFF -DSFIZZ_RENDER=OFF -DSFIZZ_LV2_UI=OFF -DSFIZZ_VST=OFF ..
```

and process as before.

All targets but `sfizz-render` can be disabled using:

```bash
cmake -DSFIZZ_JACK=OFF -DSFIZZ_SHARED=OFF -DSFIZZ_LV2=OFF -DSFIZZ_LV2_UI=OFF -DSFIZZ_VST=OFF ..
```

and process as before.

You can build with `clang`, although in that case the CMakeFile
defaults to using `libc++` instead of `libstdc++`.

[JACK]:                   https://jackaudio.org
[benchmark]:              https://github.com/google/benchmark/
[CMake]:                  https://cmake.org/
[Linux]:                  linux
[macOS]:                  macos
[Windows]:                windows
[Travis CI Build Status]: https://img.shields.io/travis/com/sfztools/sfizz.svg?label=Linux-macOS&style=popout&logo=travis
[AppVeyor Build Status]:  https://img.shields.io/appveyor/ci/sfztools/sfizz.svg?label=Windows&style=popout&logo=appveyor
