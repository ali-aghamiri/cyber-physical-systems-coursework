# Lingua Franca on Zephyr: project study

The course project examined Jellum et al., [*Beyond the Threaded Programming Model on Real-Time Operating Systems*](https://doi.org/10.4230/OASIcs.NG-RES.2023.3) (NG-RES 2023). The paper describes a Lingua Franca embedded target built on Zephyr and compares its reactor model with threaded C implementations.

My [analysis](paper-analysis-fa.pdf) and [slides](presentation-en.pdf) explain why shared-memory threads complicate reactive embedded programs, how reactors express events and timing, and which design patterns and performance dimensions the paper evaluates. The [setup report](zephyr-lf-setup-fa.pdf) records my attempt to prepare a Linux/Zephyr/Lingua Franca environment. It is a record of the 2023–24 course work, not an installation guide for current tool versions.

The source folder contained these documents, but no Lingua Franca source files or reproducible benchmark measurements. The presentation summarizes results reported by the paper's authors; it does not represent new measurements from this project.
