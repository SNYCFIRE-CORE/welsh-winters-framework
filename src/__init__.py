"""
Welsh-Winters Balance Framework

A quantitative framework for measuring and preventing AI hallucination
through balanced human-AI interaction patterns.
"""

__version__ = "1.0.0"
__author__ = "Welsh-Winters Research Team"

from .analyzer import BalanceAnalyzer
from .patterns import TechnicalPatterns, EmotionalPatterns
from .metrics import calculate_balance, phase_detector

__all__ = [
    'BalanceAnalyzer',
    'TechnicalPatterns', 
    'EmotionalPatterns',
    'calculate_balance',
    'phase_detector'
]