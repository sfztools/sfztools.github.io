
GP_INPUTS := $(wildcard sfizz/*.gp)
SVG_OUTPUTS := $(GP_INPUTS:%.gp=../assets/img/%.svg)

$(warning $(GP_INPUTS))
$(warning $(SVG_OUTPUTS))

all: $(SVG_OUTPUTS)

clean:
	rm -f $(SVG_OUTPUTS)

.PHONY: all clean

../assets/img/%.svg: %.gp
	@mkdir -p $(dir $@)
	gnuplot $< > $@
