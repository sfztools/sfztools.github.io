---
title: "Quick Reference"
---
## Contents
{:.no_toc}
1. toc ordered list
{:toc}

## How to do X in sfizz SFZ?

This section describes basic use of some SFZ features, illustrated with examples.
Some of these features may be not very widely implemented in SFZ players, or specific to sfizz.

### Oscillators

#### Basic oscillator

The most basic form of oscillator is obtained by using one of the predefined waveforms.
The name `*saw` provides the sawtooth oscillator.

```
<region>
sample=*saw
```

#### Detuned oscillator

This creates a pair of sawtooth waves. The second sawtooth is detuned by 50
cents, making the pair create together the impression of a fuller sound.

```
<region>
sample=*saw

<region>
sample=*saw
pitch=50
```

![quickref-detune-osc](/assets/img/sfizz/quickref-detune-osc.svg)

#### Wavetable oscillator

This creates an oscillator with a custom waveform, which is loaded from an
audio file. This file contains exactly one period of signal, and its
sample rate is disregarded.

One way to create wavetables is to use the `WCreate` utility.
- Documentation, and Windows software: [futur3soundz](https://www.futur3soundz.com/wavetable-synthesis)
- macOS and Linux software: [WaveTableTools](https://github.com/sfztools/WaveTableTools)

The example refers to a wave composed of the 6 first harmonics:
`WCreate 1024 "x<6" sine_hrm_06.wav`

The `oscillator` opcode indicates that we are dealing with a file which is a
wavetable.
Starting with sfizz 0.5.0, `oscillator` is optional: an audio file with less
than 3000 frames is considered to be a wavetable.

```
<region>
sample=sine_hrm_06.wav
oscillator=on
```

![quickref-wavetable-osc](/assets/img/sfizz/quickref-wavetable-osc.svg)

#### Unison oscillator

This creates an array of oscillators which are spread out in gain and frequency
relative to the fundamental, and arranged in opposite fashion in left and right
channels to create a stereo effect.

The unison mode is enabled when `oscillator_multi` is 3 or more, and
`oscillator_mode` is default or 0.

The example creates an array of 5 sawtooth waves, spread using a detuning interval
set to 50 cents. (a "supersaw")

```
<region>
sample=*saw
oscillator=on
oscillator_multi=5
oscillator_detune=50
```

#### Ring modulation oscillator (experimental)

When the opcodes are set to `oscillator_mode=0` and `oscillator_multi=2`,
this configures a pair of oscillators for ring modulation.

The modulator, whose frequency is determined by `oscillator_detune` in cents,
modulates the amplitude of the carrier oscillator, with a depth determined by
`oscillator_mod_depth` expressed as a percentage.

```
<control>
set_hdcc21=0.5

<region>
sample=*saw
oscillator=on
oscillator_mode=0
oscillator_multi=2
oscillator_detune=25
oscillator_mod_depth=100
oscillator_mod_depth_oncc21=100
```

#### FM oscillator (experimental)

A 2-operator FM arrangement can be constructed by setting `oscillator_mode=2`.

The frequency of the modulator is determined by `oscillator_detune` in cents,
and the FM index by `oscillator_mod_depth`. The depth is expressed as a
percentage, which means that the value `100` represents the FM index `1.0`.

```
<control>
set_cc21=100

<global>
volume=-3.0

<region>
sample=*sine
oscillator=on
oscillator_mode=2
oscillator_detune=5
oscillator_mod_depth=100
oscillator_mod_depth_oncc21=1000
```

### Filters

### Modulation

### Effects
