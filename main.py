#!/usr/bin/env python3
"""Main entry point for the Multi-Agent Research Ideation Tool."""

import sys
import argparse
from orchestrator import ResearchOrchestrator
from config import MAX_ROUNDS


def interactive_mode():
    """Run the tool in interactive mode."""
    print("\n" + "=" * 80)
    print("MULTI-AGENT RESEARCH IDEATION TOOL")
    print("=" * 80)
    print("\nWelcome! This tool uses five specialized AI agents to help develop")
    print("and refine your research ideas:")
    print("  1. Challenge Circle - Critically examines ideas")
    print("  2. Search Agent - Finds relevant research and context")
    print("  3. Articulator - Refines and polishes ideas")
    print("  4. Legal/IRB - Reviews ethical and compliance considerations")
    print("  5. Minutes Writer - Documents the entire process")
    print("\n" + "=" * 80 + "\n")

    # Get research idea from user
    print("Please enter your initial research idea:")
    print("(You can enter multiple lines. Press Ctrl+D or Ctrl+Z when done)\n")

    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    initial_idea = "\n".join(lines).strip()

    if not initial_idea:
        print("\nError: No research idea provided.")
        sys.exit(1)

    # Get number of rounds
    print(f"\nHow many discussion rounds? (default: {MAX_ROUNDS}): ", end="")
    try:
        rounds_input = input().strip()
        rounds = int(rounds_input) if rounds_input else MAX_ROUNDS
    except ValueError:
        rounds = MAX_ROUNDS

    # Run the ideation session
    orchestrator = ResearchOrchestrator()
    results = orchestrator.run_ideation_session(initial_idea, max_rounds=rounds)

    print("\n" + "=" * 80)
    print("SESSION SUMMARY")
    print("=" * 80)
    print(f"\nTotal messages: {len(results['conversation_history'])}")
    print(f"Discussion rounds: {results['rounds']}")
    print("\nThank you for using the Multi-Agent Research Ideation Tool!")
    print("=" * 80 + "\n")


def batch_mode(idea: str, rounds: int):
    """Run the tool in batch mode with provided idea.

    Args:
        idea: Research idea to process
        rounds: Number of discussion rounds
    """
    orchestrator = ResearchOrchestrator()
    results = orchestrator.run_ideation_session(idea, max_rounds=rounds)
    return results


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Multi-Agent Research Ideation Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --interactive
  python main.py --idea "Study the impact of AI on education" --rounds 3
  python main.py -i
        """
    )

    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )

    parser.add_argument(
        "--idea",
        type=str,
        help="Research idea to process (batch mode)"
    )

    parser.add_argument(
        "--rounds",
        type=int,
        default=MAX_ROUNDS,
        help=f"Number of discussion rounds (default: {MAX_ROUNDS})"
    )

    args = parser.parse_args()

    # Check for API key
    from config import ANTHROPIC_API_KEY
    if not ANTHROPIC_API_KEY:
        print("Error: ANTHROPIC_API_KEY not found in environment.")
        print("Please set it in your .env file or environment variables.")
        sys.exit(1)

    # Determine mode
    if args.interactive:
        interactive_mode()
    elif args.idea:
        batch_mode(args.idea, args.rounds)
    else:
        # Default to interactive if no arguments provided
        interactive_mode()


if __name__ == "__main__":
    main()
