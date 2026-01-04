"""Utility functions for the research ideation tool."""

import os
import json
from datetime import datetime
from typing import Dict, List, Any


def ensure_output_dir(output_dir: str = "output") -> str:
    """Ensure output directory exists."""
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def save_session_data(session_data: Dict[str, Any], output_dir: str = "output") -> str:
    """Save session data to a JSON file."""
    ensure_output_dir(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"session_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w') as f:
        json.dump(session_data, f, indent=2)

    return filepath


def save_minutes(minutes: str, output_dir: str = "output") -> str:
    """Save session minutes to a file."""
    ensure_output_dir(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"minutes_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w') as f:
        f.write(minutes)

    return filepath


def format_message(agent_name: str, content: str) -> Dict[str, str]:
    """Format a message from an agent."""
    return {
        "agent": agent_name,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }


def print_agent_message(agent_name: str, content: str):
    """Print an agent message with formatting."""
    separator = "=" * 80
    print(f"\n{separator}")
    print(f"[{agent_name.upper()}]")
    print(f"{separator}")
    print(content)
    print(f"{separator}\n")
