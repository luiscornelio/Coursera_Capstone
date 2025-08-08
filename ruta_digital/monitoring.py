"""Monitoring and evaluation helpers."""
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class UserProgress:
    pre_scores: Dict[str, int] = field(default_factory=dict)
    post_scores: Dict[str, int] = field(default_factory=dict)

    def gain(self, module: str) -> int:
        return self.post_scores.get(module, 0) - self.pre_scores.get(module, 0)
