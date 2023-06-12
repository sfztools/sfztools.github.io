---
title: "Opcodes Support Status"
---
<div class="d-flex justify-content-between mb-2">
  <a class="btn btn-primary btn-sm" role="button" href="./opcodes">View detailed list</a>
  <div>The classification of opcodes follows the list over at
    <a href="https://sfzformat.com/">sfzformat.com</a>.
  </div>
</div>

{%- include sfizz/status/table.liquid %}

<div class="d-flex justify-content-center gap-2 mt-2">
  <span class="badge text-bg-success">Complete</span>
  <span class="badge text-bg-warning">Work In Progress</span>
</div>

## Supported Headers

All headers, including <[sample]> are currently supported.

## Supported Operating Systems

{% for os in site.data.sfizz.support.os %}
- {{ os.name }}{%-comment-%} no paragraph {%-endcomment-%}
{% endfor %}


[here]:   opcodes
[sample]: https://sfzformat.com/headers/sample
