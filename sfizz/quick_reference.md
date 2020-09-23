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

### Filters

### Modulation

### Effects
