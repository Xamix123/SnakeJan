import json
import os

from settings import BASE_DIR

class LeaderboardManager:
    def __init__(self):
        self.file_path = os.path.join(BASE_DIR, "leaderboard.json")
        self.maps = ["spring", "summer", "autumn", "winter", "random"]
        self.data = self.load()

    def create_default_data(self):
        return {
            map_name: [
                {"name": "---", "score": 0},
                {"name": "---", "score": 0},
                {"name": "---", "score": 0},
                {"name": "---", "score": 0},
                {"name": "---", "score": 0},
            ]
            for map_name in self.maps
        }

    def load(self):
        if not os.path.exists(self.file_path):
            data = self.create_default_data()
            self.save(data)
            return data

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data=None):
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_scores(self, map_name):
        return self.data.get(map_name, [])

    def is_high_score(self, map_name, score):
        scores = self.get_scores(map_name)
        return any(score > record["score"] for record in scores)

    def add_score(self, map_name, player_name, score):
        self.data[map_name].append({
            "name": player_name,
            "score": score
        })

        self.data[map_name].sort(
            key=lambda record: record["score"],
            reverse=True
        )

        self.data[map_name] = self.data[map_name][:5]
        self.save()