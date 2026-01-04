# Multi-Agent Research Ideation Tool

A collaborative multi-agent system designed to facilitate research ideation through diverse perspectives and specialized capabilities.

## Overview

This tool employs five specialized AI agents that work together to develop, refine, and validate research ideas:

1. **Challenge Circle Agent** - Critically examines ideas, identifies weaknesses, and poses challenging questions
2. **Search Agent** - Conducts online research to find relevant literature, data, and context
3. **Articulator Agent** - Refines and polishes ideas into clear, compelling narratives
4. **Legal/IRB Agent** - Reviews ethical considerations and regulatory compliance
5. **Minutes Writer Agent** - Documents the entire ideation process and decisions

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd researchideation

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Usage

```bash
# Run the research ideation session
python main.py

# Or use the interactive mode
python main.py --interactive
```

## Configuration

Edit `config.py` to customize:
- Agent behaviors and prompts
- Research session parameters
- Output formats

## Agent Roles

### Challenge Circle Agent
- Questions assumptions
- Identifies potential flaws
- Proposes alternative perspectives
- Ensures rigor

### Search Agent
- Searches academic databases
- Finds relevant research
- Identifies trends and gaps
- Provides evidence-based context

### Articulator Agent
- Clarifies complex ideas
- Improves communication
- Structures arguments
- Polishes final outputs

### Legal/IRB Agent
- Checks ethical guidelines
- Identifies compliance requirements
- Reviews human subjects considerations
- Flags legal concerns

### Minutes Writer Agent
- Documents all discussions
- Tracks decisions and rationale
- Creates structured summaries
- Maintains session history

## Architecture

```
researchideation/
├── agents/              # Agent implementations
│   ├── base.py         # Base agent class
│   ├── challenger.py   # Challenge Circle Agent
│   ├── searcher.py     # Search Agent
│   ├── articulator.py  # Articulator Agent
│   ├── legal_irb.py    # Legal/IRB Agent
│   └── minutes.py      # Minutes Writer Agent
├── orchestrator.py     # Coordinates agent interactions
├── config.py           # Configuration
├── main.py            # Entry point
└── utils.py           # Utility functions
```

## License

MIT
