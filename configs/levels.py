from .paths import asset_path

RANDOM_FOODS = [
    asset_path("common", "images", "food", "apple.png"),
    asset_path("common", "images", "food", "orange.png"),
]

RANDOM_OBSTACLE_POOL = [
    {
        "image": asset_path("common", "images", "obstacles", "rock.png"),
        "size": 3,
    },
    {
        "image": asset_path(
            "common", "images", "obstacles", "rock_with_grass.png"
        ),
        "size": 4,
    },
    {
        "image": asset_path("common", "images", "obstacles", "tree.png"),
        "size": 6,
    },
    {
        "image": asset_path(
            "common", "images", "obstacles", "autumn_tree.png"
        ),
        "size": 8,
    },
    {
        "image": asset_path("common", "images", "obstacles", "snowman.png"),
        "size": 4,
    },
]

LEVELS = {
    "spring": {
        "panel": asset_path("levels", "spring", "images", "panels", "panel.png"),
        "panel_hover": asset_path(
            "levels", "spring", "images", "panels", "panel_hover.png"
        ),
        "background": asset_path(
            "levels", "spring", "images", "backgrounds", "background.png"
        ),
        "food": asset_path("common", "images", "food", "apple.png"),
        "obstacles": [],
    },
    "summer": {
        "panel": asset_path("levels", "summer", "images", "panels", "panel.png"),
        "panel_hover": asset_path(
            "levels", "summer", "images", "panels", "panel_hover.png"
        ),
        "background": asset_path(
            "levels", "summer", "images", "backgrounds", "background.png"
        ),
        "food": asset_path("common", "images", "food", "apple.png"),
        "obstacles": [
            {
                "image": asset_path("common", "images", "obstacles", "rock.png"),
                "position": [6, 6],
                "size": 3,
            },
            {
                "image": asset_path("common", "images", "obstacles", "rock_with_grass.png"),
                "position": [13, 12],
                "size": 4,
            },
            {
                "image": asset_path("common", "images", "obstacles", "rock.png"),
                "position": [4, 12],
                "size": 3,
            },
            {
                "image": asset_path("common", "images", "obstacles", "tree.png"),
                "position": [19, 4],
                "size": 6,
            },
        ],
    },
    "autumn": {
        "panel": asset_path("levels", "autumn", "images", "panels", "panel.png"),
        "panel_hover": asset_path(
            "levels", "autumn", "images", "panels", "panel_hover.png"
        ),
        "background": asset_path(
            "levels", "autumn", "images", "backgrounds", "background.png"
        ),
        "food": asset_path("common", "images", "food", "apple.png"),
        "play_area": {"x_min": 1, "x_max": 30, "y_min": 1, "y_max": 18},
        "obstacles": [
            {
                "image": asset_path("common", "images", "obstacles", "autumn_tree.png"),
                "position": [20, 11],
                "size": 8,
            }
        ],
    },
    "winter": {
        "panel": asset_path("levels", "winter", "images", "panels", "panel.png"),
        "panel_hover": asset_path(
            "levels", "winter", "images", "panels", "panel_hover.png"
        ),
        "background": asset_path(
            "levels", "winter", "images", "backgrounds", "background.png"
        ),
        "food": asset_path("common", "images", "food", "orange.png"),
        "obstacles": [
            {
                "image": asset_path("common", "images", "obstacles", "snowman.png"),
                "position": [7, 8],
                "size": 4,
            },
            {
                "image": asset_path("common", "images", "obstacles", "snowman.png"),
                "position": [14, 8],
                "size": 4,
            },
            {
                "image": asset_path("common", "images", "obstacles", "snowman.png"),
                "position": [21, 8],
                "size": 4,
            },
            {
                "image": asset_path("common", "images", "obstacles", "snowman.png"),
                "position": [7, 15],
                "size": 4,
            },
            {
                "image": asset_path("common", "images", "obstacles", "snowman.png"),
                "position": [14, 15],
                "size": 4,
            },
            {
                "image": asset_path("common", "images", "obstacles", "snowman.png"),
                "position": [21, 15],
                "size": 4,
            },
        ],
    },
    "random": {
        "panel": asset_path(
            "levels", "random", "images", "panels", "panel.png"
        ),
        "panel_hover": asset_path(
            "levels", "random", "images", "panels", "panel_hover.png"
        ),
        "background": asset_path(
            "levels", "random", "images", "backgrounds", "background.png"
        ),
        "foods": RANDOM_FOODS,
        "obstacle_pool": RANDOM_OBSTACLE_POOL,
        "obstacle_count": [2, 6],
    },
}
