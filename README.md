# Bio RPM Collections COVID-19

This project is to enable the RPM based nf-core pipelines for COVID-19 analysis on multiple CPU architectures, solving the following 2 challenges.

1. Some of the bio tools do not work on non-Intel (x86_64) CPUs. This prevents us from running the COVID-19 analysis on non-x86_64 CPU based HPC, even when PowerPC (ppc64le) and ARM (aarch64) based HPC have a big impact in the HPC market share.
2. In the HPC running RHEL and CentOS, the bio tools RPM packages are used to manage them in a secure and consumable manner. Even while there are the needs, there are relatively a small number of the RPM packages.

## Motivation

One of the key factors to fight COVID-19 is the DNA/RNA analysis by the bioinformatics (bio) tools. The way to make the analysis deliverable and maintainable in a secure manner on RPM based Linux distributions such as Red Hat Enterprise Linux (RHEL), CentOS, Fedora and etc, is thriving the RPM packages eco-system.

The prioritized selection for the RPM packages is decided by the actual COVID-19 analysis pipelines. In this project, we use nf-core pipelines [1] that is a community effort to collect a set of analysis pipelines built using Nextflow [2]. Nextflow is the workflow software that can have the containerized pipeline.

The pipelines are mainly executed in an High Performance Computing (HPC) environment. We can maximize the HPC resources by enabling it on the PowerPC (ppc64le), ARM (aarch64) CPU architecture.

## Expected Results

* We provide an accessible bio tool RPM collections and the practically used nf-core pipelines for COVID-19 analysis on RHEL, CentOS, Fedora x86_64, ppc64le and aarch64 CPU architectures.
* We thrive the bio tools RPM eco-system used in the RPM based Linux distributions. As almost any molecular biology technique can be used to look into some aspect of COVID-19, the RPM eco-system can widely be used beyond the COVID-19 analysis.
* We provide the benchmarking result by the analysis pipelines on ppc64le and aarch64 based HPCs that can be the case study of them.

## Roadmap

See [Roadmap](https://github.com/junaruga/bio-rpm-collections-covid19/wiki/Roadmap).

Working in progress with the Google spread sheet [here](https://docs.google.com/spreadsheets/d/1tApLhVqxRZ2VOuMH_aPUgFENQJfbLlB_PFH_Ah_q7hM/edit?usp=sharing).


Run the following command to see a list of the dependency software packages for pipelines

```
$ cat nf-core/dependencies/* | sort | uniq -c | sort -n -r
```

## Challenges

Currently there are 2 challenges. First, some of the bio tools are only supported in x86_64 CPU architecture. We will use SIMDe (SIMD Everywhere) library [3] to support the multiple CPU architectures. Second, a few of the bio tools used in the nf-core pipelines are not fully open-sourced. Instead we consider to use the fully open sourced alternative or the client tool to access the function.

## Collaboration

We collaborate with other organizations or communities, such as Fedora Medical SIG, Debian Med team [4], nf-core, Nextflow. When enabling the pipelines on aarch64 (ARM 64-bit) CPU architecture, we have a possibility to use an ARM based HPC by a collaboration.

## Rererences

* [1] https://nf-co.re/
* [2] https://www.nextflow.io/
* [3] https://github.com/nemequ/simde
* [4] https://www.debian.org/devel/debian-med/
