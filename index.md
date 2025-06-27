---
layout: default
title: Fantasy Map
---

<!-- theme stylesheet (optional, keep if you already added it) -->
<link rel="stylesheet" href="assets/theme.css">

<!-- 1️⃣  Load Mermaid from jsDelivr and auto-start it -->
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
  mermaid.initialize({ startOnLoad: true, htmlLabels: true });   /* renders on page-load & keeps <a> links */ :contentReference[oaicite:0]{index=0}
</script>

Welcome to **Fantasy Map** – an evolving guide to whimsical & world-building reads.

<!-- 2️⃣  Wrap the generated code in a mermaid fence -->
```mermaid
{% include_relative map.mmd %}
