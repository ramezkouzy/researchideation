#!/usr/bin/env python3
"""Example usage of the Multi-Agent Research Ideation Tool."""

from orchestrator import ResearchOrchestrator


def example_basic_session():
    """Example: Run a basic ideation session."""
    print("=" * 80)
    print("EXAMPLE 1: Basic Research Ideation Session")
    print("=" * 80 + "\n")

    idea = """
    Develop a mobile application that uses machine learning to help students
    with learning disabilities improve their reading comprehension through
    personalized, adaptive exercises.
    """

    orchestrator = ResearchOrchestrator()
    results = orchestrator.run_ideation_session(idea, max_rounds=3)

    print(f"\nSession completed with {len(results['conversation_history'])} messages")


def example_custom_workflow():
    """Example: Run a custom workflow."""
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Custom Workflow")
    print("=" * 80 + "\n")

    idea = """
    Investigate the effectiveness of peer mentoring programs in reducing
    burnout among healthcare workers in rural hospitals.
    """

    # Define a custom workflow: search, challenge, legal review, articulate
    workflow = ["search", "challenge", "legal", "articulate", "minutes"]

    orchestrator = ResearchOrchestrator()
    results = orchestrator.run_custom_workflow(idea, workflow)

    print(f"\nCustom workflow completed with {len(results['conversation_history'])} messages")


def example_focused_analysis():
    """Example: Focus on specific aspects using individual agents."""
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Focused Analysis with Individual Agents")
    print("=" * 80 + "\n")

    from agents import ChallengerAgent, LegalIRBAgent, ArticulatorAgent

    idea = """
    Create a longitudinal study tracking the cognitive development of children
    who participate in bilingual education programs from kindergarten through
    5th grade.
    """

    # Use individual agents for focused analysis
    print("Step 1: Challenge the idea")
    challenger = ChallengerAgent()
    challenge = challenger.challenge_idea(idea)
    print(f"Challenge: {challenge[:200]}...\n")

    print("Step 2: Review legal/ethical considerations")
    legal = LegalIRBAgent()
    compliance = legal.review_compliance(idea)
    print(f"Legal/IRB: {compliance[:200]}...\n")

    print("Step 3: Refine the idea")
    articulator = ArticulatorAgent()
    refined = articulator.refine_idea(f"{idea}\n\nChallenges: {challenge}\n\nCompliance: {compliance}")
    print(f"Refined: {refined[:200]}...\n")


if __name__ == "__main__":
    # Run examples
    # Uncomment the examples you want to run

    # example_basic_session()
    # example_custom_workflow()
    # example_focused_analysis()

    print("\nTo run these examples, uncomment them in the example_usage.py file")
    print("Make sure you have set your ANTHROPIC_API_KEY in .env first!\n")
