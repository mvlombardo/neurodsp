"""
test_plts_filt.py
Test filtering plots
"""

import numpy as np
from neurodsp.filt import filter_signal
from neurodsp.plts.filt import plot_frequency_response
from .util import plot_test


@plot_test
def test_plot_frequency_response_call():
    """
    Confirm frequency response plotting function is called and makes a plot
    """

    # Test plotting through the filter function
    sig = np.random.randn(2000)
    fs = 1000
    sig_filt, kernel = filter_signal(sig, fs, 'bandpass', (8, 12),
        plot_freq_response=True, return_kernel=True, verbose=False)
    assert True


@plot_test
def test_plot_frequency_response():
    """
    Confirm frequency response plotting function works directly
    """

    # Test plotting through the filter function
    sig = np.random.randn(2000)
    fs = 1000
    sig_filt, kernel = filter_signal(sig, fs, 'bandpass', (8, 12), return_kernel=True, verbose=False)
    plot_frequency_response(fs, kernel)
    assert True
