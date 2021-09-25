---
title: "Build"
---

[![Travis CI Build Status]](https://travis-ci.com/sfztools/sfizz)
[![AppVeyor Build Status]](https://ci.appveyor.com/project/sfztools/sfizz)

## Dependencies

`sfizz` depends mainly on the [libsndfile] library.
In order to build also the standalone client and other demos, you need to
install also the [JACK] Audio Connection Kit library.

The benchmarks depend on the [benchmark] library.
If you wish to build the benchmarks you should either build it from source and
install the static library, or use the library from your distribution.
Debian and Ubuntu provide a `libbenchmark-dev` package that does this.

## Build System

We use [CMake] as build system.
Current configuration switches for CMake are:

```null
ENABLE_LTO              Enable Link Time Optimization          [default: ON]
SFIZZ_JACK              Enable JACK stand-alone build          [default: ON]
SFIZZ_RENDER            Enable renderer of SMF files           [default: ON]
SFIZZ_LV2               Enable LV2 plug-in build               [default: ON]
SFIZZ_VST               Enable VST plug-in build               [default: OFF]
SFIZZ_AU                Enable AU plug-in build                [default: OFF]
SFIZZ_BENCHMARKS        Enable benchmarks build                [default: OFF]
SFIZZ_DEVTOOLS          Enable developer tools build           [default: OFF]
SFIZZ_TESTS             Enable tests build                     [default: OFF]
SFIZZ_SHARED            Enable shared library build            [default: ON]
SFIZZ_USE_VCPKG         Assume that sfizz is build using vcpkg [default: OFF]
SFIZZ_STATIC_LIBSNDFILE Link libsndfile statically             [default: OFF]
SFIZZ_RELEASE_ASSERTS   Forced assertions in release builds    [default: OFF]
```

By default this builds and installs:
- The shared library version of sfizz with both C and C++ interfaces
- The JACK client
- The offline rendering client
- The LV2 plugin

See the relates sections for building details for:
- [Linux]
- [macOS]
- [Windows]

## JACK

You can then find the JACK client in `clients/sfizz_jack`.
Just specify an `.sfz` file as a parameter and you are good to go.
The JACK client client will forcefully connect to the system output,
and open an event input in JACK for you to connect a midi capable software
or hardware (e.g. `jack-keyboard`).
If no JACK server is already started it will start one with basic options.

## Notes

If you already cloned the repository without the `--recursive` option,
update the submodules manually with

```bash
git submodule update --init --recursive
```

All targets but the LV2 plugin can be disabled using:

```bash
cmake -DSFIZZ_JACK=OFF -DSFIZZ_SHARED=OFF -DSFIZZ_RENDER=OFF ..
```

and process as before.
In this case, the LV2 plugin will load `libsndfile` dynamically from your system.

You can build with `clang`, although in that case the CMakeFile
defaults to using `libc++` instead of `libstdc++`.

[libsndfile]:             http://mega-nerd.com/libsndfile/
[JACK]:                   https://jackaudio.org
[benchmark]:              https://github.com/google/benchmark/
[CMake]:                  https://cmake.org/
[Linux]:                  linux
[macOS]:                  macos
[Windows]:                windows
[Travis CI Build Status]: https://img.shields.io/travis/com/sfztools/sfizz.svg?label=Linux-macOS&style=popout&logo=travis
[AppVeyor Build Status]:  https://img.shields.io/appveyor/ci/sfztools/sfizz.svg?label=Windows&style=popout&logo=appveyor
