---
title: "Opcodes Support Status"
---
The detailed table of supported opcodes is [here]; its classification follows
the list over at <https://sfzformat.com/>.

{% include sfizz/sfz_support.liquid %}

<p class="text-center">
	<span class="badge badge-success">Complete</span>
	<span class="badge badge-warning">Work In Progress</span>
</p>

## Supported Headers

All headers except <[sample]> are currently supported.

## Supported Operating Systems

{% for os in site.data.sfizz.support.os %}
- {{ os.name }}{%-comment-%} no paragraph {%-endcomment-%}
{% endfor %}

[here]:   opcodes
[sample]: https://sfzformat.com/headers/sample
