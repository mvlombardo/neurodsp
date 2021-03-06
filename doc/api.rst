.. _api_documentation:

=================
API Documentation
=================

.. currentmodule:: neurodsp

Time-Frequency analysis
=======================

.. autosummary::
  :toctree: generated/

  filt.filter_signal
  timefrequency.phase_by_time
  timefrequency.amp_by_time
  timefrequency.freq_by_time

Spectral analysis
=================

.. autosummary::
   :toctree: generated/

   spectral.compute_spectrum
   spectral.compute_scv
   spectral.spectral_hist
   spectral.morlet_transform
   spectral.rotate_powerlaw

Rhythmic analysis
=================

.. autosummary::
  :toctree: generated/

  burst.detect_bursts_dual_threshold
  burst.compute_burst_stats
  swm.sliding_window_matching
  laggedcoherence.lagged_coherence

Signal simulation
=================

.. autosummary::
  :toctree: generated/

  sim.sim_filtered_noise
  sim.sim_synaptic_noise
  sim.sim_ou_process
  sim.sim_variable_powerlaw
  sim.sim_oscillator
  sim.sim_noisy_oscillator
  sim.sim_bursty_oscillator
  sim.sim_noisy_bursty_oscillator
  sim.sim_jittered_oscillator
