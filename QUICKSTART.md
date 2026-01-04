# Quick Start Guide

## Setup (5 minutes)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-...your-key-here...
```

## Usage

### Interactive Mode (Recommended for First Time)

```bash
python main.py --interactive
```

This will:
1. Prompt you to enter your research idea
2. Ask how many discussion rounds you want
3. Run all five agents to develop and refine your idea
4. Save minutes and transcript to the `output/` directory

### Batch Mode (For Automation)

```bash
python main.py --idea "Your research idea here" --rounds 3
```

### Examples

```bash
# Interactive with default settings
python main.py -i

# Batch mode with a specific idea
python main.py --idea "Study the impact of remote work on team collaboration" --rounds 2

# View example code
python example_usage.py
```

## Understanding the Output

After running a session, you'll find two files in the `output/` directory:

1. **session_YYYYMMDD_HHMMSS.json** - Full transcript with all agent messages
2. **minutes_YYYYMMDD_HHMMSS.md** - Professional minutes document (excluded from git)

## The Five Agents

Each agent has a specific role in developing your research idea:

| Agent | Role | Key Questions They Address |
|-------|------|---------------------------|
| **Search** | Finds context and related research | What's already known? What are the gaps? |
| **Challenge Circle** | Questions assumptions | What could go wrong? What are we missing? |
| **Articulator** | Refines and clarifies | How can we say this better? What's the core idea? |
| **Legal/IRB** | Reviews compliance | Is this ethical? What approvals are needed? |
| **Minutes** | Documents everything | What did we decide? What's next? |

## Typical Workflow

A typical session follows this pattern:

1. **Round 1: Exploration**
   - Search Agent provides context
   - Challenge Circle identifies issues
   - Legal/IRB flags compliance concerns
   - Articulator refines the idea

2. **Round 2+: Refinement**
   - Agents respond to each other
   - Idea evolves and improves
   - Concerns are addressed

3. **Final: Documentation**
   - Minutes Writer creates comprehensive summary
   - All outputs are saved

## Tips for Best Results

1. **Be Specific**: The more detailed your initial idea, the better the agents can help
2. **Use Multiple Rounds**: 3-5 rounds typically gives good results
3. **Review the Minutes**: The final minutes document is the best summary
4. **Iterate**: You can run the tool multiple times with refined ideas

## Troubleshooting

**"Error: ANTHROPIC_API_KEY not found"**
- Make sure you created a `.env` file with your API key

**"Module not found"**
- Run `pip install -r requirements.txt`

**Output directory issues**
- The `output/` directory is created automatically
- Check file permissions if you get errors

## Next Steps

- Review `example_usage.py` for advanced usage patterns
- Customize agent prompts in `config.py`
- Adjust `MAX_ROUNDS` and other settings in `config.py`
- Build custom workflows using the orchestrator

## Getting Help

- Check the main `README.md` for architecture details
- Review agent code in `agents/` directory
- Look at `orchestrator.py` to understand the workflow
