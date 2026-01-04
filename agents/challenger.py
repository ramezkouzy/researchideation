"""Challenge Circle Agent - critically examines ideas."""

from .base import BaseAgent
from config import AGENT_PROMPTS


class ChallengerAgent(BaseAgent):
    """Agent that challenges ideas and identifies weaknesses."""

    def __init__(self):
        super().__init__(
            name="Challenge Circle",
            system_prompt=AGENT_PROMPTS["challenger"]
        )

    def get_agent_type(self) -> str:
        return "challenger"

    def challenge_idea(self, idea: str, conversation_history=None) -> str:
        """Challenge a research idea.

        Args:
            idea: The research idea to challenge
            conversation_history: Shared conversation history

        Returns:
            Critical analysis and challenging questions
        """
        context = f"""Please critically examine the following research idea:

{idea}

Provide:
1. Potential weaknesses or blind spots
2. Challenging questions that need to be addressed
3. Alternative perspectives to consider
4. Assumptions that should be validated
"""
        return self.respond(context, conversation_history)
