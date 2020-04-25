Bio Tools RPM Collections COVID-19 project is to enable the RPM based COVID-19 analysis pipelines on the multiple CPU architectures.

## Background

One of the key factors to fight COVID-19 is the COVID-19 analysis.
The way to make the COVID-19 analysis deliverable and maintainable in a secure manner on RPM based Linux distributions such as RHEL, CentOS, Fedora is thriving the RPM packages eco-system.

The prioritized selection for the RPM packages is decided by the actual COVID-19 analysis pipelines. In this project, we use nf-core pipelines [1] that is a community effort to collect a set of analysis pipelines built using Nextflow [2]. Nextflow is the workflow software. It's possible to run the containerized pipeline in a portable manner.

The analysis pipeline is mainly executed in an HPC environment. And enabling the pipeline on ppc64le CPU architecture based HPC connects maximizing the HPC resources.

## Targets

There are 2 project's targets.
1. Enabling the bio tools RPM packages on x86_64 and ppc64le, optionally other CPU architectures for Fedora and EPEL 7 and 8. When enabling it on EPEL, it is possible to use it on RHEL and CentOS. The RPM packages are managed on Fedora dist-git repositories, and listed up on the Fedora Koschei biology tag group [3] linked from Fedora Medical Special Interest Group (SIG) page [4].
2. Enabling the nf-core pipelines on ppc64le based HPC, benchmarking it.

## How?

We use the following nf-core pipelines. First 3 pipelines nanoseq, artic, and viralrecon are essential. Others are certainly relevant.

* nf-core/nanoseq: Nanopore DNA/RNA sequencing analysis
* nf-core/artic: COVID-19 analysis
* nf-core/viralrecon: COVID-19 analysis
* nf-core/scrnaseq: Single-cell analysis
* nf-core/smartseq2: Single-cell analysis
* nf-core/sarek: Whole-genome analysis
* nf-core/mag: Meta-genomics analysis
* nf-core/bcellmagic: Immune response analysis

We enable the bio tools RPMs used in a pipeline, then enable the pipeline on the RHEL ppc64le environment for each pipeline one by one in an agile manner.

## Challenges

There are 2 challenges.

1. Some of the bio tools are only supported in x86_64 CPU architecture.
2. A few of the bio tools used in the nf-core pipelines are not fully open-sourced.

For "1.", the reason is the use of SIMD intrinsics or Intel assembly code in the code.
As a solution, we will use SIMDe (SIMD Everywhere) library [5] to enable the multiple CPU environment, contributing to the upstream projects.
SIMDe has already been used or evaluated positively in popular bio-tools.

For "2.", instead we consider the fully open sourced alternative or the fully open sourced client tool to access the function on the server.

## Collaboration

We collaborate with other organizations or communities as a possibility, such as Fedora Medical SIG, Debian Med team [6], nf-core, Nextflow and etc.
Please note that apart from the target of this project, when enabling the nf-core pipeline on aarch64 (ARM 64-bit) CPU architecture, we might use the ARM based HPC by a collaboration.

## Rererences

* [1] https://nf-co.re/
* [2] https://www.nextflow.io/
* [3] https://koschei.fedoraproject.org/groups/biology?untracked=1
* [4] https://fedoraproject.org/wiki/SIGs/Medical
* [5] https://github.com/nemequ/simde
* [6] https://www.debian.org/devel/debian-med/
