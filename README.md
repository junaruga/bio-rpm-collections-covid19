# Bio RPM Collections COVID-19

This project is to enable the RPM based nf-core pipelines for COVID-19 analysis on multiple CPU architectures, solving the following 2 challenges.

1. Some of the bio tools do not work on non-Intel (x86_64) CPUs. This prevents us from running the COVID-19 analysis on non-x86_64 CPU based HPC, even when PowerPC (ppc64le) and ARM (aarch64) based HPC have a big impact in the HPC market share.
2. In the HPC running RHEL and CentOS, the bio tools RPM packages are used to manage them in a secure and consumable manner. Even while there are the needs, there are relatively a small number of the RPM packages.

## Long description

See [this page](doc/long_description.md).

## Dependency software packages for pipelines

Run the following command to see the list.

```
$ cat nf-core/dependencies/* | sort | uniq -c | sort -n -r
```

Working in progress with the Google spread sheet [here](https://docs.google.com/spreadsheets/d/1tApLhVqxRZ2VOuMH_aPUgFENQJfbLlB_PFH_Ah_q7hM/edit?usp=sharing).
