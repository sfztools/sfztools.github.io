---
title: Home
no_title_header: true
---
`sfizz` is a sample-based musical synthesizer.

It features the well-established [SFZ instrument format] at its core, which permits to use
existing instrument libraries, or create personal instruments with ease.

Not only is `sfizz` ready-to-use as an instrument plugin of its own, the library allows
developers to create instruments of their own, taking advantage of the abilities of SFZ.

<p>
  <a
    class="btn btn-success"
    role="button"
    href="downloads"
  ><i class="fas fa-download pr-2" aria-hidden="true"></i>Get sfizz</a></p>

## Features

- **SFZ compatible**

`sfizz` supports SFZv1, and is partially compatible with SFZv2, the current revision of the
instrument specification. The objective is to achieve a high level of SFZ compatibility,
and the quality improves with every release.

- **Ready-to-use**

The synthesizer is available as audio workstation plugins,
in [VST3i], [Audio Unit] and [LV2] formats.
The more advanced users may also use a standalone [JACK] client.

- **For instrument makers**

The hot reload ability helps you to design intruments. You are able to edit your custom
instrument and test the change on the fly, without having to interact with the software
manually.

- **Low memory footprint**

The streaming system loads the sounds on demand, and dynamically reclaims the memory of
sounds which are no longer used. This keeps the RAM memory requirement at minimum.

## See in action

Some artists have demonstrated music creation using sfizz, independently of this project.
You are welcome to watch the media and support their work.

- [How to use Virtual Playing Orchestra in Ardour] by unfa


[JACK]:                     https://jackaudio.org/
[LV2]:                      https://lv2plug.in/
[VST3i]:                    https://www.steinberg.net/en/company/technologies/vst3.html
[Audio Unit]:               https://support.apple.com/guide/logicpro/lgcp22a0dab0/mac
[SFZ instrument format]:    https://sfzformat.com/
[Download]:                 downloads
[How to use Virtual Playing Orchestra in Ardour]: https://www.youtube.com/watch?v=xvowEZqgflw
