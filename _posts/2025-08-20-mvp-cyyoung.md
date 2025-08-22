---
layout: single
title:  "Who Matches the MVP and Cy Young Profile in 2025?"
excerpt: "Using Statistical Fingerprints to Predict Baseball’s 2025 Award Winners."
date:   2025-08-20
categories: projects
author_profile: true
classes: wide
header:
    teaser: /assets/images/mvprace.png
---

Baseball award races are always full of debate, but what if we could take a more data-driven approach to identifying likely winners? Using [`diamondfp`](https://github.com/dlf57/diamondfp), a library that builds statistical fingerprints for players, I set out to see which players in 2025 most resemble past MVP and Cy Young winners. By creating composite fingerprints from past award winners and comparing them to this season’s performances, we can get a different perspective on who matches the award-winning profile

## The Process
- Select the stats and quantiles most relevant to award decisions
- Generate fingerprints for all MVP and Cy Young winners from 2015–2024
- Build a composite fingerprint that represents a typical award winner
- Compare this composite to all current-season players
- Rank the results to see who most closely matches the MVP and Cy Young profiles

**Notebooks for full analysis**

[MVP Race](https://github.com/dlf57/diamondfp/blob/main/examples/mvp_fp_search.ipynb)

[Cy Young Race](https://github.com/dlf57/diamondfp/blob/main/examples/cy_young_fp_search.ipynb)

## The Results
### MVP Race
**AL MVP Candidates**

| Rank | Player | Similarity |
|--|--|--|
| 1st | Aaron Judge | 0.88 |
| 2nd | Cal Raleigh | 0.32 |
| 3rd | Jonathan Aranda | 0.20 |

**NL MVP Candidates**

| Rank | Player | Similarity |
|--|--|--|
| 1st | Shohei Ohtani | 0.72 |
| 2nd | Kyle Schwarber | 0.48 |
| 3rd | Juan Soto | 0.32 |
| 3rd | Oneil Cruz | 0.32 |

**Takeaways:** Aaron Judge projects to earn his 3rd MVP, while Shohei Ohtani could secure his 4th. That said, the method does not capture defensive value, which could boost someone like Cal Raleigh, nor does it consider how baseball writers often weigh narratives over pure numbers.

### Cy Young Race
**AL Cy Young Candidates**

| Rank | Player | Similarity |
|--|--|--|
| 1st | Tarik Skubal  | 0.35 |
| 2nd | Garret Crochet | 0.30 |
| 3rd | Jacob deGrom | 0.26 |

**NL Cy Young Candidates**

| Rank | Player | Similarity |
|--|--|--|
| 1st | Paul Skenes | 0.39 |
| 2nd | Zack Wheeler | 0.31 |
| 3rd | Yoshinobu Yamamoto | 0.26 |

**Takeaways:** Tarik Skubal looks poised for his second Cy Young, while rookie Paul Skenes is making a strong case for his first. Similarity scores were lower overall, likely because of the wide range of pitching statistics included. A more streamlined feature set may improve results.

**Note:** These results are as of 8/20/2025

## Final Thoughts
This analysis is not meant to be a definitive prediction of who will take home the MVP and Cy Young awards, but rather a demonstration of how fingerprint similarity can surface players who resemble past winners. The results line up with some obvious choices, like Aaron Judge, Shohei Ohtani, and Tarik Skubal, while also highlighting less-expected names such as Cal Raleigh. With more refinement, like incorporating defensive metrics or adjusting the pitching feature set, this approach could provide an even sharper lens on award races. At the very least, it shows how [`diamondfp`](https://github.com/dlf57/diamondfp) can be used to build player comparisons in ways that go beyond traditional stat lines.
