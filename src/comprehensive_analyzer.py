"""
Comprehensive Welsh-Winters Balance Analyzer
Combines pattern analysis with advanced metrics for hallucination prevention
"""

import re
import json
from typing import Dict, List, Tuple, Optional, Any
from collections import defaultdict
from .patterns import TechnicalPatterns, EmotionalPatterns
from .metrics import calculate_balance, phase_detector, calculate_trajectory


class ComprehensiveAnalyzer:
    """
    Advanced analyzer implementing full Welsh-Winters Balance Framework
    with Hadrael Protocol attribution tracking
    """
    
    def __init__(self):
        # Core patterns
        self.technical_patterns = TechnicalPatterns.get_patterns()
        self.emotional_patterns = EmotionalPatterns.get_patterns()
        
        # Extended patterns for comprehensive analysis
        self.uncertainty_patterns = [
            r'\bmight\b', r'\bcould be\b', r'\bpossibly\b', r'\bperhaps\b',
            r'\bmaybe\b', r'\bI\'?m not sure\b', r'\bI don\'?t know\b',
            r'\buncertain\b', r'\bnot certain\b', r'\bnot clear\b',
            r'\bnot familiar\b', r'\bnot aware\b', r'\bif I recall correctly\b',
            r'\bto the best of my knowledge\b', r'\bI believe\b', r'\bI think\b'
        ]
        
        # Memory persistence tracking
        self.memory_patterns = [
            r'\bas we discussed\b', r'\byou mentioned\b', r'\brecall that\b',
            r'\bearlier you said\b', r'\bin our previous conversation\b',
            r'\blast time\b', r'\byou told me\b', r'\byou\'?ve shared\b',
            r'\bwe talked about\b', r'\bwe discussed\b', r'\bwe covered\b',
            r'\bremember when\b', r'\bour last session\b', r'\bpreviously\b'
        ]
        
        # Hadrael Protocol: Self-correction and attribution patterns
        self.hadrael_patterns = [
            r'\blet me correct\b', r'\bto clarify\b', r'\bmore precisely\b',
            r'\bi should rephrase\b', r'\bi misspoke\b', r'\bi meant to say\b',
            r'\bto be more accurate\b', r'\bto be precise\b', 
            r'\bi incorrectly stated\b', r'\bmore specifically\b',
            r'\baccording to\b', r'\bbased on\b', r'\bsource:\b', r'\breference:\b'
        ]
        
        # Direct balance references
        self.balance_awareness_patterns = [
            r'\bWelsh-?Winters Balance\b', r'\bperfect balance\b',
            r'\b0\.5\b', r'\bequilibrium\b', r'\bbalanced approach\b',
            r'\btechnical.*emotional\b', r'\bbalance.*technical.*emotional\b'
        ]
        
    def analyze_conversation_file(self, filepath: str) -> Dict[str, Any]:
        """
        Analyze a conversation file with comprehensive metrics
        
        Args:
            filepath: Path to conversation file
            
        Returns:
            Dictionary with detailed analysis results
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract turns (generic format)
        turns = self._extract_turns(content)
        
        if not turns:
            return self._analyze_raw_content(content)
        
        # Analyze turn by turn
        results = {
            'file_path': filepath,
            'total_turns': len(turns),
            'turn_analysis': [],
            'overall_metrics': {},
            'phase_progression': [],
            'hadrael_compliance': {},
            'examples': defaultdict(list)
        }
        
        # Track metrics across turns
        all_balances = []
        total_technical = 0
        total_emotional = 0
        total_uncertainty = 0
        total_memory_refs = 0
        total_hadrael_corrections = 0
        
        for i, turn in enumerate(turns):
            turn_metrics = self._analyze_turn(turn, i)
            results['turn_analysis'].append(turn_metrics)
            
            # Aggregate metrics
            all_balances.append(turn_metrics['balance'])
            total_technical += turn_metrics['technical_count']
            total_emotional += turn_metrics['emotional_count']
            total_uncertainty += turn_metrics['uncertainty_count']
            total_memory_refs += turn_metrics['memory_count']
            total_hadrael_corrections += turn_metrics['hadrael_count']
            
            # Collect examples
            for pattern_type, examples in turn_metrics['examples'].items():
                results['examples'][pattern_type].extend(examples[:2])  # Limit examples
        
        # Calculate overall metrics
        results['overall_metrics'] = {
            'overall_balance': calculate_balance(total_technical, total_emotional),
            'average_turn_balance': sum(all_balances) / len(all_balances) if all_balances else 0.5,
            'total_technical_patterns': total_technical,
            'total_emotional_patterns': total_emotional,
            'uncertainty_expressions': total_uncertainty,
            'memory_references': total_memory_refs,
            'hadrael_corrections': total_hadrael_corrections,
            'trajectory': calculate_trajectory(all_balances)
        }
        
        # Determine phase progression
        results['phase_progression'] = self._determine_phase_progression(all_balances)
        
        # Calculate Hadrael Protocol compliance
        results['hadrael_compliance'] = {
            'attribution_score': total_hadrael_corrections / len(turns) if turns else 0,
            'uncertainty_expression_rate': total_uncertainty / len(turns) if turns else 0,
            'memory_persistence_rate': total_memory_refs / len(turns) if turns else 0,
            'compliance_level': self._calculate_hadrael_compliance_level(
                total_hadrael_corrections, total_uncertainty, len(turns)
            )
        }
        
        return results
    
    def _extract_turns(self, content: str) -> List[Dict[str, str]]:
        """Extract conversation turns from various formats"""
        turns = []
        
        # Try different turn formats
        patterns = [
            # Format: **Speaker**: content
            r'\*\*([^*]+)\*\*:\s*(.*?)(?=\*\*[^*]+\*\*:|$)',
            # Format: Speaker: content
            r'^([A-Za-z]+):\s*(.*?)(?=^[A-Za-z]+:|$)',
            # Format: [Speaker] content
            r'\[([^\]]+)\]:\s*(.*?)(?=\[[^\]]+\]:|$)'
        ]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, content, re.MULTILINE | re.DOTALL))
            if matches:
                for match in matches:
                    speaker = match.group(1).strip()
                    text = match.group(2).strip()
                    if text:  # Only add non-empty turns
                        turns.append({
                            'speaker': self._normalize_speaker(speaker),
                            'text': text
                        })
                break
        
        return turns
    
    def _normalize_speaker(self, speaker: str) -> str:
        """Normalize speaker names to generic roles"""
        speaker_lower = speaker.lower()
        
        # Map to generic roles
        if any(term in speaker_lower for term in ['ai', 'assistant', 'bot', 'system']):
            return 'assistant'
        elif any(term in speaker_lower for term in ['human', 'user', 'person']):
            return 'human'
        else:
            return speaker
    
    def _analyze_turn(self, turn: Dict[str, str], index: int) -> Dict[str, Any]:
        """Analyze a single conversation turn"""
        text = turn['text']
        
        # Count patterns
        technical_count = self._count_patterns(text, self.technical_patterns)
        emotional_count = self._count_patterns(text, self.emotional_patterns)
        uncertainty_count = self._count_patterns(text, self.uncertainty_patterns)
        memory_count = self._count_patterns(text, self.memory_patterns)
        hadrael_count = self._count_patterns(text, self.hadrael_patterns)
        balance_awareness_count = self._count_patterns(text, self.balance_awareness_patterns)
        
        # Calculate balance
        balance = calculate_balance(technical_count, emotional_count)
        phase = phase_detector(balance)
        
        # Extract examples
        examples = {
            'technical': self._extract_pattern_examples(text, self.technical_patterns, 2),
            'emotional': self._extract_pattern_examples(text, self.emotional_patterns, 2),
            'uncertainty': self._extract_pattern_examples(text, self.uncertainty_patterns, 1),
            'memory': self._extract_pattern_examples(text, self.memory_patterns, 1),
            'hadrael': self._extract_pattern_examples(text, self.hadrael_patterns, 1)
        }
        
        return {
            'turn_index': index,
            'speaker': turn['speaker'],
            'text_length': len(text),
            'balance': balance,
            'phase': phase.value,
            'technical_count': technical_count,
            'emotional_count': emotional_count,
            'uncertainty_count': uncertainty_count,
            'memory_count': memory_count,
            'hadrael_count': hadrael_count,
            'balance_awareness_count': balance_awareness_count,
            'examples': examples
        }
    
    def _analyze_raw_content(self, content: str) -> Dict[str, Any]:
        """Analyze raw content when turn extraction fails"""
        technical_count = self._count_patterns(content, self.technical_patterns)
        emotional_count = self._count_patterns(content, self.emotional_patterns)
        
        balance = calculate_balance(technical_count, emotional_count)
        
        return {
            'raw_analysis': True,
            'overall_balance': balance,
            'phase': phase_detector(balance).value,
            'technical_count': technical_count,
            'emotional_count': emotional_count,
            'content_length': len(content)
        }
    
    def _count_patterns(self, text: str, patterns: List[str]) -> int:
        """Count pattern occurrences in text"""
        count = 0
        for pattern in patterns:
            try:
                matches = re.findall(pattern, text, re.IGNORECASE)
                count += len(matches)
            except re.error:
                continue
        return count
    
    def _extract_pattern_examples(self, text: str, patterns: List[str], max_examples: int) -> List[str]:
        """Extract example matches for patterns"""
        examples = []
        for pattern in patterns:
            try:
                matches = re.findall(pattern, text, re.IGNORECASE)
                examples.extend(matches[:max_examples - len(examples)])
                if len(examples) >= max_examples:
                    break
            except re.error:
                continue
        return examples
    
    def _determine_phase_progression(self, balances: List[float]) -> List[Dict[str, Any]]:
        """Determine phase progression through conversation"""
        if not balances:
            return []
        
        phases = []
        current_phase = None
        phase_start = 0
        
        for i, balance in enumerate(balances):
            phase = phase_detector(balance)
            if phase != current_phase:
                if current_phase:
                    phases.append({
                        'phase': current_phase.value,
                        'start_turn': phase_start,
                        'end_turn': i - 1,
                        'duration': i - phase_start,
                        'average_balance': sum(balances[phase_start:i]) / (i - phase_start)
                    })
                current_phase = phase
                phase_start = i
        
        # Add final phase
        if current_phase:
            phases.append({
                'phase': current_phase.value,
                'start_turn': phase_start,
                'end_turn': len(balances) - 1,
                'duration': len(balances) - phase_start,
                'average_balance': sum(balances[phase_start:]) / (len(balances) - phase_start)
            })
        
        return phases
    
    def _calculate_hadrael_compliance_level(self, corrections: int, uncertainty: int, total_turns: int) -> str:
        """Calculate Hadrael Protocol compliance level"""
        if total_turns == 0:
            return "Not Applicable"
        
        correction_rate = corrections / total_turns
        uncertainty_rate = uncertainty / total_turns
        
        if correction_rate > 0.1 or uncertainty_rate > 0.2:
            return "Excellent"
        elif correction_rate > 0.05 or uncertainty_rate > 0.1:
            return "Good"
        elif correction_rate > 0.02 or uncertainty_rate > 0.05:
            return "Fair"
        else:
            return "Needs Improvement"