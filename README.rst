In-place Tuning
===============

The idea is to optimize frequencies of all currently sounding notes
to have just intonation-like ratios.

The process involves:

- Finding pairwise relationships between currently sounding notes
- Choosing nominal starting frequencies, e.g., A=440Hz, A#=466.16, and so on
- Noticing that the nominal frequencies will in general not satisfy the desired ratios
- Modifying the frequencies as little as possible to achieve the desired ratios

This idea was inspired by videos made by Adam Neely [1]_ and work done Polansky et al [2]_.

A next step would be a moving window optimization which would allow for "just in time"
tuning for live electronic music.

The current state of the project is not robust.  This is meant as a proof of concept,
not as a "ready for production" suite.  Some simple things will fail because of how ratios
and notes are defined under the hood.  Any pull request is welcome to help fix it, but as
this is simply a one and done hobby project, I'm going to officially leave it dormant for
now.

Examples
========

Information is best obtained from the `inplacetuning` function's docstring.
A basic example is provided and can be run like this on Unix-like systems
with Python 3:

.. code:: python

    python -m examples.basic

It will produce a WAV file of a sum of sines of the unoptimized just intonation
frequencies followed by the in-place intonation optimized frequencies for
comparison.

References
==========
[1] Adam Neely's YouTube Channel https://www.youtube.com/user/havic5/videos
[2] Polansky, Larry, et al. "A mathematical model for optimal tuning systems."
    Perspectives of new music (2009): 69-110.
