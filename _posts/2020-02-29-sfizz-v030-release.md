---
title: "sfizz v0.3.0 release"
author: "redtide"
---
- Added filter and EQ handling (the `filN_...` and `eqN_...` opcodes).
  There are also no limits to the amount of filters and EQs you can slap on each
  region beyond your CPU.
  Most if not all of the relevant filter types from the SFZ v2 spec are supported.
- Added a new command-line option for the JACK client to set the client's name ([#75], [#76]).
- Added initial MIDNAM support ([#79]).
  The MIDNAM shows the named CCs in the SFZ file for now.
- Reworked the parsing code for faster dispatching and better handling of complex
  opcodes with multiple parameters in their opcode name ([#40]).
- Reworked the panning and stereo image process. The new process uses tabulated
  functions and avoid expensive calls to compute sine and cosine functions ([#47], [#56]).
- Added a crude `*noise` generator. This generator is a bit expensive for what
  it does but it's mostly useful to test the filters.
- Added fine timings within the callbacks for performance improvements
  and regression testing ([#65]).
- Corrected a bug with Ardour where saving a session with no file loaded would
  crash on reopening.
- Corrected a bug where voices triggered on key off would never end and fill up
  the polyphony ([#63]).
- Improved and completed CI on all platforms.

[#40]: https://github.com/sfztools/sfizz/pull/40
[#47]: https://github.com/sfztools/sfizz/pull/47
[#56]: https://github.com/sfztools/sfizz/pull/56
[#63]: https://github.com/sfztools/sfizz/issues/63
[#65]: https://github.com/sfztools/sfizz/pull/65
[#75]: https://github.com/sfztools/sfizz/issues/75
[#76]: https://github.com/sfztools/sfizz/pull/76
[#79]: https://github.com/sfztools/sfizz/issues/79
