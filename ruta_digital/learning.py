"""Interactive learning modules for La Ruta Digital app."""
from dataclasses import dataclass, field
from typing import List

@dataclass
class InteractiveLearningModule:
    """Represents a story-driven lesson with quizzes and decisions."""
    title: str
    content_blocks: List[str] = field(default_factory=list)
    quizzes: List[str] = field(default_factory=list)

    def run(self) -> None:
        """Placeholder for executing the module logic."""
        print(f"Starting module: {self.title}")
        for block in self.content_blocks:
            print(block)
        if self.quizzes:
            print("Quiz time!")
