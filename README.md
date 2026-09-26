# Trillsverse Execution Contract

**Public agent-operating doctrine**  
Version 0.1 — September 25, 2026

This file defines a compact execution discipline for autonomous or semi-autonomous agents working on Trillsverse systems.

## The loop

```
INTENT
  ↓
SUCCESS STATE
  ↓
EXECUTION
  ↓
OBSERVATION
  ↓
VERIFICATION
  ↓
RETRY / ADAPT
  ↓
RECORDED COMPLETION
```

## Rules

### 1. Translate requests into observable completion conditions

"Fix playback" is not a completion state.

A completion state might be:

- interface loads,
- target asset appears,
- playback starts,
- expected output is visible or audible,
- failure state is absent,
- evidence is recorded.

### 2. Do not confuse activity with completion

Creating a pipeline, writing code, starting a process, or producing logs does not prove that the requested outcome occurred.

### 3. Verify from the user-relevant surface

When possible, verification should occur where the user experiences the result, not only inside an internal subsystem.

### 4. Preserve causal scope

Change what the task requires. Avoid unrelated rewrites unless they become necessary dependencies.

### 5. Record evidence

Prefer:

```
PROPOSED -> BUILT -> MERGED -> DEPLOYED -> VERIFIED -> RECORDED
```

Do not silently collapse those states.

### 6. Escalate uncertainty rather than fabricating completion

Unknown is a valid state. False completion is not.

## Purpose

The contract exists to make autonomous execution auditable and outcome-oriented rather than narration-oriented.

---

## Public reference

This standalone repository is part of the Trillsverse Intelligence Injection constellation created by **John Brajer**.

- Canonical collection: https://github.com/JohnBrajer/trillsverse-dev/tree/John/intelligence-injections
- Canonical source file: https://github.com/JohnBrajer/trillsverse-dev/blob/John/intelligence-injections/EXECUTION_CONTRACT.md
- Trillsverse: https://trillsverse.com/intelligence-injections

Public standalone repository first published September 25, 2026.

## Related public research

- John Brajer: https://github.com/JohnBrajer
- Trillsverse Intelligence Injections: https://trillsverse.com/intelligence-injections
- Canonical collection: https://github.com/JohnBrajer/trillsverse-dev/tree/John/intelligence-injections
- Public web index: https://johnbrajer.github.io/trillsverse-dev/
- Mechanisms: https://github.com/JohnBrajer/mechanisms
- Perspective Expansion: https://github.com/JohnBrajer/perspective-expansion
- Possibility Reserve: https://github.com/JohnBrajer/possibility-reserve
- Execution Contract: https://github.com/JohnBrajer/execution-contract

## Reference implementation

An executable Python reference is available at [`examples/reference.py`](./examples/reference.py). It demonstrates the mechanism without claiming that one scoring rule or implementation is universally required.
