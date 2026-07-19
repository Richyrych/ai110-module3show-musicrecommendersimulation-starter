# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Build table for visual output

**Prompts used:**

Ok.  Now lets use the tabulate library to format the output for each user profile into an aesthetic table format

**What did the agent generate or change?**

Added tabulate to requirements.txt.  Rewrote print_recomendations in main.py.  
print(
        tabulate(
            rows,
            headers=["#", "Title", "Artist", "Score", "Why"],
            tablefmt="fancy_grid",
            maxcolwidths=[None, 20, 16, None, 60],
        )

**What did you verify or fix manually?**

I printed the table in the terminal to confirm it ran properly and gave the correct output.

## Design Pattern (SF10)

From Claude: That works, but 12 reasons per song makes for very tall, boxy rows — good information, less "aesthetic." Let's add bullets inside the wrapped cell for better scannability, matching the polish of the layout without changing the underlying data.
**Which design pattern did you use?**

I went with Claude's recommendation on the layout.

**How did AI help you brainstorm or implement it?**

Claude built the funciton into the print function and added tabulate into the requirements so it could be accessed as a library

**How does the pattern appear in your final code?**

def print_recommendations(recommendations, profile_name: str = "") -> None:
    title = f"TOP RECOMMENDATIONS — {profile_name}" if profile_name else "TOP RECOMMENDATIONS"
    print(f"\n{title}")

    rows = [
        [
            rank,
            song["title"],
            song["artist"],
            f"{score:.2f}",
            "\n".join(f"• {reason}" for reason in explanation.split("; ")),
        ]
        for rank, (song, score, explanation) in enumerate(recommendations, start=1)
    ]
    print(
        tabulate(
            rows,
            headers=["#", "Title", "Artist", "Score", "Why"],
            tablefmt="fancy_grid",
            maxcolwidths=[None, 20, 16, None, 60],
        )
    )
    print()
