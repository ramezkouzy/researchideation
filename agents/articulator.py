"""Articulator Agent - refines and polishes ideas."""

from .base import BaseAgent
from config import AGENT_PROMPTS


class ArticulatorAgent(BaseAgent):
    """Agent that articulates and refines research ideas."""

    def __init__(self):
        super().__init__(
            name="Articulator",
            system_prompt=AGENT_PROMPTS["articulator"]
        )

    def get_agent_type(self) -> str:
        return "articulator"

    def refine_idea(self, rough_idea: str, conversation_history=None) -> str:
        """Refine and articulate a research idea.

        Args:
            rough_idea: Initial or rough research idea
            conversation_history: Shared conversation history

        Returns:
            Refined and articulated version of the idea
        """
        context = f"""Please refine and articulate this research idea:

{rough_idea}

Provide:
1. A clear, compelling statement of the research idea
2. Key objectives and expected outcomes
3. Logical structure and flow of the argument
4. Improved clarity and accessibility
5. Suggestions for further refinement
"""
        return self.respond(context, conversation_history)

    def synthesize_discussion(self, discussion: str, conversation_history=None) -> str:
        """Synthesize a discussion into clear points.

        Args:
            discussion: Discussion to synthesize
            conversation_history: Shared conversation history

        Returns:
            Synthesized and clarified version
        """
        context = f"""Please synthesize and clarify the following discussion:

{discussion}

Provide:
1. Main themes and points
2. Areas of agreement and disagreement
3. Clear articulation of key insights
4. Structured summary
"""
        return self.respond(context, conversation_history)
