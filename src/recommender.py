import csv
import heapq
from typing import List, Dict, Tuple, Optional
from dataclasses import asdict, dataclass, field

NUMERIC_FIELDS = (
    "energy",
    "tempo_bpm",
    "valence",
    "danceability",
    "acousticness",
    "popularity",
    "instrumentalness",
    "speechiness",
)

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float
    popularity: float
    instrumentalness: float
    speechiness: float

# Default feature weights, per the Phase 2 Algorithm Recipe.
# Categorical matches (genre, artist) are weighted highest; numeric
# closeness-to-target features follow. Popularity is intentionally
# excluded here — it is used only as a tie-breaker, never scored directly.
DEFAULT_FEATURE_WEIGHTS: Dict[str, float] = {
    "genre": 3.0,
    "artist": 3.0,
    "energy": 2.0,
    "valence": 2.0,
    "acousticness": 1.5,
    "instrumentalness": 1.5,
    "speechiness": 1.5,
    "danceability": 1.0,
    "tempo_bpm": 1.0,
}

# Numeric features scored by closeness-to-target, mapped to the UserProfile /
# user_prefs key that holds each feature's target value.
NUMERIC_TARGET_FEATURES: Dict[str, str] = {
    "energy": "target_energy",
    "valence": "target_valence",
    "danceability": "target_danceability",
    "acousticness": "target_acousticness",
    "instrumentalness": "target_instrumentalness",
    "speechiness": "target_speechiness",
    "tempo_bpm": "target_tempo_bpm",
}

# Design note: our Algorithm Recipe calls for the "spread" in the linear
# closeness formula (1 - distance / spread) to come from the variance of a
# user's listening history. This simulation doesn't track listening history —
# a UserProfile is a single authored target — so these are fixed tolerances
# standing in for spread. tempo_bpm uses a wider absolute tolerance since it
# isn't on the same 0-1 scale as the other features.
FEATURE_TOLERANCES: Dict[str, float] = {
    "energy": 0.3,
    "valence": 0.3,
    "danceability": 0.3,
    "acousticness": 0.3,
    "instrumentalness": 0.3,
    "speechiness": 0.3,
    "tempo_bpm": 40.0,
}

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_artist: str
    favorite_mood: str
    target_energy: float
    target_valence: float
    target_danceability: float
    target_acousticness: float
    target_instrumentalness: float
    target_speechiness: float
    target_tempo_bpm: float
    weights: Dict[str, float] = field(default_factory=lambda: dict(DEFAULT_FEATURE_WEIGHTS))

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs for user, ranked by score with popularity as the tie-breaker."""
        user_prefs = asdict(user)
        scored = []
        for song in self.songs:
            score, _reasons = score_song(user_prefs, asdict(song))
            scored.append((song, score))

        top = heapq.nlargest(k, scored, key=lambda entry: (entry[1], entry[0].popularity))
        return [song for song, _score in top]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a semicolon-joined explanation of how song scored against user's preferences."""
        _score, reasons = score_song(asdict(user), asdict(song))
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts, converting numeric fields to float."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for field_name in NUMERIC_FIELDS:
                row[field_name] = float(row[field_name])
            row["id"] = int(row["id"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score song against user_prefs via weighted categorical and numeric closeness, returning (score, reasons)."""
    weights = user_prefs.get("weights", DEFAULT_FEATURE_WEIGHTS)
    reasons: List[str] = []
    weighted_total = 0.0
    total_weight = 0.0

    # --- Categorical features: genre, artist ---
    for feature_name, pref_key in (("genre", "favorite_genre"), ("artist", "favorite_artist")):
        weight = weights.get(feature_name, 0.0)
        if weight <= 0:
            continue

        preferred_value = user_prefs[pref_key]
        song_value = song[feature_name]
        is_match = song_value == preferred_value
        feature_score = 1.0 if is_match else 0.0
        contribution = weight * feature_score

        weighted_total += contribution
        total_weight += weight

        if is_match:
            reasons.append(f"{feature_name.capitalize()} match ({song_value}): +{contribution:.2f}")
        else:
            reasons.append(
                f"{feature_name.capitalize()} mismatch (wanted {preferred_value}, got {song_value}): +0.00"
            )

    # --- Numeric features: closeness to target, linear falloff ---
    for feature_name, target_key in NUMERIC_TARGET_FEATURES.items():
        weight = weights.get(feature_name, 0.0)
        if weight <= 0:
            continue

        target_value = user_prefs[target_key]
        song_value = song[feature_name]
        tolerance = FEATURE_TOLERANCES[feature_name]

        distance = abs(song_value - target_value)
        closeness = max(0.0, 1.0 - distance / tolerance)
        contribution = weight * closeness

        weighted_total += contribution
        total_weight += weight

        reasons.append(
            f"{feature_name.capitalize()} close to target "
            f"(target {target_value:.2f}, song {song_value:.2f}): +{contribution:.2f}/{weight:.2f}"
        )

    final_score = weighted_total / total_weight if total_weight > 0 else 0.0
    return final_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score and rank all songs for user_prefs, returning the top-k as (song, score, explanation) tuples."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored.append((song, score, explanation))

    # Rank by score; ties broken by popularity (never scored directly, per
    # the Algorithm Recipe — it only breaks ties here at ranking time).
    return heapq.nlargest(k, scored, key=lambda entry: (entry[1], entry[0]["popularity"]))
