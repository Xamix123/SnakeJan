import json
import os

from configs.paths import BASE_DIR


class LeaderboardManager:
    """
    Manages leaderboard data for all game maps.

    The manager is responsible for:
    - creating default leaderboard data;
    - loading scores from a JSON file;
    - saving scores to disk;
    - checking whether a score is a high score;
    - adding new records to the leaderboard.
    """

    def __init__(self):
        """
        Initialize the leaderboard manager.
        """
        # Path to the leaderboard data file.
        self.file_path = os.path.join(BASE_DIR, "leaderboard.json")
        # List of all supported maps.
        self.maps = ["spring", "summer", "autumn", "winter", "random"]
        # Load leaderboard data from disk.
        self.data = self.load()

    def create_default_data(self):
        """
        Create default leaderboard data.

        Each map contains five placeholder records.

        Returns:
            dict: Default leaderboard structure.
        """
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
        """
        Load leaderboard data from the JSON file.

        If the file does not exist, create it with default data.

        Returns:
            dict: Loaded leaderboard data.
        """
        if not os.path.exists(self.file_path):
            data = self.create_default_data()
            self.save(data)
            return data

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data=None):
        """
        Save leaderboard data to the JSON file.

        Args:
            data (dict | None):
                Data to save. If None, self.data is used.
        """
        if data is None:
            data = self.data

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_scores(self, map_name):
        """
        Return scores for the specified map.

        Args:
            map_name (str): Map identifier.

        Returns:
            list[dict]: List of score records.
        """
        return self.data.get(map_name, [])

    def is_high_score(self, map_name, score):
        """
        Check whether the score qualifies for the leaderboard.

        Args:
            map_name (str): Map identifier.
            score (int): Player score.

        Returns:
            bool: True if the score is higher than at least one record.
        """
        scores = self.get_scores(map_name)
        return any(score > record["score"] for record in scores)

    def add_score(self, map_name, player_name, score):
        """
        Add a new score to the leaderboard.

        The records are sorted in descending order,
        and only the top five entries are kept.

        Args:
            map_name (str): Map identifier.
            player_name (str): Player name.
            score (int): Player score.
        """
        self.data[map_name].append({"name": player_name, "score": score})

        self.data[map_name].sort(key=lambda record: record["score"], reverse=True)

        # Keep only the top five scores.
        self.data[map_name] = self.data[map_name][:5]
        # Save updated leaderboard data.
        self.save()
