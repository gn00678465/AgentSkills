# Prompt Structure Frameworks Reference

This document contains various prompt engineering frameworks for optimizing and structuring prompts. Each framework has specific strengths for different use cases.

## Framework Overview Table

| Framework | Core Components | Design Philosophy | Best Use Cases | Practical Tips | Source |
|:---------:|:---------------:|:-----------------:|:--------------:|:--------------:|:------:|
| **B.R.O.K.E** | Background, Role, Objectives, Key Results, Evolve | Complete context with professional identity, measurable metrics, supports iterative refinement | Complex tasks requiring multiple versions or long-term optimization. Request improvement suggestions to support evolution | Using specific quantitative data in "Key Results" (e.g., "increase conversion rate by 10%") makes AI output more precise | [1] |
| **T.R.A.C.E** | Task, Reasoning, Action, Check, Evaluate | Focus on logical thinking process and self-correction mechanisms | Logical reasoning, complex problem-solving. Have model reflect on improvements for next iteration | Require model to outline logic framework in "Reasoning" before "Action" to reduce logical errors | [1] |
| **C.O.A.S.T** | Context, Objective, Actions, Scenario, Task | Detailed scenario description and role relationship definition ensures model understands core interaction task | Daily task handling, communication requiring specific context. Summarize core task in one sentence at end | Adding emotional states or relationship dynamics in "Scenario" (e.g., responding to dissatisfied customer) enables more empathetic responses | [2] |
| **R.O.S.E.S** | Role, Objective, Scenario, Expected Solution, Steps | Combines role-playing with concrete action plans, emphasizes final solution type definition | Project planning, strategic planning. Add specific constraints to match real-world scenarios | Specifying format in "Expected Solution" (e.g., SWOT analysis table) directly produces usable report materials | [3] |
| **C.A.R.E** | Context, Action, Result, Example | Uses few-shot prompting concept, provides examples to align style and format | Content creation, style alignment. Provide brief examples to help model understand expected output format | Providing 2-3 example paragraphs matching target style works better than pure text descriptions | [2] |
| **R.I.S.E** | Role, Input, Steps, Expectation | Standard task-oriented structure with clear input data and execution flow | Data processing, standard operating procedures. Clearly explain provided fields and context | Presenting "Steps" as numbered list guides model to process large datasets sequentially | [2] |
| **C.L.E.A.R** | Concise, Logical, Explicit, Adaptive, Reflective | Universal principle checklist ensuring instructions are unambiguous and support iteration | General prompt checking. If results aren't perfect, use "Adaptive" principle for fine-tuning rather than abandoning | Using "what not to do" negative constraints effectively demonstrates "Explicit" principle | [4] |
| **R.A.C.E** | Role, Action, Context, Expectation | Emphasizes combination of professional identity with evaluation criteria | Professional consulting, work execution. Define standards for evaluating quality | After setting "expert role", requiring model to respond with domain-specific terminology increases authority | [3] |
| **I.C.I.O** | Instruction, Context, Input, Output | Minimal structure focusing on task start and end points | Automated workflows, API integration. Clearly describe output format (e.g., JSON) and content scope | Specifying Key-Value relationships in "Output" facilitates subsequent code parsing | [3] |
| **A.P.E** | Action, Purpose, Expectation | Clarifies intent behind execution action, reduces AI misunderstanding of goals | Quick task assignment. Explain "why we're doing this" | Explaining "Purpose" helps AI make reasonable judgments based on intent when encountering ambiguous instructions | [5] |
| **T.A.G** | Task, Audience, Goal | User-centric structure emphasizing output content's target audience | Marketing copy, educational document writing. Specify who will see the output | Specifying "Audience" as "3rd grade students" makes AI automatically simplify vocabulary for easier comprehension | [5] |
| **E.R.A** | Example, Rules, Action | Uses negative constraints and positive examples to define AI behavior boundaries | Code refactoring, strict format conversion. List constraints model must follow | Adding "no external libraries" in "Rules" ensures generated code is highly compatible | [5] |
| **Atomic** | Specific UI elements, components, modals (Atomic Vocab) | Decomposes complex interfaces into minimal units (atoms), gradually increases complexity | UI design, component development (Lovable). "Component-first rather than page-first" prompting yields clearer results | First request AI to build a "button component", confirm style, then request placing it in "navigation bar" | - |

## Framework Selection Guide

### By Task Complexity

**Simple, quick tasks:**
- **A.P.E**: Minimal structure for straightforward assignments
- **T.A.G**: User-focused for simple content creation
- **I.C.I.O**: Clean input-output for automation

**Moderate complexity:**
- **R.A.C.E**: Professional work with clear evaluation
- **C.O.A.S.T**: Scenario-based communication
- **R.I.S.E**: Standard procedures with defined steps

**Complex, multi-stage tasks:**
- **B.R.O.K.E**: Long-term projects with measurable outcomes
- **T.R.A.C.E**: Problems requiring deep reasoning
- **R.O.S.E.S**: Strategic planning with multiple phases

### By Task Type

**Content Creation & Writing:**
- **C.A.R.E**: Style alignment with examples
- **T.A.G**: Audience-specific content

**Problem Solving & Analysis:**
- **T.R.A.C.E**: Logical reasoning required
- **C.L.E.A.R**: General problem-solving checklist

**Project Planning & Strategy:**
- **B.R.O.K.E**: Measurable, evolving projects
- **R.O.S.E.S**: Strategic planning with solution types

**Data Processing & Automation:**
- **R.I.S.E**: Standard operating procedures
- **I.C.I.O**: API/workflow automation

**Code & Technical Work:**
- **E.R.A**: Strict constraints and examples
- **Atomic**: UI component development

**Professional Consulting:**
- **R.A.C.E**: Expert advice with standards
- **C.O.A.S.T**: Client interaction scenarios

### By Key Features Needed

**Need iteration/evolution:** B.R.O.K.E, T.R.A.C.E, C.L.E.A.R
**Need examples/few-shot:** C.A.R.E, E.R.A
**Need role-playing:** R.O.S.E.S, R.A.C.E, R.I.S.E
**Need measurable outcomes:** B.R.O.K.E
**Need audience focus:** T.A.G
**Need strict constraints:** E.R.A, C.L.E.A.R
**Need scenario context:** C.O.A.S.T, R.O.S.E.S

## Detailed Framework Descriptions

### B.R.O.K.E Framework
- **Background**: Provide complete context and situation
- **Role**: Define the expert persona AI should adopt
- **Objectives**: State clear goals
- **Key Results**: Define measurable success metrics
- **Evolve**: Build in iteration and improvement cycles

**When to use**: Multi-version comparisons, long-term optimization, projects with quantifiable success criteria.

### T.R.A.C.E Framework
- **Task**: Define what needs to be done
- **Reasoning**: Require logical thinking process
- **Action**: Execute the plan
- **Check**: Verify the work
- **Evaluate**: Assess and identify improvements

**When to use**: Complex problem-solving, logical reasoning tasks, situations requiring self-correction.

### C.O.A.S.T Framework
- **Context**: Set the background
- **Objective**: Define the goal
- **Actions**: List required actions
- **Scenario**: Describe the specific situation
- **Task**: Summarize the core task in one sentence

**When to use**: Daily tasks, customer interactions, communication requiring specific contextual understanding.

### R.O.S.E.S Framework
- **Role**: Expert persona
- **Objective**: What to achieve
- **Scenario**: Situation details
- **Expected Solution**: Type of solution wanted (e.g., SWOT analysis, report)
- **Steps**: Action plan

**When to use**: Project planning, strategy development, situations requiring specific output formats.

### C.A.R.E Framework
- **Context**: Background information
- **Action**: What to do
- **Result**: Expected outcome
- **Example**: Provide 2-3 examples of desired output

**When to use**: Content creation, style matching, format alignment tasks.

### R.I.S.E Framework
- **Role**: Define expert identity
- **Input**: Specify data provided
- **Steps**: List numbered procedure
- **Expectation**: Define output requirements

**When to use**: Data processing, standard operating procedures, systematic workflows.

### C.L.E.A.R Framework (Principles)
- **Concise**: Remove verbosity, keep it tight
- **Logical**: Structure with clear flow
- **Explicit**: State what you want AND don't want
- **Adaptive**: Support iteration and refinement
- **Reflective**: Include self-checking mechanisms

**When to use**: Universal framework for checking any prompt quality.

### R.A.C.E Framework
- **Role**: Professional identity
- **Action**: What to do
- **Context**: Background
- **Expectation**: Evaluation standards

**When to use**: Professional consulting, expert advice, work requiring authority and credibility.

### I.C.I.O Framework
- **Instruction**: Command
- **Context**: Background
- **Input**: Data provided
- **Output**: Desired format (e.g., JSON, specific structure)

**When to use**: Automation, API integration, clean input-output transformations.

### A.P.E Framework
- **Action**: What to do
- **Purpose**: Why doing it (the intent)
- **Expectation**: Expected result

**When to use**: Quick task assignment, situations where understanding intent improves execution.

### T.A.G Framework
- **Task**: What to accomplish
- **Audience**: Who will consume the output
- **Goal**: Desired outcome

**When to use**: Marketing copy, educational content, any audience-specific writing.

### E.R.A Framework
- **Example**: Show 1-3 examples of desired output
- **Rules**: State constraints and prohibitions
- **Action**: Define the task

**When to use**: Code refactoring, strict format conversions, bounded creative tasks.

### Atomic Framework
- **Atomic Vocabulary**: Break down into smallest UI units
- **Component-first**: Build from atoms to molecules to organisms
- **Progressive Complexity**: Start simple, add complexity gradually

**When to use**: UI design, component development, interface building.

## References
[1] Advanced prompt engineering techniques
[2] Practical prompt structuring methods
[3] Task-oriented prompting frameworks
[4] Universal prompt quality principles
[5] Intent-focused prompt patterns
