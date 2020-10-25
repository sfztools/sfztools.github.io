---
title: "sfizz v0.5.1 release"
author: "redtide"
date: "2020-10-25T13:08:26+0100"
---
- Corrected race conditions that appeared with the new thread and file pools
  (#507 #508 #514 #521)
- Take the internal oversampling factor into account for loop points, and solve
  an issue where loop points specified in sfz files were not taken into account
  (#506)
- Fix an implementation error for the internal hash function when applied
  on a single byte (#512)
- Knobs are linear in the AU plugin (#517)
- Fix a crash in VSTGUI (#520)
- Fix the resource path in the LV2 plugin under windows (#524)
- Add MacOS make install rules (#525)
