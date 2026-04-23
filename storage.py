import json
from pathlib import Path


class JsonStorage:
    def __init__(self, filename):
        self.filename = Path(filename)

    def save(self, high_score):
        with open(self.filename, "w") as f:
            json.dump(high_score, f)

    def load(self):
        if not self.filename.exists():
            return 0
        with open(self.filename, "r") as f:
            return json.load(f)
