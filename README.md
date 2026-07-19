# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

# How Recommendations are Determined
Recommendations are offered based on the song itself and its features, such as genre, artist, energy, and so on (content-based).  The behaviors and habits of other users with similar profiles to any individual user are also factored in(collaborative).

Each feature is given a number score, and the user has a baseline score that coresponds to each feature.  Songs with features whose score is closest to that of the users' baseline will be recommended first.  It is up to the app devs on which categories to prioritize, as well as how significant the preferences of other users are.

I will be using the features already contained in the template: artist, genre, mood, energy, acousticness, mood, instrumentalness, and popularity.

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

The user profile will contain a baseline for numerical targets and string values for things like genre.  The songs will then be ranked according to the closeness of the scores to the user profile, with higher ranked feature given priority and thus being more significant.  Popularity will be used as a tie-breaker.  The nreturned list of songs will be sorted in descending order of highest rank.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output



```

TOP RECOMMENDATIONS — Somber Acoustic Rock
╒═════╤════════════════════╤════════════════╤═════════╤══════════════════════════════════════════════╕
│   # │ Title              │ Artist         │   Score │ Top Reasons                                  │
╞═════╪════════════════════╪════════════════╪═════════╪══════════════════════════════════════════════╡
│   1 │ Storm Runner       │ Voltline       │    0.43 │ • Genre match (rock): +3.00                  │
│     │                    │                │         │ • Artist match (Voltline): +3.00             │
│     │                    │                │         │ • Speechiness close to target (target 0.03,  │
│     │                    │                │         │ song 0.07): +1.30/1.50                       │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   2 │ Glass Cathedral    │ Echo Halden    │    0.43 │ • Energy close to target (target 0.25, song  │
│     │                    │                │         │ 0.20): +1.67/2.00                            │
│     │                    │                │         │ • Speechiness close to target (target 0.03,  │
│     │                    │                │         │ song 0.02): +1.45/1.50                       │
│     │                    │                │         │ • Acousticness close to target (target 0.90, │
│     │                    │                │         │ song 0.97): +1.15/1.50                       │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   3 │ Desert Static      │ Voltline       │    0.39 │ • Artist match (Voltline): +3.00             │
│     │                    │                │         │ • Valence close to target (target 0.20, song │
│     │                    │                │         │ 0.20): +2.00/2.00                            │
│     │                    │                │         │ • Speechiness close to target (target 0.03,  │
│     │                    │                │         │ song 0.04): +1.45/1.50                       │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   4 │ Spacewalk Thoughts │ Orbit Bloom    │    0.39 │ • Energy close to target (target 0.25, song  │
│     │                    │                │         │ 0.28): +1.80/2.00                            │
│     │                    │                │         │ • Speechiness close to target (target 0.03,  │
│     │                    │                │         │ song 0.03): +1.50/1.50                       │
│     │                    │                │         │ • Acousticness close to target (target 0.90, │
│     │                    │                │         │ song 0.92): +1.40/1.50                       │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   5 │ Library Rain       │ Paper Lanterns │    0.38 │ • Speechiness close to target (target 0.03,  │
│     │                    │                │         │ song 0.03): +1.50/1.50                       │
│     │                    │                │         │ • Energy close to target (target 0.25, song  │
│     │                    │                │         │ 0.35): +1.33/2.00                            │
│     │                    │                │         │ • Acousticness close to target (target 0.90, │
│     │                    │                │         │ song 0.86): +1.30/1.50                       │
╘═════╧════════════════════╧════════════════╧═════════╧══════════════════════════════════════════════╛


TOP RECOMMENDATIONS — High-Energy Pop
╒═════╤═══════════════════╤═══════════════╤═════════╤══════════════════════════════════════════════╕
│   # │ Title             │ Artist        │   Score │ Top Reasons                                  │
╞═════╪═══════════════════╪═══════════════╪═════════╪══════════════════════════════════════════════╡
│   1 │ Gym Hero          │ Max Pulse     │    0.94 │ • Genre match (pop): +3.00                   │
│     │                   │               │         │ • Artist match (Max Pulse): +3.00            │
│     │                   │               │         │ • Energy close to target (target 0.90, song  │
│     │                   │               │         │ 0.93): +1.80/2.00                            │
├─────┼───────────────────┼───────────────┼─────────┼──────────────────────────────────────────────┤
│   2 │ Sunrise City      │ Neon Echo     │    0.75 │ • Genre match (pop): +3.00                   │
│     │                   │               │         │ • Valence close to target (target 0.85, song │
│     │                   │               │         │ 0.84): +1.93/2.00                            │
│     │                   │               │         │ • Instrumentalness close to target (target   │
│     │                   │               │         │ 0.02, song 0.02): +1.50/1.50                 │
├─────┼───────────────────┼───────────────┼─────────┼──────────────────────────────────────────────┤
│   3 │ Neon Pulse Parade │ Prism Six     │    0.61 │ • Energy close to target (target 0.90, song  │
│     │                   │               │         │ 0.95): +1.67/2.00                            │
│     │                   │               │         │ • Valence close to target (target 0.85, song │
│     │                   │               │         │ 0.92): +1.53/2.00                            │
│     │                   │               │         │ • Instrumentalness close to target (target   │
│     │                   │               │         │ 0.02, song 0.01): +1.45/1.50                 │
├─────┼───────────────────┼───────────────┼─────────┼──────────────────────────────────────────────┤
│   4 │ Rooftop Lights    │ Indigo Parade │    0.47 │ • Valence close to target (target 0.85, song │
│     │                   │               │         │ 0.81): +1.73/2.00                            │
│     │                   │               │         │ • Speechiness close to target (target 0.08,  │
│     │                   │               │         │ song 0.06): +1.40/1.50                       │
│     │                   │               │         │ • Instrumentalness close to target (target   │
│     │                   │               │         │ 0.02, song 0.10): +1.10/1.50                 │
├─────┼───────────────────┼───────────────┼─────────┼──────────────────────────────────────────────┤
│   5 │ Thunder Chant     │ Iron Verse    │    0.46 │ • Energy close to target (target 0.90, song  │
│     │                   │               │         │ 0.88): +1.87/2.00                            │
│     │                   │               │         │ • Acousticness close to target (target 0.08, │
│     │                   │               │         │ song 0.08): +1.50/1.50                       │
│     │                   │               │         │ • Instrumentalness close to target (target   │
│     │                   │               │         │ 0.02, song 0.02): +1.50/1.50                 │
╘═════╧═══════════════════╧═══════════════╧═════════╧══════════════════════════════════════════════╛


TOP RECOMMENDATIONS — Classic Country
╒═════╤═════════════════════╤═════════════════╤═════════╤══════════════════════════════════════════════╕
│   # │ Title               │ Artist          │   Score │ Top Reasons                                  │
╞═════╪═════════════════════╪═════════════════╪═════════╪══════════════════════════════════════════════╡
│   1 │ Dusty Backroads     │ Dusty Trailhead │    0.96 │ • Genre match (country): +3.00               │
│     │                     │                 │         │ • Artist match (Dusty Trailhead): +3.00      │
│     │                     │                 │         │ • Energy close to target (target 0.45, song  │
│     │                     │                 │         │ 0.42): +1.80/2.00                            │
├─────┼─────────────────────┼─────────────────┼─────────┼──────────────────────────────────────────────┤
│   2 │ Coffee Shop Stories │ Slow Stereo     │    0.47 │ • Valence close to target (target 0.65, song │
│     │                     │                 │         │ 0.71): +1.60/2.00                            │
│     │                     │                 │         │ • Energy close to target (target 0.45, song  │
│     │                     │                 │         │ 0.37): +1.47/2.00                            │
│     │                     │                 │         │ • Speechiness close to target (target 0.08,  │
│     │                     │                 │         │ song 0.05): +1.35/1.50                       │
├─────┼─────────────────────┼─────────────────┼─────────┼──────────────────────────────────────────────┤
│   3 │ Velvet Whisper      │ Sable Moon      │    0.41 │ • Valence close to target (target 0.65, song │
│     │                     │                 │         │ 0.62): +1.80/2.00                            │
│     │                     │                 │         │ • Energy close to target (target 0.45, song  │
│     │                     │                 │         │ 0.50): +1.67/2.00                            │
│     │                     │                 │         │ • Instrumentalness close to target (target   │
│     │                     │                 │         │ 0.05, song 0.05): +1.50/1.50                 │
├─────┼─────────────────────┼─────────────────┼─────────┼──────────────────────────────────────────────┤
│   4 │ Island Sway         │ Coral Tide      │    0.4  │ • Instrumentalness close to target (target   │
│     │                     │                 │         │ 0.05, song 0.05): +1.50/1.50                 │
│     │                     │                 │         │ • Speechiness close to target (target 0.08,  │
│     │                     │                 │         │ song 0.06): +1.40/1.50                       │
│     │                     │                 │         │ • Energy close to target (target 0.45, song  │
│     │                     │                 │         │ 0.55): +1.33/2.00                            │
├─────┼─────────────────────┼─────────────────┼─────────┼──────────────────────────────────────────────┤
│   5 │ Open Mic Monday     │ Wordsmith Lane  │    0.37 │ • Energy close to target (target 0.45, song  │
│     │                     │                 │         │ 0.45): +2.00/2.00                            │
│     │                     │                 │         │ • Instrumentalness close to target (target   │
│     │                     │                 │         │ 0.05, song 0.02): +1.35/1.50                 │
│     │                     │                 │         │ • Live recording match (True): +1.00         │
╘═════╧═════════════════════╧═════════════════╧═════════╧══════════════════════════════════════════════╛


TOP RECOMMENDATIONS — Neo-Classical
╒═════╤════════════════════╤════════════════╤═════════╤══════════════════════════════════════════════╕
│   # │ Title              │ Artist         │   Score │ Top Reasons                                  │
╞═════╪════════════════════╪════════════════╪═════════╪══════════════════════════════════════════════╡
│   1 │ Glass Cathedral    │ Echo Halden    │    0.97 │ • Genre match (classical): +3.00             │
│     │                    │                │         │ • Artist match (Echo Halden): +3.00          │
│     │                    │                │         │ • Energy close to target (target 0.20, song  │
│     │                    │                │         │ 0.20): +2.00/2.00                            │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   2 │ Spacewalk Thoughts │ Orbit Bloom    │    0.46 │ • Instrumentalness close to target (target   │
│     │                    │                │         │ 0.95, song 0.95): +1.50/1.50                 │
│     │                    │                │         │ • Energy close to target (target 0.20, song  │
│     │                    │                │         │ 0.28): +1.47/2.00                            │
│     │                    │                │         │ • Speechiness close to target (target 0.02,  │
│     │                    │                │         │ song 0.03): +1.45/1.50                       │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   3 │ Library Rain       │ Paper Lanterns │    0.38 │ • Speechiness close to target (target 0.02,  │
│     │                    │                │         │ song 0.03): +1.45/1.50                       │
│     │                    │                │         │ • Acousticness close to target (target 0.95, │
│     │                    │                │         │ song 0.86): +1.05/1.50                       │
│     │                    │                │         │ • Energy close to target (target 0.20, song  │
│     │                    │                │         │ 0.35): +1.00/2.00                            │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   4 │ Focus Flow         │ LoRoom         │    0.32 │ • Speechiness close to target (target 0.02,  │
│     │                    │                │         │ song 0.03): +1.45/1.50                       │
│     │                    │                │         │ • Live recording match (False): +1.00        │
│     │                    │                │         │ • Instrumentalness close to target (target   │
│     │                    │                │         │ 0.95, song 0.80): +0.75/1.50                 │
├─────┼────────────────────┼────────────────┼─────────┼──────────────────────────────────────────────┤
│   5 │ Midnight Coding    │ LoRoom         │    0.29 │ • Speechiness close to target (target 0.02,  │
│     │                    │                │         │ song 0.04): +1.40/1.50                       │
│     │                    │                │         │ • Live recording match (False): +1.00        │
│     │                    │                │         │ • Valence close to target (target 0.40, song │
│     │                    │                │         │ 0.56): +0.93/2.00                            │
╘═════╧════════════════════╧════════════════╧═════════╧══════════════════════════════════════════════╛
============================================================

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

When I changed the weight of genre, I got much more varied results.  Right now genre is the most weighted factor but a song either matches or it does not, so removing that significance madde much more variety.

I tried adding songs that had features that were not in the recommender functions, but they had no effect on the algorithm.

---

## Limitations and Risks

This model is limited in its recommendations for a few important reasons. The genres are not compared for closeness, so if a song does not match the genre it is just a zero value. It also does not let the user pick what is most important to them- maybe they are not looking for a match on artists or genre at all, but instead are looking for a new genre specifically but still want instrumentalness to match.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

I learned the fundamentals on recommending algorithms.  This was huge for me, because I had not given it much thought before, and this project quantified it and made it concrete. It also taught me how important human judgment is in design, because the weights and the features could vary wildly depending on what is being searched (music, movies, games, etc.) and also how broad or general the application is.



