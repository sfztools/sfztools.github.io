---
title: "sfizz v0.2.0 release"
author: "redtide"
---
- Added an LV2 plugin version.
- The parser now falls back to case-insensitive search if it doesn't find the
  sample file in its current path ([#28]), so that the behavior of SFZ libraries
  on case-sensitive filesystems will match Windows and macOS default
  case-insensitive filesystems.
- The file now reload automatically on file change,
  and you can force a reload if necessary ([#17]).
- Corrected a bug where memory would be read past the end of the file in memory,
  generating artifacts.
- Corrected a bug where the real-time queue handling background loading
  of the voices would fail spuriously.
- Corrected a bug where in the LV2 plugin
  the unknown opcode list was truncated ([#18]).
- Added dynamic updates for the current modifiers
  (panning, stereo image, volume and amplitude mainly) ([#19], [#28])
- Added timing for callbacks and file loading times.
- Added support for pitch bends ([#6]) as well as pitch-bend activation for regions
  ([lobend] and [hibend] opcodes).
- The JACK client will warn you instead of crashing
  if you do not give it a file to load ([#27]).
- Added a windows build process for both the shared library and the LV2.
  `sfizz` now builds on all major platforms.

[#6]:     https://github.com/sfztools/sfizz/issues/6
[#17]:    https://github.com/sfztools/sfizz/issues/17
[#18]:    https://github.com/sfztools/sfizz/issues/18
[#19]:    https://github.com/sfztools/sfizz/issues/19
[#27]:    https://github.com/sfztools/sfizz/issues/27
[#28]:    https://github.com/sfztools/sfizz/pull/28
[lobend]: https://sfzformat.com/opcodes/lobend
[hibend]: https://sfzformat.com/opcodes/hibend
