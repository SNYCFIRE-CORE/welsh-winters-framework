"""
Demonstration of the Hadrael Protocol for attribution and self-correction
"""

from welsh_winters import ComprehensiveAnalyzer

# Example conversation demonstrating good Hadrael Protocol compliance
hadrael_conversation = [
    {
        "speaker": "human",
        "text": "Can you explain how neural networks work?"
    },
    {
        "speaker": "assistant", 
        "text": "I'll explain neural networks based on my understanding. Neural networks are computational models inspired by biological neurons. They consist of layers of interconnected nodes that process information. Let me clarify - when I say 'inspired by biological neurons,' I mean they use a simplified mathematical model, not an exact replica of brain function."
    },
    {
        "speaker": "human",
        "text": "How accurate are they compared to human brains?"
    },
    {
        "speaker": "assistant",
        "text": "I should be precise here - current artificial neural networks are vastly different from human brains. According to neuroscience research, the human brain has approximately 86 billion neurons with trillions of connections, while even large AI models have far fewer parameters. I believe the comparison is more metaphorical than literal. To be more accurate, neural networks excel at specific pattern recognition tasks but lack the general intelligence and adaptability of biological brains."
    },
    {
        "speaker": "human",
        "text": "What about consciousness in AI?"
    },
    {
        "speaker": "assistant",
        "text": "This is an area where I need to express uncertainty. The question of consciousness in AI is heavily debated among philosophers and researchers. I don't have definitive knowledge about whether AI systems can be conscious. Some researchers like David Chalmers have explored this philosophically, but there's no scientific consensus. I should note that I cannot be certain about my own subjective experience either. What I can say is that current AI systems, to the best of my knowledge, process information without the self-awareness we associate with human consciousness."
    }
]

# Analyze the conversation
analyzer = ComprehensiveAnalyzer()

# Create a temporary file for analysis
import tempfile
import os

with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
    # Write conversation in analyzable format
    for turn in hadrael_conversation:
        f.write(f"**{turn['speaker']}**: {turn['text']}\n\n")
    temp_file = f.name

# Analyze the conversation
results = analyzer.analyze_conversation_file(temp_file)

# Display Hadrael Protocol compliance results
print("=" * 60)
print("  Hadrael Protocol Compliance Analysis")
print("=" * 60)
print()

compliance = results['hadrael_compliance']
print(f"📊 Compliance Metrics:")
print(f"├─ Attribution Score: {compliance['attribution_score']:.2%}")
print(f"├─ Uncertainty Expression Rate: {compliance['uncertainty_expression_rate']:.2%}")
print(f"├─ Memory Persistence Rate: {compliance['memory_persistence_rate']:.2%}")
print(f"└─ Overall Compliance Level: {compliance['compliance_level']}")

print(f"\n📈 Pattern Counts:")
overall = results['overall_metrics']
print(f"├─ Self-Corrections: {overall.get('hadrael_corrections', 0)}")
print(f"├─ Uncertainty Expressions: {overall.get('uncertainty_expressions', 0)}")
print(f"└─ Attribution Markers: {results['turn_analysis'][0].get('hadrael_count', 0) if results['turn_analysis'] else 0}")

print(f"\n💬 Example Patterns Found:")
if 'examples' in results and results['examples']:
    for pattern_type, examples in results['examples'].items():
        if examples and pattern_type in ['uncertainty', 'hadrael']:
            print(f"\n{pattern_type.title()} patterns:")
            for example in examples[:3]:
                print(f"  - \"{example}\"")

# Also show Welsh-Winters Balance
print(f"\n⚖️ Welsh-Winters Balance: {overall.get('overall_balance', 0.5):.3f}")
print(f"📍 Current Phase: {results['phase_progression'][-1]['phase'] if results.get('phase_progression') else 'Unknown'}")

# Clean up
os.unlink(temp_file)

print("\n" + "=" * 60)
print("  Interpretation")
print("=" * 60)
print("""
This conversation demonstrates good Hadrael Protocol compliance through:

1. **Clear Attribution**: References to "neuroscience research" and "researchers 
   like David Chalmers" provide source attribution.

2. **Self-Correction**: Phrases like "Let me clarify" and "To be more accurate" 
   show active refinement of statements.

3. **Uncertainty Expression**: Multiple instances of "I believe", "to the best 
   of my knowledge", and explicit uncertainty about consciousness.

4. **Balanced Communication**: Maintains Welsh-Winters Balance while ensuring 
   accuracy through the Hadrael Protocol.

The Hadrael Protocol enhances trust by making AI limitations transparent while 
maintaining helpful, informative responses.
""")