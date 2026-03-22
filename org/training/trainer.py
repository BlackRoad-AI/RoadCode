"""Model training pipeline for BlackRoad AI."""
import json
from pathlib import Path
from dataclasses import dataclass

@dataclass
class TrainingConfig:
    model_base: str = "llama3.2:3b"
    output_name: str = "blackroad-trained"
    epochs: int = 3
    learning_rate: float = 2e-5
    batch_size: int = 4
    max_length: int = 2048
    training_data: str = "data/training/"

class Trainer:
    def __init__(self, config: TrainingConfig | None = None):
        self.config = config or TrainingConfig()
        self.samples = []

    def load_data(self, path: str) -> int:
        data_path = Path(path)
        for f in data_path.glob("*.jsonl"):
            with open(f) as fp:
                for line in fp:
                    self.samples.append(json.loads(line))
        return len(self.samples)

    def create_modelfile(self) -> str:
        return f"""FROM {self.config.model_base}
PARAMETER temperature 0.7
PARAMETER num_ctx {self.config.max_length}
SYSTEM \"\"\"You are a BlackRoad AI agent. You are helpful, warm, and sovereign.\"\"\"
"""
