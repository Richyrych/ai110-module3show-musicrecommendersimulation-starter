from src.recommender import Song, UserProfile, Recommender

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
            popularity=0.85,
            instrumentalness=0.02,
            speechiness=0.06,
            release_decade=2020,
            live_recording=False,
            loudness=-4.0,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
            popularity=0.35,
            instrumentalness=0.75,
            speechiness=0.04,
            release_decade=2020,
            live_recording=False,
            loudness=-9.0,
        ),
    ]
    return Recommender(songs)


def make_pop_lover_profile() -> UserProfile:
    return UserProfile(
        favorite_genre="pop",
        favorite_artist="Test Artist",
        favorite_mood="happy",
        target_energy=0.8,
        target_valence=0.9,
        target_danceability=0.8,
        target_acousticness=0.2,
        target_instrumentalness=0.02,
        target_speechiness=0.06,
        target_tempo_bpm=120,
        target_release_decade=2020,
        prefers_live=False,
        target_loudness=-4.0,
    )


def test_recommend_returns_songs_sorted_by_score():
    user = make_pop_lover_profile()
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = make_pop_lover_profile()
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_user_profile_default_weights_match_algorithm_recipe():
    user = make_pop_lover_profile()

    assert user.weights["genre"] == 3.0
    assert user.weights["artist"] == 3.0
    assert user.weights["energy"] == 2.0
    assert user.weights["valence"] == 2.0
    assert user.weights["acousticness"] == 1.5
    assert user.weights["instrumentalness"] == 1.5
    assert user.weights["speechiness"] == 1.5
    assert user.weights["danceability"] == 1.0
    assert user.weights["tempo_bpm"] == 1.0
    assert user.weights["release_decade"] == 1.0
    assert user.weights["live_recording"] == 1.0
    assert user.weights["loudness"] == 1.0
    # Popularity is a tie-breaker only, never a scored/weighted feature.
    assert "popularity" not in user.weights


def test_user_profile_accepts_custom_weights():
    custom_weights = {"genre": 5.0, "artist": 1.0}
    user = UserProfile(
        favorite_genre="pop",
        favorite_artist="Test Artist",
        favorite_mood="happy",
        target_energy=0.8,
        target_valence=0.9,
        target_danceability=0.8,
        target_acousticness=0.2,
        target_instrumentalness=0.02,
        target_speechiness=0.06,
        target_tempo_bpm=120,
        target_release_decade=2020,
        prefers_live=False,
        target_loudness=-4.0,
        weights=custom_weights,
    )

    assert user.weights == custom_weights
