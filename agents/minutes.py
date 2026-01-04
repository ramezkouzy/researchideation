"""Minutes Writer Agent - documents the research ideation process."""

from .base import BaseAgent
from config import AGENT_PROMPTS
from typing import List, Dict, Any


class MinutesAgent(BaseAgent):
    """Agent that documents and summarizes the ideation session."""

    def __init__(self):
        super().__init__(
            name="Minutes Writer",
            system_prompt=AGENT_PROMPTS["minutes"]
        )

    def get_agent_type(self) -> str:
        return "minutes"

    def document_session(self, conversation_history: List[Dict[str, Any]]) -> str:
        """Document the entire ideation session.

        Args:
            conversation_history: Full conversation history

        Returns:
            Comprehensive session minutes
        """
        # Format the conversation history
        formatted_history = "\n\n".join([
            f"[{msg.get('agent', 'User')}]: {msg['content']}"
            for msg in conversation_history
        ])

        context = f"""Please create comprehensive minutes for this research ideation session:

{formatted_history}

Include:
1. Session overview and initial research idea
2. Key points raised by each agent
3. Main decisions and agreements
4. Outstanding questions or concerns
5. Action items and next steps
6. Summary of the refined research direction

Format as a professional meeting minutes document.
"""
        return self.respond(context)

    def summarize_round(self, round_number: int, round_messages: List[Dict[str, Any]]) -> str:
        """Summarize a single round of discussion.

        Args:
            round_number: The round number
            round_messages: Messages from this round

        Returns:
            Round summary
        """
        formatted_messages = "\n\n".join([
            f"[{msg.get('agent', 'User')}]: {msg['content']}"
            for msg in round_messages
        ])

        context = f"""Summarize Round {round_number} of the research ideation session:

{formatted_messages}

Provide:
1. Key points raised
2. Progress made
3. Important insights or concerns
"""
        return self.respond(context)
