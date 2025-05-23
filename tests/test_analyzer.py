"""
Unit tests for Welsh-Winters Balance Analyzer
"""

import unittest
from src.analyzer import BalanceAnalyzer
from src.metrics import calculate_balance, phase_detector, CollaborationPhase


class TestBalanceAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = BalanceAnalyzer()
    
    def test_pure_technical_text(self):
        """Test analysis of purely technical text"""
        text = "Implement the API endpoint using REST architecture and JSON schema validation."
        balance = self.analyzer.analyze_text(text)
        self.assertGreater(balance, 0.9)
    
    def test_pure_emotional_text(self):
        """Test analysis of purely emotional text"""
        text = "I feel grateful and happy to be working together on this amazing journey!"
        balance = self.analyzer.analyze_text(text)
        self.assertLess(balance, 0.1)
    
    def test_balanced_text(self):
        """Test analysis of balanced text"""
        text = "I'm excited to implement this feature together. Let's configure the database and celebrate our progress!"
        balance = self.analyzer.analyze_text(text)
        self.assertGreater(balance, 0.3)
        self.assertLess(balance, 0.7)
    
    def test_empty_text(self):
        """Test handling of empty text"""
        balance = self.analyzer.analyze_text("")
        self.assertEqual(balance, 0.5)
    
    def test_conversation_analysis(self):
        """Test full conversation analysis"""
        conversation = [
            {"role": "human", "content": "Hello! I need help with coding."},
            {"role": "assistant", "content": "I'll help you implement the algorithm."},
            {"role": "human", "content": "Thank you so much!"},
        ]
        
        results = self.analyzer.analyze_conversation(conversation)
        
        self.assertEqual(results['total_messages'], 3)
        self.assertEqual(len(results['turn_balances']), 3)
        self.assertIn('overall_balance', results)
        self.assertGreater(results['technical_count'], 0)
        self.assertGreater(results['emotional_count'], 0)


class TestMetrics(unittest.TestCase):
    
    def test_balance_calculation(self):
        """Test balance score calculation"""
        # Equal counts should give 0.5
        self.assertEqual(calculate_balance(10, 10), 0.5)
        
        # All technical should give 1.0
        self.assertEqual(calculate_balance(10, 0), 1.0)
        
        # All emotional should give 0.0
        self.assertEqual(calculate_balance(0, 10), 0.0)
        
        # No patterns should give 0.5
        self.assertEqual(calculate_balance(0, 0), 0.5)
    
    def test_phase_detection(self):
        """Test collaboration phase detection"""
        # Foundation phase
        self.assertEqual(phase_detector(0.56), CollaborationPhase.FOUNDATION)
        
        # Development phase
        self.assertEqual(phase_detector(0.80), CollaborationPhase.DEVELOPMENT)
        
        # Mastery phase
        self.assertEqual(phase_detector(0.75), CollaborationPhase.MASTERY)
        
        # Unknown phase
        self.assertEqual(phase_detector(0.30), CollaborationPhase.UNKNOWN)


class TestPatternBreakdown(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = BalanceAnalyzer()
    
    def test_pattern_breakdown(self):
        """Test detailed pattern breakdown"""
        text = "I need to implement a function to process the API response."
        breakdown = self.analyzer.get_pattern_breakdown(text)
        
        self.assertIn('technical', breakdown)
        self.assertIn('emotional', breakdown)
        
        # Should find technical patterns
        self.assertGreater(len(breakdown['technical']), 0)
        
        # Check specific patterns were found
        technical_patterns_found = list(breakdown['technical'].keys())
        self.assertTrue(any('function' in p for p in technical_patterns_found))
        self.assertTrue(any('API' in p for p in technical_patterns_found))


if __name__ == '__main__':
    unittest.main()