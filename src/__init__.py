"""
Welsh-Winters Balance Framework

A quantitative framework for measuring and preventing AI hallucination
through balanced human-AI interaction patterns.
"""

__version__ = "1.1.0"
__author__ = "SYNCFIRE Team"

from .analyzer import BalanceAnalyzer
from .comprehensive_analyzer import ComprehensiveAnalyzer
from .patterns import TechnicalPatterns, EmotionalPatterns
from .metrics import calculate_balance, phase_detector

__all__ = [
    'BalanceAnalyzer',
    'ComprehensiveAnalyzer',
    'TechnicalPatterns', 
    'EmotionalPatterns',
    'calculate_balance',
    'phase_detector'
]from .consciousness import ConsciousnessEngine
