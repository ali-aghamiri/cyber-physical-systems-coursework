# Cyber-Physical Systems — coursework and paper study

Selected work from a graduate **Advanced Real-Time and Embedded Systems / Cyber-Physical Systems** course at the University of Tehran. This repository contains my own paper reviews, project analysis, presentation, and environment setup notes. The documents are mainly in Persian; this page is an English guide.

## Project: reactor-based programming on an RTOS

I studied [*Beyond the Threaded Programming Model on Real-Time Operating Systems*](https://doi.org/10.4230/OASIcs.NG-RES.2023.3) and its use of Lingua Franca reactors on Zephyr. My work focused on the motivation for deterministic, timed event coordination in embedded applications, the paper's comparison with threaded C, and the practical steps needed to set up a Zephyr/Lingua Franca environment.

| Artifact | Content |
| --- | --- |
| [Paper analysis](project/paper-analysis-fa.pdf) | Persian technical discussion of the paper's design and evaluation |
| [Presentation](project/presentation-en.pdf) | English slides on reactors, embedded patterns, and evaluation |
| [Environment notes](project/zephyr-lf-setup-fa.pdf) | Historical Zephyr and Lingua Franca setup exploration |

The [project guide](project/README.md) explains the scope of these artifacts. Benchmark figures discussed in the paper belong to its authors; this repository does not claim an independent reproduction of those experiments.

## Paper reviews

| # | Paper and topic | My review |
| --- | --- | --- |
| 1 | *The Robotization of Extreme Automation: The Balance Between Fear and Courage* — collaborative robotics and automation | [Persian PDF](reviews/01-robotization-extreme-automation-fa.pdf) |
| 2 | *Timing Anomalies in Dynamically Scheduled Microprocessors* — worst-case execution-time analysis | [Persian PDF](reviews/02-timing-anomalies-fa.pdf) |
| 3 | [*An Industrial View on the Common Academic Understanding of Mixed-Criticality Systems*](https://doi.org/10.1007/s11241-018-9308-9) — industry and safety standards | [Persian PDF](reviews/03-industrial-mixed-criticality-fa.pdf) |
| 4 | *Multi-Model Systems – an MCS by Any Other Name* — task models and criticality | [Persian PDF](reviews/04-multi-model-systems-fa.pdf) |
| 5 | [*Resilient Scheduling of Energy-Variable Weakly-Hard Real-Time Systems*](https://doi.org/10.1145/3139258.3139282) — energy-aware scheduling | [Persian PDF](reviews/05-energy-variable-scheduling-fa.pdf) |

A short [seminar note on zero-knowledge proofs for CPS/IoT](notes/cps-seminar-zero-knowledge-fa.pdf) is also included.

## Attribution and public scope

The linked PDFs are my own course notes, reviews, and presentation. Original research articles, instructor slides, and other third-party course materials are not redistributed. Student ID numbers have been removed from the public PDF copies. No source code for the Lingua Franca benchmark was present in the course folder, so this repository presents the documented paper study and setup work rather than an executable benchmark.
