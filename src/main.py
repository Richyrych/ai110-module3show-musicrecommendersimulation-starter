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


def print_recommendations(recommendations) -> None:
    divider = "=" * 60
    print(f"\n{divider}")
    print("TOP RECOMMENDATIONS".center(60))
    print(divider)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — Score: {score:.2f}")
        print("-" * 60)
        for reason in explanation.split("; "):
            print(f"   • {reason}")

    print(f"\n{divider}\n")


def main() -> None:
    songs = load_songs(SONGS_CSV_PATH)

    # user_prefs mirrors the UserProfile schema as a plain dict, derived from
    # the same somber_acoustic_rock_fan instance used by the OOP path — one
    # source of truth for the taste profile across both implementations.
    user_prefs = asdict(somber_acoustic_rock_fan)

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print_recommendations(recommendations)


if __name__ == "__main__":
    main()
