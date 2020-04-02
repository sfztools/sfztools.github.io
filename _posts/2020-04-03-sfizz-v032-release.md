---
title: "sfizz v0.3.2 release"
author: "redtide"
---
- sfizz now builds down to gcc-4.9 with stricter C++11 compliance.
  The main release builds use C++17 mode on newer compilers ([#111], [#110])
- Upstream libraries updates (abseil, filesystem and atomic_queue) ([#121])
- Added an experimental support for `make uninstall` ([#118], [#120])
- Add the autopan ([#105]), width, rectifier, gain, limiter ([#131]),
  and string resonator ([#143]) effects
- Curves are now registered within the synth but cannot be referenced yet ([#96])
- Corrected a bug where the VST plugin got recreated needlessly in some hosts ([#122])
- Added a "panic button" API that kills voices ([#122])
- Corrected a potential overflow for CC names ([930bfd])
- Added support for more generators using wavetables ([#61])
- Added support for the `oscillator` opcode, to create generators from files ([#128])
- Generators using wavetables are now correctly tuned ([#126])
- The stereo panning stage of the process was corrected;
  width is now set to 100% by default as it should,
  and panning is properly applied ([1faa7f], [b55171], [#133])
- The logging API can be used to set a log filename ([a6cbb4])
- Corrected errors in the performance report script related to display values
  (file names and histogram range)
- Reworked the parser; the new one is more efficient,
  and can indicate error/warning ranges ([#130])
- The VST plugin now reloads the file automatically, like the LV2 plugin ([#139])
- The max number of CCs was increased to 512, to accomodate some libraries that use cc300 modifiers.
- The engine uses floating point values internally for midi events ([#137]); this prepares it for high-resolution midi down the line.
- Fixes some realtime synchronization issues in the VST ([#140])
- Added support for `note_polyphony`, `polyphony`, and `note_selfmask` ([#142])
- Added support for `pitch_cc` and `tune_cc` modifiers ([#142])
- The modifier support was overhauled; all regions can now have multiple CCs modifying the same target ([#142]).
- Corrected bugs and differences with Cakewalk/ARIA in the ADSR envelope ([#136], [#129])
- Improved performance of the amplitude stage gain of the rendering process ([#145])
- The VST3 are now a submodule; more architecture targets have been added
  ([#158], [#147], patch proposed by hexdump0815)

[930bfd]: https://github.com/sfztools/sfizz/commit/930bfd
[1faa7f]: https://github.com/sfztools/sfizz/commit/1faa7f
[b55171]: https://github.com/sfztools/sfizz/commit/b55171
[a6cbb4]: https://github.com/sfztools/sfizz/commit/a6cbb4
[#61]:  https://github.com/sfztools/sfizz/pull/61
[#96]:  https://github.com/sfztools/sfizz/pull/96
[#105]: https://github.com/sfztools/sfizz/pull/105
[#110]: https://github.com/sfztools/sfizz/issues/110
[#111]: https://github.com/sfztools/sfizz/pull/111
[#118]: https://github.com/sfztools/sfizz/issues/118
[#120]: https://github.com/sfztools/sfizz/pull/120
[#121]: https://github.com/sfztools/sfizz/pull/121
[#122]: https://github.com/sfztools/sfizz/pull/122
[#126]: https://github.com/sfztools/sfizz/pull/126
[#128]: https://github.com/sfztools/sfizz/pull/128
[#129]: https://github.com/sfztools/sfizz/issues/129
[#130]: https://github.com/sfztools/sfizz/pull/130
[#131]: https://github.com/sfztools/sfizz/pull/131
[#133]: https://github.com/sfztools/sfizz/issues/133
[#136]: https://github.com/sfztools/sfizz/pull/136
[#137]: https://github.com/sfztools/sfizz/pull/137
[#139]: https://github.com/sfztools/sfizz/pull/139
[#140]: https://github.com/sfztools/sfizz/pull/140
[#142]: https://github.com/sfztools/sfizz/pull/142
[#143]: https://github.com/sfztools/sfizz/pull/143
[#145]: https://github.com/sfztools/sfizz/pull/145
[#147]: https://github.com/sfztools/sfizz/issues/147
[#158]: https://github.com/sfztools/sfizz/pull/158
