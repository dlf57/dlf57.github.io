---
layout: single
title:  "Comparing Baseball Players Like Molecules!"
excerpt: "Statistical fingerprints for baseball players — find their closest matches."
date:   2025-08-19
categories: projects
author_profile: true
classes: wide
header:
    teaser: /assets/images/diamondfp2.png
---

I’ve been working on a new Python library called [`diamondfp`](https://github.com/dlf57/diamondfp), designed to bring ideas from cheminformatics into the world of baseball analytics. In chemistry, molecular similarity is often measured by encoding molecules into fingerprints (binary feature vectors) and comparing them with metrics like the Tanimoto coefficient (also known as the Jaccard score).

[`diamondfp`](https://github.com/dlf57/diamondfp) applies the same idea to baseball: it creates statistical fingerprints of players, enabling similarity searches between careers, seasons, or even specific performance slices.

**What [`diamondfp`](https://github.com/dlf57/diamondfp) does**
- Encodes players into binary fingerprints or binned quantile fingerprints
- Works with hitting, pitching, and fielding statistics
- Allows comparisons across players, eras, and styles
- Supports rookie similarity searches, useful when modeling new players in machine learning workflows

By representing performance as a fingerprint, we can do fast, interpretable similarity searches. Who is the closest comparable player for Shohei Ohtani? How does Babe Ruth’s statistical profile match up with modern hitters? With diamondfp, you can start answering those kinds of questions.


### Example Usage
```python
import pandas as pd
from diamondfp.fingerprints import binaryfp, binnedfp
from diamondfp.utils.features import generate_quantiles
from diamondfp.scoring import jaccard, manhattan, cosine_sim

df = pd.read_csv("data/career-batting.csv")

stat_features = {
    "H": [0.5, 0.75, 0.9, 0.95],
    "2B": [0.75, 0.95],
    "3B": [0.75, 0.95],
    "HR": [0.9, 0.99],
    "K%": [0.1, 0.25],
    "BB%": [0.75, 0.99],
    "AVG": [0.5, 0.75, 0.9, 0.95],
    "OBP": [0.5, 0.75, 0.9, 0.95],
    "SLG": [0.5, 0.75, 0.9, 0.95],
    "OPS": [0.5, 0.75, 0.9, 0.95],
}

feat_quants = generate_quantiles(df, stat_features)

babe_ruth = binaryfp(df[df["Name"] == "Babe Ruth"].squeeze(), feat_quants)
shohei_ohtani = binaryfp(df[df["Name"] == "Shohei Ohtani"].squeeze(), feat_quants)
sim_score = jaccard(babe_ruth, shohei_ohtani)
print(f"Jaccard score: {sim_score:0.2f}")  # 0.72
cos_sim = cosine_sim(babe_ruth, shohei_ohtani)
print(f"Cosine similarity: {cos_sim:0.2f}")  # 0.85
man_dist = manhattan(babe_ruth, shohei_ohtani)
print(f"Manhattan distance: {man_dist}")  # 5
```

This snippet encodes Babe Ruth and Shohei Ohtani into binary fingerprints and compares them using three different similarity metrics: Jaccard/Tanimoto, Cosine similarity, and Manhattan distance.

### Try it Out!

Curious to try it yourself? Head over to [GitHub](https://github.com/dlf57/diamondfp) and dive in! I've included [example scripts & notebooks](https://github.com/dlf57/diamondfp/blob/main/examples/examples.md) so you can start comparing players today.