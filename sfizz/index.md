---
title: "Home"
layout: "home"
---
`sfizz` is a software library to play audio in [SFZ format],
it is also available as a [JACK] standalone client, [LV2] plugin, and a currently
experimental [VST3] plugin.

## Dependencies

`sfizz` depends mainly on the [libsndfile] library.
In order to build also the standalone client and other demos, you need to
install also the [JACK] Audio Connection Kit library.
In Debian-based distributions, this translates into

```bash
sudo apt install libjack-jackd2-dev libsndfile1-dev
```

The benchmarks depend on the [benchmark] library.
If you wish to build the benchmarks you should either build it from source and
install the static library, or use the library from your distribution.
Ubuntu proposes a `libbenchmark-dev` package that does this.

[benchmark]:  https://github.com/google/benchmark/
[JACK]:       https://jackaudio.org/
[libsndfile]: http://mega-nerd.com/libsndfile/
[LV2]:        https://lv2plug.in/
[VST3]:       https://www.steinberg.net/en/company/technologies/vst3.html
[SFZ format]: https://sfzformat.com/
