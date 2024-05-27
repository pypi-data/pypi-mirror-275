# Introduction

DESimPy is an event-driven discrete event simulation engine.

![](assets/logo.jpg)

DESimPy was largely motivated by the desire to get more practice with discrete event simulation. It was also motivated by wishing to have a discrete event simulation engine that did not depend on using exception handling for non-exceptional behaviour of a program.

# Installation

```bash
pip install desimpy
```

# Quick Start

```python
from desimpy import core

class CustomEvent(core.Event):
    """Custom event for demonstration."""

    def execute(self, env) -> None:
        """Execution logic of the custom event."""
        print(f"Custom event executed at time {env.now}")

if __name__ == "__main__":
    env = core.Environment()  # Initialize the simulation environment
    event = CustomEvent(5)  # Schedule the custom event at time 5
    env.schedule_event(event)
    env.run(10)  # Run the simulation for 10 time units
```
