---
title: "Linux Build"
---
In Debian-based distributions, the required dependencies can be installed as
follow:

```bash
sudo apt install libjack-jackd2-dev libsndfile1-dev libcairo2-dev libfontconfig1-dev libx11-xcb-dev libxcb-util-dev libxcb-cursor-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev libxcb-keysyms1-dev libglib2.0-dev
```

For benchmarks, Debian and Ubuntu provide a `libbenchmark-dev` package that does this.

The process is as follows:
1. Clone the repository with all the submodules
2. Create a build directory for CMake and `cd` into it
3. Build as release
4. Enjoy :)

In the shell world, this means

```bash
git clone --recursive https://github.com/sfztools/sfizz.git
cd sfizz
mkdir build && cd build
cmake ..
make
sudo make install
```

You can build with `clang`, although in that case the CMakeFile
defaults to using `libc++` instead of `libstdc++`.

## Building the LV2 plugin with static linkage to `libsndfile` on Linux

Most people will probably want the LV2 plugin with `libsndfile` built-in statically.
You can directly build it this way through Docker by calling these in an *empty* directory :
```
wget https://raw.githubusercontent.com/sfztools/sfizz/master/scripts/Dockerfile
wget https://raw.githubusercontent.com/sfztools/sfizz/master/scripts/x64-linux-hidden.cmake
docker build -t sfizz .
docker cp $(docker create sfizz:latest):/tmp/sfizz/build/sfizz.lv2 .
```
Note that the statically linked LV2 plugin is to be distributed under
the LGPL license, as per the terms of the `libsndfile` library.

This uses Docker and `vcpkg`.

