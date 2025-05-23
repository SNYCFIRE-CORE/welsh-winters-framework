"""
Example of analyzing conversation trajectory over time
"""

from welsh_winters import BalanceAnalyzer
from welsh_winters.metrics import calculate_trajectory, hallucination_risk_score

# Simulate a conversation that evolves over time
# This represents a typical collaboration lifecycle
conversation_phases = {
    "Foundation Phase": [
        "Hi! I'm really excited to start learning programming with you!",
        "I feel a bit nervous but hopeful. Thank you for being patient.",
        "This is amazing! I appreciate your support so much.",
        "I'm starting to understand. You're a wonderful teacher!"
    ],
    "Development Phase": [
        "Let's implement the database schema using PostgreSQL.",
        "We need to configure the API endpoints and test the integration.",
        "The algorithm complexity is O(n²), we should optimize it.",
        "Deploy the microservice to the Kubernetes cluster with proper error handling."
    ],
    "Mastery Phase": [
        "I've refactored the codebase to improve performance by 40%.",
        "The new architecture uses event-driven microservices with Redis caching.",
        "Let's implement CI/CD pipelines with automated testing.",
        "I'm grateful for this journey - the system architecture is beautiful!"
    ]
}

analyzer = BalanceAnalyzer()
all_balances = []

print("=== Conversation Trajectory Analysis ===\n")

# Analyze each phase
for phase_name, messages in conversation_phases.items():
    print(f"\n{phase_name}:")
    phase_balances = []
    
    for i, message in enumerate(messages, 1):
        balance = analyzer.analyze_text(message)
        phase_balances.append(balance)
        all_balances.append(balance)
        print(f"  Message {i}: Balance = {balance:.3f}")
    
    avg_balance = sum(phase_balances) / len(phase_balances)
    print(f"  Phase Average: {avg_balance:.3f}")

# Calculate overall trajectory
trajectory = calculate_trajectory(all_balances)

print("\n=== Trajectory Metrics ===")
print(f"Overall Trend: {trajectory['trend']}")
print(f"Start Balance: {trajectory['start_balance']:.3f}")
print(f"End Balance: {trajectory['end_balance']:.3f}")
print(f"Average Balance: {trajectory['average_balance']:.3f}")
print(f"Volatility: {trajectory['volatility']:.3f}")
print(f"Stability Score: {trajectory['stability_score']:.3f}")
print(f"Phases Detected: {', '.join(trajectory['phases_detected'])}")

# Calculate hallucination risk
risk = hallucination_risk_score(
    trajectory['average_balance'], 
    trajectory['volatility']
)
print(f"\nHallucination Risk Score: {risk:.3f} ({'Low' if risk < 0.3 else 'Medium' if risk < 0.7 else 'High'})")

# Visualize the trajectory
print("\n=== Balance Evolution Visualization ===")
print("1.0 ┤")
print("    │")
for i, balance in enumerate(all_balances):
    bar_length = int(balance * 40)
    spaces = ' ' * i * 2
    print(f"{balance:.1f} ┤{spaces}{'█' * bar_length}")
print("0.0 ┤")
print("    └" + "─" * 50)
print("     Time →")

# Recommendations based on trajectory
print("\n=== Recommendations ===")
if trajectory['trend'] == 'technical_shift':
    print("• Trajectory shows healthy progression toward technical mastery")
    print("• Consider incorporating occasional emotional check-ins")
elif trajectory['trend'] == 'emotional_shift':
    print("• Trajectory shows increasing emotional focus")
    print("• Balance with more technical discussions when appropriate")
else:
    print("• Trajectory shows stable balance")
    print("• Maintain current interaction patterns")

if trajectory['volatility'] > 0.2:
    print("• High volatility detected - aim for more consistent patterns")
if risk > 0.5:
    print("• Elevated hallucination risk - focus on balanced interactions")