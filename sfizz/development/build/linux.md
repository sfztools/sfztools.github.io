---
title: "Linux Build"
---
In Debian-based distributions, the required dependencies can be installed as
follow:

```bash
sudo apt install libjack-jackd2-dev libsndfile1-dev libcairo2-dev libfontconfig1-dev libx11-xcb-dev libxcb-util-dev libxcb-cursor-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev libxcb-keysyms1-dev libglib2.0-dev zenity
```

For benchmarks, add the `libbenchmark-dev` package.

## Building the LV2 plugin with static linkage

Most people will probably want the LV2 plugin with `libsndfile` built-in statically.\
In this case add `-DSFIZZ_STATIC_DEPENDENCIES=ON` to the build options.

Note that the statically linked LV2 plugin is to be distributed under
the LGPL license, as per the terms of the `libsndfile` library.

Alternatively add `-DSFIZZ_USE_SNDFILE=OFF` to use the `dr_libs` instead.
