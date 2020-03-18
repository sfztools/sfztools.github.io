---
title: "sfizz v0.3.1 release"
author: "redtide"
---
- Added a VST3 plug-in front-end to the library. It is still quite experimental
  and suffers from problems that stem from the VST3 SDK itself. ([#99])
- Added effect buses and processing. There is a [lofi] effect available for now,
  as well as the same filters and EQs you can apply on the regions.
  More will come soon! ([#84])
- Added a script to parse and render the timings.
  This can help tracking performance issues and regressions. ([#89])
- Various fixups, performance improvements, and CI updates.

[#84]:  https://github.com/sfztools/sfizz/pull/84
[#89]:  https://github.com/sfztools/sfizz/pull/89
[#99]:  https://github.com/sfztools/sfizz/pull/99
[lofi]: https://sfzformat.com/opcodes/type#lofi
