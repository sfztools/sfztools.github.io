---
title: "Build"
---
We use [CMake] as build system, the available build options are listed
in the main [CMakeLists.txt] configuration file.\

The process is as follows:
1. Clone the repository with all the submodules
2. Create a build directory for CMake and `cd` into it
3. Build as release
4. Enjoy :)

In the shell world, this means:

```
git clone --recursive https://github.com/sfztools/sfizz.git
cd sfizz
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --target all
```

By default this builds:
- The shared library version of sfizz with both C and C++ interfaces
- The JACK client
- The offline rendering client
- The LV2 plugin

See the related sections for building details for:
- [Linux]
- [macOS]
- [Windows]

You can build with `clang`, although in that case the CMakeFile
defaults to using `libc++` instead of `libstdc++`.

On UNIX based systems is it possible to use `make` for the build step.\
`sudo make install` to install system wide or\
`cmake --build . --target install` as platform independent command.

## Dependencies

By default `sfizz` is built against and dynamically linked to the
[libsndfile] library, though it's possible to replace it with the built in
[dr_libs] alternative.

The benchmarks depend on the [benchmark] library.
If you wish to build the benchmarks you should either build it from source and
install the static library, or use the library from your distribution.
Debian and Ubuntu provide a `libbenchmark-dev` package that does this.

## JACK

In order to build the standalone client and other demos, you need to
install also the [JACK] Audio Connection Kit library.

You can then find the JACK client in `clients/sfizz_jack`.
Just specify an `.sfz` file as a parameter and you are good to go.
The JACK client client will forcefully connect to the system output,
and open an event input in JACK for you to connect a midi capable software
or hardware (e.g. `jack-keyboard`).
If no JACK server is already started it will start one with basic options.

## Notes

If you already cloned the repository without the `--recursive` option,
update the submodules manually with:

```
git submodule update --init --recursive
```

All targets but the LV2 plugin can be disabled using:

```
cmake -DSFIZZ_JACK=OFF -DSFIZZ_SHARED=OFF -DSFIZZ_RENDER=OFF ..
```

and process as before.
In this case, the LV2 plugin will load `libsndfile` dynamically from your system.

You can build with `clang`, although in that case the CMakeFile
defaults to using `libc++` instead of `libstdc++`.

[libsndfile]:             http://mega-nerd.com/libsndfile/
[dr_libs]:                https://github.com/mackron/dr_libs
[JACK]:                   https://jackaudio.org
[benchmark]:              https://github.com/google/benchmark/
[CMake]:                  https://cmake.org/
[CMakeLists.txt]:         https://github.com/sfztools/sfizz/blob/develop/CMakeLists.txt#L21
[Linux]:                  linux
[macOS]:                  macos
[Windows]:                windows
