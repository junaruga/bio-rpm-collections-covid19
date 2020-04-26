Bio RPM Collections COVID-19 project is to enable the RPM based pipelines for COVID-19 analysis on the multiple CPU architectures.

## Motivation

One of the key factors to fight COVID-19 is the DNA/RNA analysis by the bioinformatics (bio) tools. The way to make the analysis deliverable and maintainable in a secure manner on RPM based Linux distributions such as Red Hat Enterprise Linux (RHEL), CentOS, Fedora and etc is thriving the RPM packages eco-system.

The prioritized selection for the RPM packages is decided by the actual COVID-19 analysis pipelines. In this project, we use nf-core pipelines [1] that is a community effort to collect a set of analysis pipelines built using Nextflow [2]. Nextflow is the workflow software that can have the containerized pipeline.

The pipelines are mainly executed in an High Performance Computing (HPC) environment. We can maximize the HPC resources by enabling it on the ppc64le CPU architecture.

## Expected Results

* We provide an accessible bio tool RPM collections and the practically used nf-core pipelines for COVID-19 analysis on RHEL, CentOS, Fedora x86_64 and ppc64le CPU architectures.
* We thrive the bio tools RPM eco-system used in the RPM based Linux distributions. As almost any molecular biology technique can be used to look into some aspect of COVID-19, the RPM eco-system can widely be used beyond the COVID-19 analysis.
* We provide the benchmarking result by the analysis pipelines on ppc64le based HPC that can be the case study of the ppc64le based HPC.

## Roadmap

There are 2 project targets.

1. Enabling the bio tools RPM packages on x86_64 and ppc64le, optionally other CPU architectures for Fedora and Extra Packages for Enterprise Linux (EPEL) 7 and 8. The RPM packages are maintained on Fedora dist-git repositories, and listed up on the Fedora Koschei biology tag group [3] linked from Fedora Medical Special Interest Group (SIG) page [4].
2. Enabling the nf-core pipelines on ppc64le based HPC, benchmarking it.

We use the following nf-core pipelines. First 3 pipelines are essential. Others are certainly relevant.
We repeat the first  and second target for each pipeline in order in an agile manner.

* nf-core/nanoseq: Nanopore sequencing analysis
* nf-core/artic: COVID-19 analysis
* nf-core/viralrecon: COVID-19 analysis
* nf-core/scrnaseq: Single-cell analysis
* nf-core/smartseq2: Single-cell analysis
* nf-core/sarek: Whole-genome analysis
* nf-core/mag: Meta-genomics analysis
* nf-core/bcellmagic: Immune response analysis

## Challenges

Currently there are 2 challenges. First, some of the bio tools are only supported in x86_64 CPU architecture. We will use SIMDe (SIMD Everywhere) library [5] to support the multiple CPU architectures. Second, a few of the bio tools used in the nf-core pipelines are not fully open-sourced. Instead we consider to use the fully open sourced alternative or the client tool to access the function.

## Collaboration

We collaborate with other organizations or communities, such as Fedora Medical SIG, Debian Med team [6], nf-core, Nextflow. When enabling the pipelines on aarch64 (ARM 64-bit) CPU architecture, we have a possibility to use an ARM based HPC by a collaboration.

## Rererences

* [1] https://nf-co.re/
* [2] https://www.nextflow.io/
* [3] https://koschei.fedoraproject.org/groups/biology?untracked=1
* [4] https://fedoraproject.org/wiki/SIGs/Medical
* [5] https://github.com/nemequ/simde
* [6] https://www.debian.org/devel/debian-med/
