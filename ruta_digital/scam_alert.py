"""Scam detection and reporting stubs."""
from dataclasses import dataclass, field
from typing import List

@dataclass
class Report:
    description: str
    confidence: float

@dataclass
class ScamAlertSystem:
    """Stores reports and pretends to analyze text for scams."""
    reports: List[Report] = field(default_factory=list)

    def report(self, description: str, confidence: float = 0.5) -> None:
        self.reports.append(Report(description, confidence))

    def analyze_text(self, text: str) -> float:
        """Placeholder analysis returning a fixed confidence score."""
        print(f"Analyzing: {text}")
        return 0.0
