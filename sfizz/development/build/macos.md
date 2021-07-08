---
title: "macOS Build"
---
## Configuration

Update [Homebrew], install [CMake] and [libsndfile] if missing.

```bash
brew update
brew upgrade cmake
brew install libsndfile
```

## make

```bash
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release \
      -DSFIZZ_VST=ON \
      -DSFIZZ_AU=ON \
      -DCMAKE_CXX_STANDARD=14 \
      ..
make -j$(sysctl -n hw.ncpu)
```

Add `-DSFIZZ_LV2=ON` if you want to use the LV2 version of the plugin.

## XCode

Usually the XCode build is called with something like:

```bash
mkdir build && cd build
cmake -G Xcode ..
xcodebuild -project sfizz.xcodeproj -alltargets -configuration Release build
```

But unfortunately there is an [issue] currently building with XCode 10+
using CMake, so we are using `make` instead.

[CMake]:      https://cmake.org/
[Homebrew]:   https://brew.sh/
[issue]:      https://gitlab.kitware.com/cmake/cmake/issues/18088
[libsndfile]: http://mega-nerd.com/libsndfile/
