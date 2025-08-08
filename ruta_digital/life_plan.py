"""Life plan generator module."""
from dataclasses import dataclass, field
from typing import List

@dataclass
class Goal:
    description: str
    steps: List[str] = field(default_factory=list)

@dataclass
class LifePlanGenerator:
    """Guides users through setting and tracking goals."""
    goals: List[Goal] = field(default_factory=list)

    def add_goal(self, description: str, steps: List[str]) -> None:
        self.goals.append(Goal(description, steps))

    def summary(self) -> str:
        lines = ["Life Plan Summary:"]
        for goal in self.goals:
            lines.append(f"- {goal.description}")
            for step in goal.steps:
                lines.append(f"  * {step}")
        return "\n".join(lines)
