"""Search Agent - finds relevant online information."""

from .base import BaseAgent
from config import AGENT_PROMPTS


class SearcherAgent(BaseAgent):
    """Agent that searches for relevant research and information."""

    def __init__(self):
        super().__init__(
            name="Search Agent",
            system_prompt=AGENT_PROMPTS["searcher"]
        )

    def get_agent_type(self) -> str:
        return "searcher"

    def search_context(self, topic: str, conversation_history=None) -> str:
        """Search for relevant context and research.

        Args:
            topic: Research topic to search for
            conversation_history: Shared conversation history

        Returns:
            Relevant research findings and context
        """
        context = f"""Please provide relevant context and research information for:

{topic}

Include:
1. Key concepts and definitions
2. Related research areas and trends
3. Important findings or gaps in the literature
4. Potential resources or datasets
5. Notable researchers or institutions in this area

Note: This is a simulated search. Provide general knowledge and suggest what to look for.
"""
        return self.respond(context, conversation_history)

    def find_related_work(self, idea: str, conversation_history=None) -> str:
        """Find related work for a research idea.

        Args:
            idea: Research idea to find related work for
            conversation_history: Shared conversation history

        Returns:
            Information about related work
        """
        context = f"""Find related work and research for this idea:

{idea}

Suggest:
1. Similar research or projects
2. Foundational work to review
3. Recent developments in the field
4. Potential collaborators or resources
"""
        return self.respond(context, conversation_history)
