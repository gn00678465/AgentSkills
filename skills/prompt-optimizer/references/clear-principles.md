# C.L.E.A.R. Principles

C.L.E.A.R. is not a fill-in-the-blank structural template like C.O.A.S.T. or R.I.S.E., but rather a set of core prompting principles that can be applied universally to improve any prompt's quality.

## Principles Overview

| Concept | Definition | Principle | Application Example |
|:-------:|:----------:|:---------:|:-------------------:|
| **C - Concise** | Being clear and getting straight to the point without unnecessary fluff. | Avoid filler words and distracting details that do not provide guidance to the model. | ❌ Bad: "Can you write something about a scientific topic?" <br> ✅ Good: "Write a 200-word summary about the impact of climate change on coastal cities." |
| **L - Logical** | Organizing requests in a step-by-step or well-structured sequence. | Break down complex requests into ordered steps or bullet points to separate concerns. | ❌ Bad: "Build me a user registration feature and show some usage stats." <br> ✅ Good: "First, implement a registration form with email/password using Supabase. Then, show a dashboard with user count stats." |
| **E - Explicit** | Stating exactly what is wanted and what is not wanted. | Be precise about styles (e.g., JSON format) and specific details; do not assume the AI can read your mind. | ❌ Bad: "Tell me about dogs." <br> ✅ Good: "List 5 unique facts about Golden Retrievers in bullet point form." |
| **A - Adaptive** | Iterating and refining the prompt based on the initial output. | Treat prompting as a conversation; clarify instructions or point out errors if the first answer isn't perfect. | ❌ Bad: Starting a completely new chat when the output is slightly off. <br> ✅ Good: "The solution is missing the authentication step. Please include user authentication in the code." |
| **R - Reflective** | Reviewing what worked and what didn't after each AI interaction. | Note which phrasing gets good results and ask the AI to summarize its reasoning to build a library of effective prompts. | ❌ Bad: Closing the chat without analyzing why a prompt failed. <br> ✅ Good: "Summarize the errors we encountered and draft a prompt I can use in the future to avoid these mistakes." |

## Detailed Principle Breakdown

### C - Concise

**Definition**: Being clear and getting straight to the point without unnecessary fluff.

**Core Principle**: Avoid filler words and distracting details that do not provide guidance to the model.

**Why It Matters**: Every unnecessary word dilutes the signal-to-noise ratio. AI models perform better with dense, information-rich instructions.

**Techniques**:
- Remove qualifiers like "perhaps", "maybe", "if possible"
- Eliminate redundant phrases ("I want you to", "Can you please")
- Cut context that doesn't inform the output
- Use specific numbers instead of vague quantities ("about 200 words" → "200 words")

### L - Logical

**Definition**: Organizing requests in a step-by-step or well-structured sequence.

**Core Principle**: Break down complex requests into ordered steps or bullet points to separate concerns.

**Why It Matters**: Sequential structure helps the model follow your intended execution path and prevents mixing unrelated concerns.

**Techniques**:
- Number your steps explicitly (1, 2, 3...)
- Use clear transitions ("First... Then... Finally...")
- Separate distinct sub-tasks into bullet points
- Order dependencies correctly (inputs before processing before outputs)

### E - Explicit

**Definition**: Stating exactly what is wanted and what is not wanted.

**Core Principle**: Be precise about styles (e.g., JSON format) and specific details; do not assume the AI can read your mind.

**Why It Matters**: Ambiguity is the enemy of precision. What's obvious to you may be interpreted differently by the model.

**Techniques**:
- Specify output format explicitly (JSON, Markdown, bullet points)
- Define length constraints (word count, number of items)
- Include negative constraints ("Do NOT include...", "Avoid...")
- Name specific styles, tones, or audiences

### A - Adaptive

**Definition**: Iterating and refining the prompt based on the initial output.

**Core Principle**: Treat prompting as a conversation; clarify instructions or point out errors if the first answer isn't perfect.

**Why It Matters**: Perfect prompts rarely emerge on the first try. The conversation context allows for progressive refinement.

**Techniques**:
- Point out specific errors rather than starting over
- Add missing constraints when you see gaps
- Narrow scope if output is too broad
- Expand examples if the style is off

### R - Reflective

**Definition**: Reviewing what worked and what didn't after each AI interaction.

**Core Principle**: Note which phrasing gets good results and ask the AI to summarize its reasoning to build a library of effective prompts.

**Why It Matters**: Building a personal library of effective prompt patterns accelerates future work and prevents repeating mistakes.

**Techniques**:
- Ask the AI to explain why certain approaches worked
- Save successful prompts as templates
- Document which constraints prevented common errors
- Request prompt drafts for future similar tasks

## Using C.L.E.A.R. with Other Frameworks

C.L.E.A.R. principles enhance any structural framework. Apply them as a quality checklist:

| Framework | C.L.E.A.R. Enhancement |
|:---------:|:----------------------:|
| B.R.O.K.E | Apply **Concise** to Background; **Explicit** to Key Results |
| T.R.A.C.E | Apply **Logical** to Reasoning; **Reflective** to Evaluate |
| R.O.S.E.S | Apply **Explicit** to Expected Solution; **Logical** to Steps |
| C.A.R.E | Apply **Concise** to Context; **Explicit** to Example selection |
| R.I.S.E | Apply **Logical** to Steps; **Explicit** to Input/Expectation |

## Quick Reference Checklist

Before finalizing any prompt, verify:

- [ ] **Concise**: Have I removed all filler words and irrelevant details?
- [ ] **Logical**: Are my requests structured in a clear, sequential order?
- [ ] **Explicit**: Have I stated what I want AND what I don't want?
- [ ] **Adaptive**: Am I prepared to refine based on initial output?
- [ ] **Reflective**: Will I review and learn from this interaction?
