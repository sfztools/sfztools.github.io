---
title: "sfizz v1.0.0 release"
author: "redtide"
date: "2021-04-16T23:00:47+0200"
---
- SFZ v1 is virtually supported except for a handful of opcodes ! Please check
  https://sfz.tools/sfizz/development/status/ for the up-to-date status of opcode support.
- It is now possible to build sfizz without relying on libsndfile, using a set of libraries. This is now the
  default build mode. Building with libsndfile can be enabled at configure time.
- The library and plugins can now load DecentSampler files, and could accomodate other formats.
- CCs, keyswitch range, key ranges and active keyswitch are now displayed in the editor for all plugins.
  There has been a lot of UI work to make it more practical to use.
- There is an OSC interface in the library, which allows to have introspection into the currently
  loaded file, the state of CCs/keyswitches, and also set some parameters for loaded regions.
