---
title: "Build"
---

## Git

Ensure to have `git` installed to be able to download the sfizz source files,
then run:

```sh
git clone --recursive https://github.com/sfztools/sfizz-ui.git
```

This will also download recursively all the submodules required to build the project.

Use `sfizz.git` repository if you are only interested on the library.

If you already downloaded the project without the `recursive` (or `recurse-submodules`)
option, you can run:

```sh
git submodule update --init --recursive
```

See also the main [FAQ](../../../faq#missing-submodules) page.

## Dependencies

On macOS and Windows we build most of bundled dependencies statically.
However you can use a package manager to install the required libraries, like
[Homebrew](https://brew.sh/) on macOS and specifying the related
`SFIZZ_USE_SYSTEM_*` CMake options (see below).
This will also speed up the build process.

Check the [Linux] page for details on how to install the required libraries
on various distributions.

## CMake Build System

We use [CMake] as build system.
The basic process is to configure and build the project.

On macOS using `brew`:

```bash
brew update
brew upgrade cmake
```

### Configuration

<div class="alert alert-warning" role="alert">
  Some of the following options might be added / changed / removed,
  so please check the main <code>CMakeLists.txt</code> on the root directory of the repository.
  If using the <code>sfizz-ui</code> repository check also in the
  <code>library</code> subdirectory / submodule.
</div>

Current configuration options for sfizz are:

```null
ENABLE_LTO                Enable Link Time Optimization                       [default: ON]
SFIZZ_JACK                Enable JACK stand-alone build                       [default: ON only on Linux]
SFIZZ_RENDER              Enable renderer of SMF files                        [default: ON]
SFIZZ_SHARED              Enable shared library build                         [default: ON]
PLUGIN_AU                 Enable AU plug-in build                             [default: ON only on macOS]
PLUGIN_LV2                Enable LV2 plug-in build                            [default: ON]
PLUGIN_LV2_UI             Enable LV2 GUI build                                [default: ON]
PLUGIN_PUREDATA           Enable Puredata plug-in build                       [default: OFF]
PLUGIN_VST2               Enable VST2 plug-in build (unsupported)             [default: OFF]
PLUGIN_VST3               Enable VST3 plug-in build                           [default: ON]
SFIZZ_BENCHMARKS          Enable benchmarks build                             [default: OFF]
SFIZZ_DEMOS               Enable feature demos build                          [default: OFF]
SFIZZ_DEVTOOLS            Enable developer tools build                        [default: OFF]
SFIZZ_TESTS               Enable tests build                                  [default: OFF]
SFIZZ_USE_SNDFILE         Build with libsndfile                               [default: OFF]
SFIZZ_SNDFILE_STATIC      Link the sndfile library statically                 [default: OFF]
SFIZZ_USE_SYSTEM_ABSEIL   Use Abseil libraries preinstalled on system         [default: OFF]
SFIZZ_USE_SYSTEM_CATCH    Use Catch libraries preinstalled on system          [default: OFF]
SFIZZ_USE_SYSTEM_CXXOPTS  Use CXXOPTS libraries preinstalled on system        [default: OFF]
SFIZZ_USE_SYSTEM_GHC_FS   Use GHC Filesystem libraries preinstalled on system [default: OFF]
SFIZZ_USE_SYSTEM_LV2      Use LV2 headers preinstalled on system              [default: OFF]
SFIZZ_USE_SYSTEM_SIMDE    Use SIMDe libraries preinstalled on system          [default: OFF]
SFIZZ_USE_SYSTEM_KISS_FFT Use KISS libraries preinstalled on system           [default: OFF]
SFIZZ_USE_SYSTEM_PUGIXML  Use pugixml libraries preinstalled on system        [default: OFF]
SFIZZ_USE_SYSTEM_VST3SDK  Use VST3SDK source files preinstalled on system     [default: OFF]
SFIZZ_PROFILE_BUILD       Profile the build time                              [default: OFF]
SFIZZ_RELEASE_ASSERTS     Forced assertions in release builds                 [default: OFF]
```

On macOS it's possible to enable universal builds by adding
`-D CMAKE_OSX_ARCHITECTURES="arm64;x86_64"`.

### Build

The 3 basic steps are:
- create a build directory and `cd` into it
- create the configuration
- run the build command
  (the following example uses `make`, default build tool on Unix based systems)

```sh
mkdir build && cd build
cmake ..
make
```

From (at least) CMake v3.13 this can be done in 2 steps in a crossplatform way:

```sh
cmake -B build -S .
cmake --build build
```

For further details check the [CMake configuration options manual].
For reference check also our [CI] build workflow file.

You can build with `clang`, although in that case the CMakeFile
defaults to using `libc++` instead of `libstdc++`.

By default this builds:
- The shared library version of sfizz with both C and C++ interfaces
- The JACK client on Linux
- The offline rendering client
- The AU plugin on macOS
- The LV2 plugin and its UI
- The VST3 plugin

## Examples

All targets but the GUI-less LV2 plugin can be disabled using:

```sh
cmake .. \
-DSFIZZ_JACK=OFF \
-DSFIZZ_SHARED=OFF \
-DSFIZZ_RENDER=OFF \
-DPLUGIN_LV2_UI=OFF \
-DPLUGIN_VST3=OFF
```

and process as before.

All targets but `sfizz_render` can be disabled using:

```sh
cmake .. \
-DSFIZZ_JACK=OFF \
-DSFIZZ_SHARED=OFF \
-DPLUGIN_LV2=OFF \
-DPLUGIN_LV2_UI=OFF \
-DPLUGIN_VST3=OFF
```

and process as before.

## Rendering MIDI files

You can find `sfizz_render` in `clients/sfizz_render`.
From your `build` directory, type `clients/sfizz_render --help` for more information.


[Linux]:   linux
[macOS]:   macos
[Windows]: windows
[CI]:      https://github.com/sfztools/sfizz-ui/blob/develop/.github/workflows/build.yml
[CMake]:   https://cmake.org/
[CMake configuration options manual]: https://cmake.org/cmake/help/latest/manual/cmake.1.html#options
