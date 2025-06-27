---
layout: default
title: Fantasy Map
---

<link rel="stylesheet" href="assets/theme.css">

<!-- Load Mermaid and start it -->
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
  mermaid.initialize({ startOnLoad: true, htmlLabels: true });
</script>

Welcome to **Fantasy Map** – an evolving guide to whimsical & world-building reads.

```mermaid
{% include_relative map.mmd %}
