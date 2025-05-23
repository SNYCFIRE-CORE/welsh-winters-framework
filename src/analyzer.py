"""
Core analyzer for Welsh-Winters Balance calculation
"""

import re
from typing import Dict, List, Tuple, Optional
from .patterns import TechnicalPatterns, EmotionalPatterns
from .metrics import calculate_balance


class BalanceAnalyzer:
    """Analyzes text to calculate Welsh-Winters Balance score"""
    
    def __init__(self):
        self.technical_patterns = TechnicalPatterns.get_patterns()
        self.emotional_patterns = EmotionalPatterns.get_patterns()
        
    def analyze_text(self, text: str) -> float:
        """
        Analyze text and return Welsh-Winters Balance score
        
        Args:
            text: Input text to analyze
            
        Returns:
            Balance score between 0.0 and 1.0
        """
        technical_count = self._count_patterns(text, self.technical_patterns)
        emotional_count = self._count_patterns(text, self.emotional_patterns)
        
        return calculate_balance(technical_count, emotional_count)
    
    def analyze_conversation(self, messages: List[Dict[str, str]]) -> Dict[str, any]:
        """
        Analyze a full conversation with multiple messages
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            
        Returns:
            Dictionary with analysis results including overall balance and per-turn metrics
        """
        results = {
            'total_messages': len(messages),
            'turn_balances': [],
            'technical_count': 0,
            'emotional_count': 0,
            'phase_evolution': []
        }
        
        for i, message in enumerate(messages):
            text = message.get('content', '')
            technical = self._count_patterns(text, self.technical_patterns)
            emotional = self._count_patterns(text, self.emotional_patterns)
            balance = calculate_balance(technical, emotional)
            
            results['turn_balances'].append({
                'turn': i + 1,
                'role': message.get('role', 'unknown'),
                'balance': balance,
                'technical': technical,
                'emotional': emotional
            })
            
            results['technical_count'] += technical
            results['emotional_count'] += emotional
        
        results['overall_balance'] = calculate_balance(
            results['technical_count'], 
            results['emotional_count']
        )
        
        return results
    
    def _count_patterns(self, text: str, patterns: List[str]) -> int:
        """Count occurrences of patterns in text"""
        if not text:
            return 0
            
        count = 0
        for pattern in patterns:
            try:
                matches = re.findall(pattern, text, re.IGNORECASE)
                count += len(matches)
            except re.error:
                # Skip invalid regex patterns
                continue
                
        return count
    
    def get_pattern_breakdown(self, text: str) -> Dict[str, Dict[str, int]]:
        """
        Get detailed breakdown of which patterns were found
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with pattern counts for both technical and emotional
        """
        breakdown = {
            'technical': {},
            'emotional': {}
        }
        
        # Technical patterns breakdown
        for pattern in self.technical_patterns:
            try:
                count = len(re.findall(pattern, text, re.IGNORECASE))
                if count > 0:
                    breakdown['technical'][pattern] = count
            except re.error:
                continue
        
        # Emotional patterns breakdown  
        for pattern in self.emotional_patterns:
            try:
                count = len(re.findall(pattern, text, re.IGNORECASE))
                if count > 0:
                    breakdown['emotional'][pattern] = count
            except re.error:
                continue
                
        return breakdown