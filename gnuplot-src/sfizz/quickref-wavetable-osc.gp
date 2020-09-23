set term svg

set grid
set xrange [0.0:1.0]
set yrange [-1.5:+1.5]
set xlabel "Time"
set ylabel "Amplitude"

sinN(x) = sin(2*pi*x)
att = 0.213

plot att*(sinN(x)+sinN(2*x)+sinN(3*x)+sinN(4*x)+sinN(5*x)+sinN(6*x)) t "Wavetable"
