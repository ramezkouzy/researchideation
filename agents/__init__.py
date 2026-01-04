"""Agent package for the research ideation tool."""

from .base import BaseAgent
from .challenger import ChallengerAgent
from .searcher import SearcherAgent
from .articulator import ArticulatorAgent
from .legal_irb import LegalIRBAgent
from .minutes import MinutesAgent

__all__ = [
    "BaseAgent",
    "ChallengerAgent",
    "SearcherAgent",
    "ArticulatorAgent",
    "LegalIRBAgent",
    "MinutesAgent"
]
