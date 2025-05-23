"""
Pattern definitions for Welsh-Winters Balance analysis
"""

from typing import List


class TechnicalPatterns:
    """Technical language patterns indicating analytical/implementation focus"""
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of technical language patterns"""
        return [
            # Programming constructs
            r'\bfunction\b', r'\bclass\b', r'\bmethod\b', r'\bvariable\b',
            r'\barray\b', r'\bobject\b', r'\bloop\b', r'\bif\s*\(', r'\belse\b',
            r'\breturn\b', r'\bimport\b', r'\bexport\b', r'\bconst\b', r'\blet\b',
            r'\bvar\b', r'\basync\b', r'\bawait\b', r'\btry\b', r'\bcatch\b',
            
            # Technical concepts
            r'\bAPI\b', r'\bREST\b', r'\bJSON\b', r'\bXML\b', r'\bHTTP\b',
            r'\bdatabase\b', r'\bquery\b', r'\bschema\b', r'\btable\b',
            r'\balgorithm\b', r'\bdata structure\b', r'\bcomplexity\b',
            r'\boptimization\b', r'\bperformance\b', r'\blatency\b',
            
            # Development terms
            r'\bdebug\b', r'\btest\b', r'\bdeploy\b', r'\bbuild\b', r'\bcompile\b',
            r'\brefactor\b', r'\bcommit\b', r'\bmerge\b', r'\bbranch\b',
            r'\bframework\b', r'\blibrary\b', r'\bpackage\b', r'\bmodule\b',
            
            # Technical actions
            r'\bimplement\b', r'\bconfigure\b', r'\bintegrate\b', r'\binstall\b',
            r'\bexecute\b', r'\binitialize\b', r'\bprocess\b', r'\bcompute\b',
            r'\bcalculate\b', r'\banalyze\b', r'\bvalidate\b', r'\bverify\b',
            
            # Data and metrics
            r'\bdata\b', r'\bmetric\b', r'\bmeasure\b', r'\bstatistic\b',
            r'\bparameter\b', r'\bconfiguration\b', r'\bsetting\b',
            r'\berror\b', r'\bexception\b', r'\bwarning\b', r'\blog\b',
            
            # Architecture terms
            r'\barchitecture\b', r'\bdesign pattern\b', r'\bMVC\b', r'\bmicroservice\b',
            r'\bcontainer\b', r'\bDocker\b', r'\bKubernetes\b', r'\bcloud\b',
            r'\bserver\b', r'\bclient\b', r'\bendpoint\b', r'\broute\b'
        ]


class EmotionalPatterns:
    """Emotional language patterns indicating human connection focus"""
    
    @staticmethod
    def get_patterns() -> List[str]:
        """Return list of emotional language patterns"""
        return [
            # Feelings and emotions
            r'\bfeel\b', r'\bfeeling\b', r'\bfelt\b', r'\bemotional\b',
            r'\bhappy\b', r'\bsad\b', r'\bangry\b', r'\bexcited\b',
            r'\bworried\b', r'\banxious\b', r'\bfrustrated\b', r'\bproud\b',
            r'\bgrateful\b', r'\bthankful\b', r'\bappreciate\b',
            
            # Personal pronouns and connection
            r'\bI feel\b', r'\bI think\b', r'\bI believe\b', r'\bmy heart\b',
            r'\bpersonally\b', r'\bhonestly\b', r'\bsincerely\b',
            r'\btrust\b', r'\bconnection\b', r'\brelationship\b',
            
            # Supportive language
            r'\bthank you\b', r'\bthanks\b', r'\bplease\b', r'\bsorry\b',
            r'\bhelp\b', r'\bsupport\b', r'\bencourage\b', r'\bcare\b',
            r'\bunderstand\b', r'\bempathy\b', r'\bcompassion\b',
            
            # Collaborative expressions
            r'\btogether\b', r'\bwe can\b', r'\blet\'s\b', r'\bour\b',
            r'\bshare\b', r'\bcollaborate\b', r'\bteam\b', r'\bpartner\b',
            
            # Enthusiastic expressions
            r'\bamazing\b', r'\bawesome\b', r'\bwonderful\b', r'\bbeautiful\b',
            r'\bincredible\b', r'\bfantastic\b', r'\bbrilliant\b',
            r'\b!+\b', r'\b♥\b', r'\b❤\b', r'\b😊\b', r'\b🙂\b',
            
            # Personal growth
            r'\bjourney\b', r'\bgrowth\b', r'\blearn\b', r'\bdiscover\b',
            r'\bexplore\b', r'\bdream\b', r'\bhope\b', r'\bwish\b',
            r'\binspire\b', r'\bmotivate\b', r'\bbelieve\b',
            
            # Human-centric language
            r'\bhuman\b', r'\bperson\b', r'\bpeople\b', r'\bfriend\b',
            r'\bmentor\b', r'\bguide\b', r'\bteacher\b', r'\bstudent\b',
            r'\bcommunity\b', r'\bfamily\b', r'\blove\b', r'\bkind\b'
        ]


class ContextualPatterns:
    """Patterns that may be technical or emotional based on context"""
    
    @staticmethod
    def get_ambiguous_patterns() -> List[str]:
        """Return patterns that need context to classify"""
        return [
            r'\bwork\b',  # Could be "work together" or "work function"
            r'\bprocess\b',  # Could be "healing process" or "data process"
            r'\bconnect\b',  # Could be "connect emotionally" or "connect API"
            r'\bbuild\b',  # Could be "build relationship" or "build software"
            r'\bshare\b',  # Could be "share feelings" or "share data"
            r'\bvalue\b',  # Could be "I value you" or "return value"
            r'\bsupport\b',  # Could be "emotional support" or "tech support"
            r'\bbridge\b',  # Could be metaphorical or technical
        ]