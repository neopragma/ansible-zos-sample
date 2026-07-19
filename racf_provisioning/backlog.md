BACKLOG.md

Sprint 1

Goal

The validator is production quality.

Definition of Done

- Public API unchanged.
- Existing tests pass.
- Missing behaviors covered by tests.
- validator.py refactored for readability.
- Planner can begin on a stable foundation.

Stories

1. Expand validator test suite

- cover missing behavior
- cover regressions
- organize by validator behavior

Not assigned to sprints:

Story 2.

- validator.py split \_validate\_field() into
  - \_validate\_string(), 
  - \_validate\_integer(), 
  - \_validate\_boolean(), 
  - \_validate\_enum(),
  - \_validate\_list(),
  - \_validate\_object()

Story 3.

- validator.py introduce helper \_add\_error() 

Story 4.

- Standardize error messages

Story 5. 

- Default implementation of strict mode.

Roadmap

Planner

Goal

Translate validated model into provisioning operations.

Stories

- operation model
- planner
- planner tests

Renderer

Goal

Translate operations into RACF commands.

Executor

Goal

Execute commands against z/OS.

z/OS integration

Goal

Validate the complete provisioning workflow.
