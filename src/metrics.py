"""
Metrics calculation for Welsh-Winters Balance Framework
"""

from typing import List, Dict, Tuple, Optional
from enum import Enum


class CollaborationPhase(Enum):
    """Phases of human-AI collaboration based on balance patterns"""
    FOUNDATION = "Foundation Phase"
    DEVELOPMENT = "Development Phase"
    MASTERY = "Mastery Phase"
    UNKNOWN = "Unknown Phase"


def calculate_balance(technical_count: int, emotional_count: int) -> float:
    """
    Calculate Welsh-Winters Balance score
    
    Args:
        technical_count: Number of technical pattern matches
        emotional_count: Number of emotional pattern matches
        
    Returns:
        Balance score between 0.0 (pure emotional) and 1.0 (pure technical)
    """
    total = technical_count + emotional_count
    
    if total == 0:
        return 0.5  # Default to balanced if no patterns found
    
    return technical_count / total


def phase_detector(balance: float) -> CollaborationPhase:
    """
    Detect collaboration phase based on balance score
    
    Args:
        balance: Welsh-Winters Balance score
        
    Returns:
        CollaborationPhase enum value
    """
    if 0.54 <= balance <= 0.58:
        return CollaborationPhase.FOUNDATION
    elif 0.74 <= balance <= 0.86:
        return CollaborationPhase.DEVELOPMENT
    elif 0.70 <= balance <= 0.81:
        return CollaborationPhase.MASTERY
    else:
        return CollaborationPhase.UNKNOWN


def calculate_trajectory(balances: List[float]) -> Dict[str, any]:
    """
    Calculate trajectory metrics from a series of balance measurements
    
    Args:
        balances: List of balance scores over time
        
    Returns:
        Dictionary with trajectory metrics
    """
    if not balances:
        return {
            'trend': 'neutral',
            'volatility': 0.0,
            'phases_detected': [],
            'stability_score': 0.0
        }
    
    # Calculate trend
    if len(balances) > 1:
        start_avg = sum(balances[:len(balances)//3]) / (len(balances)//3)
        end_avg = sum(balances[-len(balances)//3:]) / (len(balances)//3)
        
        if end_avg > start_avg + 0.1:
            trend = 'technical_shift'
        elif end_avg < start_avg - 0.1:
            trend = 'emotional_shift'
        else:
            trend = 'stable'
    else:
        trend = 'insufficient_data'
    
    # Calculate volatility
    if len(balances) > 1:
        differences = [abs(balances[i] - balances[i-1]) for i in range(1, len(balances))]
        volatility = sum(differences) / len(differences)
    else:
        volatility = 0.0
    
    # Detect phases
    phases_detected = []
    for balance in balances:
        phase = phase_detector(balance)
        if phase != CollaborationPhase.UNKNOWN and phase not in phases_detected:
            phases_detected.append(phase)
    
    # Calculate stability score (inverse of volatility, normalized)
    stability_score = max(0, 1 - (volatility * 10))
    
    return {
        'trend': trend,
        'volatility': volatility,
        'phases_detected': [phase.value for phase in phases_detected],
        'stability_score': stability_score,
        'start_balance': balances[0] if balances else None,
        'end_balance': balances[-1] if balances else None,
        'average_balance': sum(balances) / len(balances) if balances else None
    }


def hallucination_risk_score(balance: float, volatility: float) -> float:
    """
    Calculate hallucination risk based on balance and volatility
    
    Lower scores indicate lower hallucination risk
    
    Args:
        balance: Current Welsh-Winters Balance
        volatility: Balance volatility measure
        
    Returns:
        Risk score between 0.0 (low risk) and 1.0 (high risk)
    """
    # Optimal balance is around 0.5-0.7
    balance_deviation = abs(balance - 0.6)
    
    # High volatility increases risk
    volatility_factor = min(volatility * 2, 1.0)
    
    # Extreme imbalance increases risk
    if balance < 0.2 or balance > 0.9:
        extreme_factor = 0.5
    else:
        extreme_factor = 0.0
    
    risk_score = (balance_deviation + volatility_factor + extreme_factor) / 3
    
    return min(max(risk_score, 0.0), 1.0)