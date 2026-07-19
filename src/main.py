"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from dataclasses import asdict
from pathlib import Path

from recommender import load_songs, recommend_songs, UserProfile

SONGS_CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "songs.csv"

# OOP taste profile: a rock fan who leans instrumental over vocal, acoustic,
# low-energy, and somber/melancholy. Wired into Recommender once
# Recommender.recommend() is implemented.
somber_acoustic_rock_fan = UserProfile(
    favorite_genre="rock",
    favorite_artist="Voltline",
    favorite_mood="somber",
    target_energy=0.25,
    target_valence=0.20,
    target_danceability=0.20,
    target_acousticness=0.90,
    target_instrumentalness=0.80,
    target_speechiness=0.03,
    target_tempo_bpm=65,
)

# Three distinct user_prefs dicts (functional-path schema — mirrors
# UserProfile's fields, "weights" omitted so score_song falls back to
# DEFAULT_FEATURE_WEIGHTS) for comparing how the recommender responds to
# very different tastes.

# High-energy pop: loud, upbeat, danceable, vocal-forward.
high_energy_pop_fan = {
    "favorite_genre": "pop",
    "favorite_artist": "Max Pulse",
    "favorite_mood": "hype",
    "target_energy": 0.90,
    "target_valence": 0.85,
    "target_danceability": 0.88,
    "target_acousticness": 0.08,
    "target_instrumentalness": 0.02,
    "target_speechiness": 0.08,
    "target_tempo_bpm": 128,
}

# Classic country: no "country" genre exists in songs.csv, and the artist is
# invented — a deliberate cold-start case with zero categorical match.
classic_country_fan = {
    "favorite_genre": "country",
    "favorite_artist": "Dusty Trailhead",
    "favorite_mood": "nostalgic",
    "target_energy": 0.45,
    "target_valence": 0.65,
    "target_danceability": 0.40,
    "target_acousticness": 0.75,
    "target_instrumentalness": 0.05,
    "target_speechiness": 0.08,
    "target_tempo_bpm": 95,
}

# Neo-classical: quiet, acoustic, instrumental. Deliberately matches
# "Glass Cathedral" / "Echo Halden" in songs.csv as a sanity-check case.
neo_classical_fan = {
    "favorite_genre": "classical",
    "favorite_artist": "Echo Halden",
    "favorite_mood": "reflective",
    "target_energy": 0.20,
    "target_valence": 0.40,
    "target_danceability": 0.15,
    "target_acousticness": 0.95,
    "target_instrumentalness": 0.95,
    "target_speechiness": 0.02,
    "target_tempo_bpm": 65,
}


def print_recommendations(recommendations, profile_name: str = "") -> None:
    divider = "=" * 60
    header = f"TOP RECOMMENDATIONS — {profile_name}" if profile_name else "TOP RECOMMENDATIONS"
    print(f"\n{divider}")
    print(header.center(60))
    print(divider)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — Score: {score:.2f}")
        print("-" * 60)
        for reason in explanation.split("; "):
            print(f"   • {reason}")

    print(f"\n{divider}\n")


def main() -> None:
    songs = load_songs(SONGS_CSV_PATH)

    # user_prefs mirrors the UserProfile schema as a plain dict. somber_acoustic_rock_fan
    # is a UserProfile instance (the OOP path's source of truth), so it's converted with
    # asdict() here; the other three profiles are already authored as plain dicts.
    profiles = {
        "Somber Acoustic Rock": asdict(somber_acoustic_rock_fan),
        "High-Energy Pop": high_energy_pop_fan,
        "Classic Country": classic_country_fan,
        "Neo-Classical": neo_classical_fan,
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(recommendations, profile_name=profile_name)


if __name__ == "__main__":
    main()
