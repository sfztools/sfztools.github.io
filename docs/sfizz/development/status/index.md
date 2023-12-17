---
title: "Opcodes Support Status"
---
<div class="d-flex justify-content-between">
  <a class="btn btn-primary btn-sm" role="button" href="opcodes">View detailed list</a>
  <div>The classification of opcodes follows the list over at
    <a href="https://sfzformat.com/">sfzformat.com</a>.
  </div>
</div>

{% include "sfizz/sfz_support_table.j2" %}

<div class="d-flex justify-content-center gap-2">
  <span class="badge text-bg-success">Complete</span>
  <span class="badge text-bg-warning">Work In Progress</span>
</div>

## Supported Headers

All headers, including <[sample]>
are currently supported.

## Supported Operating Systems

<ul>
{% for os in sfizz_support_macros.os %}
  <li>{{ os.name }}</li>
{% endfor %}
</ul>


[sample]: https://sfzformat.com/headers/sample

