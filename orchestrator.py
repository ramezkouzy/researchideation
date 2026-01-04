"""Orchestrator for coordinating multi-agent research ideation."""

from typing import List, Dict, Any, Optional
from agents import (
    ChallengerAgent,
    SearcherAgent,
    ArticulatorAgent,
    LegalIRBAgent,
    MinutesAgent
)
from utils import format_message, print_agent_message, save_session_data, save_minutes
from config import MAX_ROUNDS, SAVE_TRANSCRIPTS, SAVE_MINUTES, OUTPUT_DIR


class ResearchOrchestrator:
    """Orchestrates the multi-agent research ideation process."""

    def __init__(self):
        """Initialize the orchestrator and all agents."""
        self.challenger = ChallengerAgent()
        self.searcher = SearcherAgent()
        self.articulator = ArticulatorAgent()
        self.legal_irb = LegalIRBAgent()
        self.minutes_writer = MinutesAgent()

        self.conversation_history: List[Dict[str, Any]] = []
        self.current_round = 0

    def add_message(self, agent_name: str, content: str):
        """Add a message to the conversation history.

        Args:
            agent_name: Name of the agent sending the message
            content: Message content
        """
        message = format_message(agent_name, content)
        self.conversation_history.append(message)

    def run_ideation_session(self, initial_idea: str, max_rounds: int = MAX_ROUNDS) -> Dict[str, Any]:
        """Run a complete research ideation session.

        Args:
            initial_idea: The initial research idea to develop
            max_rounds: Maximum number of discussion rounds

        Returns:
            Session results including final idea and minutes
        """
        print("\n" + "=" * 80)
        print("RESEARCH IDEATION SESSION STARTING")
        print("=" * 80)
        print(f"\nInitial Idea: {initial_idea}\n")

        # Add initial idea to history
        self.add_message("User", f"Initial research idea: {initial_idea}")

        # Round 1: Initial exploration
        print("\n### ROUND 1: Initial Exploration ###\n")
        self.current_round = 1

        # Search agent provides context
        search_response = self.searcher.search_context(initial_idea, self.conversation_history)
        print_agent_message("Search Agent", search_response)
        self.add_message("Search Agent", search_response)

        # Challenger examines the idea
        challenge_response = self.challenger.challenge_idea(initial_idea, self.conversation_history)
        print_agent_message("Challenge Circle", challenge_response)
        self.add_message("Challenge Circle", challenge_response)

        # Legal/IRB reviews compliance
        legal_response = self.legal_irb.identify_risks(initial_idea, self.conversation_history)
        print_agent_message("Legal/IRB", legal_response)
        self.add_message("Legal/IRB", legal_response)

        # Articulator refines based on feedback
        articulation_response = self.articulator.refine_idea(
            f"Original idea: {initial_idea}\n\nConsider the feedback from other agents.",
            self.conversation_history
        )
        print_agent_message("Articulator", articulation_response)
        self.add_message("Articulator", articulation_response)

        # Additional rounds for refinement
        for round_num in range(2, max_rounds + 1):
            print(f"\n### ROUND {round_num}: Refinement and Validation ###\n")
            self.current_round = round_num

            # Challenger continues to probe
            challenge_response = self.challenger.respond(
                "Based on the discussion so far, what additional challenges or questions should be addressed?",
                self.conversation_history
            )
            print_agent_message("Challenge Circle", challenge_response)
            self.add_message("Challenge Circle", challenge_response)

            # Legal/IRB provides updated assessment
            if round_num == 2:
                legal_response = self.legal_irb.respond(
                    "Based on the refined idea, provide an updated compliance assessment.",
                    self.conversation_history
                )
                print_agent_message("Legal/IRB", legal_response)
                self.add_message("Legal/IRB", legal_response)

            # Articulator synthesizes
            synthesis_response = self.articulator.respond(
                "Synthesize the discussion so far and provide an updated, refined version of the research idea.",
                self.conversation_history
            )
            print_agent_message("Articulator", synthesis_response)
            self.add_message("Articulator", synthesis_response)

        # Final documentation
        print("\n### GENERATING FINAL MINUTES ###\n")
        final_minutes = self.minutes_writer.document_session(self.conversation_history)
        print_agent_message("Minutes Writer", final_minutes)
        self.add_message("Minutes Writer", final_minutes)

        # Prepare session results
        session_results = {
            "initial_idea": initial_idea,
            "rounds": self.current_round,
            "conversation_history": self.conversation_history,
            "final_minutes": final_minutes
        }

        # Save outputs
        if SAVE_TRANSCRIPTS:
            transcript_path = save_session_data(session_results, OUTPUT_DIR)
            print(f"\nSession transcript saved to: {transcript_path}")

        if SAVE_MINUTES:
            minutes_path = save_minutes(final_minutes, OUTPUT_DIR)
            print(f"Session minutes saved to: {minutes_path}")

        print("\n" + "=" * 80)
        print("RESEARCH IDEATION SESSION COMPLETE")
        print("=" * 80 + "\n")

        return session_results

    def run_custom_workflow(self, initial_idea: str, workflow_steps: List[str]) -> Dict[str, Any]:
        """Run a custom workflow with specified steps.

        Args:
            initial_idea: The initial research idea
            workflow_steps: List of workflow steps (agent actions)

        Returns:
            Session results
        """
        print("\n" + "=" * 80)
        print("CUSTOM RESEARCH WORKFLOW STARTING")
        print("=" * 80)
        print(f"\nInitial Idea: {initial_idea}\n")

        self.add_message("User", f"Initial research idea: {initial_idea}")

        agent_map = {
            "search": self.searcher,
            "challenge": self.challenger,
            "articulate": self.articulator,
            "legal": self.legal_irb,
            "minutes": self.minutes_writer
        }

        for step_num, step in enumerate(workflow_steps, 1):
            print(f"\n### STEP {step_num}: {step} ###\n")

            if step in agent_map:
                agent = agent_map[step]
                response = agent.respond(
                    f"Address the current research idea and previous discussion.",
                    self.conversation_history
                )
                print_agent_message(agent.name, response)
                self.add_message(agent.name, response)

        # Generate minutes
        final_minutes = self.minutes_writer.document_session(self.conversation_history)
        print_agent_message("Minutes Writer", final_minutes)

        return {
            "initial_idea": initial_idea,
            "workflow": workflow_steps,
            "conversation_history": self.conversation_history,
            "final_minutes": final_minutes
        }
