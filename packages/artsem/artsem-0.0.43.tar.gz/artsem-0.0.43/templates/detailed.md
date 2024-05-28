{# templates/detailed.md #}

# DETAILED ANALYSIS RESULTS
## Summary

- **{{analysis.count_targets()}}** files analyzed

---

{% for tg in analysis %}
## {{tg.filename}}

|Algorithm|Hash|
|:-------:|:---:|
|MD5|{{tg.hash.md5}}|
|SHA1|{{tg.hash.sha1}}|
|SHA256|{{tg.hash.sha256}}|

{{tg.probes.to_string()}}


{% endfor %}
