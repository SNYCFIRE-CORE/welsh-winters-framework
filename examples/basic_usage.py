"""
Basic usage example for Welsh-Winters Balance Framework
"""

from welsh_winters import BalanceAnalyzer, phase_detector

# Example 1: Analyze a single text
analyzer = BalanceAnalyzer()

technical_text = """
Let's implement a REST API using FastAPI. We'll need to configure the database 
connection, set up the schema, and deploy the microservice to our Kubernetes cluster.
The algorithm complexity should be O(n log n) for optimal performance.
"""

emotional_text = """
I really appreciate your help with this! I was feeling frustrated earlier, but 
working together makes me feel so much better. Thank you for being patient and 
understanding. This journey of learning has been amazing!
"""

balanced_text = """
I'm excited to share the new feature we built together! The API integration works 
beautifully, and I'm grateful for your support during the debugging process. Let's 
deploy it tomorrow and celebrate our teamwork.
"""

# Analyze each text
tech_balance = analyzer.analyze_text(technical_text)
emot_balance = analyzer.analyze_text(emotional_text)
balanced_balance = analyzer.analyze_text(balanced_text)

print("Welsh-Winters Balance Scores:")
print(f"Technical text: {tech_balance:.3f}")
print(f"Emotional text: {emot_balance:.3f}")
print(f"Balanced text: {balanced_balance:.3f}")
print()

# Example 2: Analyze a conversation
conversation = [
    {"role": "human", "content": "Hi! I'm excited to start this project with you!"},
    {"role": "assistant", "content": "Hello! I'm happy to help. What would you like to build?"},
    {"role": "human", "content": "I want to create a web API for data processing."},
    {"role": "assistant", "content": "Great! We'll need to set up endpoints, configure the database schema, and implement error handling."},
    {"role": "human", "content": "That sounds complex, but I trust we can figure it out together."},
    {"role": "assistant", "content": "Absolutely! Let's start by defining the API structure and then implement each endpoint step by step."}
]

# Analyze the conversation
results = analyzer.analyze_conversation(conversation)

print("Conversation Analysis:")
print(f"Total messages: {results['total_messages']}")
print(f"Overall balance: {results['overall_balance']:.3f}")
print(f"Phase: {phase_detector(results['overall_balance']).value}")
print()

# Show turn-by-turn analysis
print("Turn-by-turn balance:")
for turn in results['turn_balances']:
    print(f"  Turn {turn['turn']} ({turn['role']}): {turn['balance']:.3f}")

# Example 3: Get detailed pattern breakdown
sample_text = "I need to implement an async function to process the API response and handle errors gracefully."
breakdown = analyzer.get_pattern_breakdown(sample_text)

print("\nPattern Breakdown:")
print(f"Technical patterns found: {len(breakdown['technical'])}")
print(f"Emotional patterns found: {len(breakdown['emotional'])}")

if breakdown['technical']:
    print("\nTop technical patterns:")
    for pattern, count in list(breakdown['technical'].items())[:5]:
        print(f"  '{pattern}': {count} occurrences")