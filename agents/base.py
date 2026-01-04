"""Base agent class for all research ideation agents."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any
import anthropic
from config import ANTHROPIC_API_KEY, MODEL, MAX_TOKENS, TEMPERATURE


class BaseAgent(ABC):
    """Base class for all agents in the research ideation system."""

    def __init__(self, name: str, system_prompt: str):
        """Initialize the agent.

        Args:
            name: Agent name/identifier
            system_prompt: System prompt defining the agent's role
        """
        self.name = name
        self.system_prompt = system_prompt
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        self.conversation_history: List[Dict[str, str]] = []

    def add_to_history(self, role: str, content: str):
        """Add a message to the conversation history.

        Args:
            role: Message role (user or assistant)
            content: Message content
        """
        self.conversation_history.append({
            "role": role,
            "content": content
        })

    def respond(self, context: str, conversation_history: List[Dict[str, Any]] = None) -> str:
        """Generate a response based on the context.

        Args:
            context: Current context or prompt for the agent
            conversation_history: Optional shared conversation history

        Returns:
            Agent's response as a string
        """
        # Build messages for the API call
        messages = []

        # Include shared conversation history if provided
        if conversation_history:
            for msg in conversation_history:
                if msg.get("agent") != self.name:  # Don't include own messages
                    messages.append({
                        "role": "user",
                        "content": f"[{msg['agent']}]: {msg['content']}"
                    })

        # Add current context
        messages.append({
            "role": "user",
            "content": context
        })

        # Make API call
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            system=self.system_prompt,
            messages=messages
        )

        response_text = response.content[0].text

        # Update internal history
        self.add_to_history("user", context)
        self.add_to_history("assistant", response_text)

        return response_text

    def reset_history(self):
        """Clear the conversation history."""
        self.conversation_history = []

    @abstractmethod
    def get_agent_type(self) -> str:
        """Return the agent type identifier."""
        pass
