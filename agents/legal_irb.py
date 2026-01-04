"""Legal/IRB Agent - reviews ethical and legal considerations."""

from .base import BaseAgent
from config import AGENT_PROMPTS


class LegalIRBAgent(BaseAgent):
    """Agent that reviews legal and IRB compliance considerations."""

    def __init__(self):
        super().__init__(
            name="Legal/IRB",
            system_prompt=AGENT_PROMPTS["legal_irb"]
        )

    def get_agent_type(self) -> str:
        return "legal_irb"

    def review_compliance(self, research_plan: str, conversation_history=None) -> str:
        """Review research plan for legal and ethical compliance.

        Args:
            research_plan: Research plan to review
            conversation_history: Shared conversation history

        Returns:
            Compliance review and recommendations
        """
        context = f"""Please review this research plan for legal and ethical considerations:

{research_plan}

Assess:
1. Human subjects protections and IRB requirements
2. Privacy and data protection concerns
3. Informed consent requirements
4. Potential ethical issues or risks
5. Regulatory compliance requirements
6. Recommendations for addressing concerns
"""
        return self.respond(context, conversation_history)

    def identify_risks(self, idea: str, conversation_history=None) -> str:
        """Identify potential legal or ethical risks.

        Args:
            idea: Research idea to assess
            conversation_history: Shared conversation history

        Returns:
            Risk assessment
        """
        context = f"""Identify potential legal and ethical risks for this research idea:

{idea}

Consider:
1. Human subjects involvement
2. Data collection and privacy
3. Vulnerable populations
4. Conflicts of interest
5. Institutional requirements
"""
        return self.respond(context, conversation_history)
