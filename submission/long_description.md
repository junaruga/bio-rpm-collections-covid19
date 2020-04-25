Bio Tools RPM Collections COVID-19 project is to enable the RPM based COVID-19 analysis pipelines on the multiple CPU architectures.

## Background

One of the key factors to fight COVID-19 is the DNA/RNA analysis by the bioinformatics tools.
The way to make the analysis deliverable and maintainable in a secure manner on RPM based Linux distributions such as Red Hat Enterprise Linux (RHEL), CentOS, Fedora and etc is thriving the RPM packages eco-system.

The prioritized selection for the RPM packages is decided by the actual COVID-19 analysis pipelines. In this project, we use nf-core pipelines [1] that is a community effort to collect a set of analysis pipelines built using Nextflow [2]. Nextflow is the workflow software. It's possible to run the containerized pipeline in a portable manner.

The analysis pipeline is mainly executed in an High Performance Computing (HPC) environment. And by enabling the pipeline on the ppc64le based HPC environment, we can maximize the HPC resources to fight COVID-19.

## Targets and Strategies

There are 2 project targets.

1. Enabling the bio tools RPM packages on x86_64 and ppc64le, optionally other CPU architectures for Fedora and Extra Packages for Enterprise Linux (EPEL) 7 and 8. EPEL enables the packages on RHEL and CentOS. The RPM packages are maintained on Fedora dist-git repositories, and listed up on the Fedora Koschei biology tag group [3] linked from Fedora Medical Special Interest Group (SIG) page [4].
2. Enabling the nf-core pipelines on ppc64le based HPC, benchmarking it.

We use the following nf-core pipelines. First 3 pipelines are essential. Others are certainly relevant.
We repeat the "1." and "2." target for each pipeline in order in an agile manner.

* nf-core/nanoseq: Nanopore DNA/RNA sequencing analysis
* nf-core/artic: COVID-19 analysis
* nf-core/viralrecon: COVID-19 analysis
* nf-core/scrnaseq: Single-cell analysis
* nf-core/smartseq2: Single-cell analysis
* nf-core/sarek: Whole-genome analysis
* nf-core/mag: Meta-genomics analysis
* nf-core/bcellmagic: Immune response analysis

## Challenges

Currently there are 2 challenges.

1. Some of the bio tools are only supported in x86_64 CPU architecture.
2. A few of the bio tools used in the nf-core pipelines are not fully open-sourced.

For the first challenge, the reason is the use of SIMD intrinsics or Intel specific assembly code.
As a solution, we will use SIMDe (SIMD Everywhere) library [5] to enable the multiple CPU environment, contributing to the upstream projects.
SIMDe has already been used or evaluated positively in a few bio tools.

For the second challenge, instead we consider to use the fully open sourced alternative or the fully open sourced client tool to access the function on the server.

## Collaboration

We collaborate with other organizations or communities as a possibility, such as Fedora Medical SIG, Debian Med team [6], nf-core, Nextflow and etc.
Please note that apart from the target of this project, when enabling the nf-core pipeline on aarch64 (ARM 64-bit) CPU architecture, we might use an ARM based HPC by a collaboration.

## Rererences

* [1] https://nf-co.re/
* [2] https://www.nextflow.io/
* [3] https://koschei.fedoraproject.org/groups/biology?untracked=1
* [4] https://fedoraproject.org/wiki/SIGs/Medical
* [5] https://github.com/nemequ/simde
* [6] https://www.debian.org/devel/debian-med/
