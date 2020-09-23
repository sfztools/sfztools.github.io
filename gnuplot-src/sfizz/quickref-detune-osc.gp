set term svg

semi2ratio(semi) = 2.0 ** (semi / 12.0)
cents2ratio(cents) = semi2ratio(cents / 100.0)

periodicity_(x, f) = fmod(x, 1.0/f)/(1.0/f)
wave_saw(x, f) = 2.0*(1.0-periodicity(x, f))-1.0

f1=1.0
f2=f1*cents2ratio(50.0)
t0=5.5

set grid
set xrange [t0:t0+2.0]
set yrange [-2.0:+2.0]
set xlabel "Time"
set ylabel "Amplitude"

plot wave_saw(x, f1)+wave_saw(x, f2) t "Detuned saw"
