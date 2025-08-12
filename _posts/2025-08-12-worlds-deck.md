---
layout: single
title:  "Picking the Deck to Win Pokemon Worlds 2025"
excerpt: "Simulating what deck is most likely to win Pokemon Worlds 2025 in TCG."
date:   2025-08-12
categories: projects
author_profile: true
classes: wide
header:
    teaser: /assets/images/meta.png
---

## Setting the Stage
Pokemon Worlds 2025 is just around the corner and the meta game has been heating up since the release of Black Bolt and White Flare. Going into the Black Bolt and White Flare release, the three top performing decks were Raging Blot, Grimmsnarl, and Gardevior with solo Dragapult being the most common of it's variants. Newly introduced cards like [Genesect ex](https://pkmncards.com/card/genesect-ex-black-bolt-blk-067/), [Hilda](https://pkmncards.com/card/hilda-white-flare-wht-084/), and [Brave Bangle](https://pkmncards.com/card/brave-bangle-white-flare-wht-080/) and returning cards like [Air Balloon](https://pkmncards.com/card/air-balloon-black-bolt-blk-079/) have shaken up the meta significantly. 

## The Plan
To determine what deck we should pick if we were going to Worlds/what deck we think stands the strongest chance to win worlds, we will be analyzing the meta and matchups and then run some Monte Carlo simulations to get an idea of the standout deck(s). For those new to Monte Carlo simulations, it is a technique that uses random sampling to model different outcomes. In this project we will take a deck and then simulate a tournament run by randomly selecting a deck to play against every round. We then calculate the probability of the deck winning a best of 3 set against the randoly selected decks. 

To best simulate the Worlds tournament, we have to take into account the tournament structure. I will be basing the structure off of the 2024 Worlds tournament so there might be more rounds than will be in the 2025 tournament. To start, all players will play in a Day 1 8 round Swiss elimination where 6 wins is needed to make Day 2. We will run a Monte Carlo simulation of all decks for 8 rounds and determine the probability that a deck makes Day 2 of the tournament. We will then use these probabilities to construct a likely Day 2 meta. This Day 2 meta will be used to simulate the Day 2 an additional 4 rounds of swiss followed by a Top Cut of 16. From here, we can get the probablitiy that a deck will win the World Championship and then compare that to the other decks to determin which deck has the highest chance to become the Worlds winning deck. 

## Caveats
Without any official in-person tournaments, we have had to turn to online hosted tournaments on sites like [Limitless](https://play.limitlesstcg.com/) to get an idea of the meta shake up. While good for indications of the meta, caveats need to be made for conclusions made from this data. First, online tournaments can be entered by anyone whereas the Pokemon Worlds tournament is invite only with the below structure for TCG players in TPCi regions. In TPC regions, players qualified through their country's championship tournament or Master Ball League tournaments where the number of spots getting an invite varied by region. In addition to qualifying through these established means, winners of TPCi regionals or special events and top 4 at international championships recieved automatic invites that would not go against thier regions top X qualifiers. Suffice it to say, these are a the best of the best and only a small handful of those who play. I do not want to insinuate that the online players we will be basing our data on are worse than these world qualifiers, but there may be a difference in skill level which is why we will be using only data from players who made Top 16 in these online tournaments. This feels like an acceptable compromise to try and represent the caliber of players playing at Worlds. 

| Region        | Qualifiers |
|---------------|------------|
| USA & Canada  | Top 125    |
| Europe        | Top 125    |
| Latin America | Top 100    |
| Oceania       | Top 20     |
| Middle East & South Africa | Top 10 |

The second caveat we need to make is that a lot of online tournaments are best of 1 (BO1) with top cut possibly being best of 3 (BO3) if it is a larger tournament. The official Pokemon TCG format is a BO3. In our work here we can try our best to account for this but when looking at Top 16 metas, decks that perform best in BO1 might overperform when compared to the official BO3 format. 


## Now let's get into the data!
**Special thanks to [Trainer hill](https://www.trainerhill.com/), a very useful site that aggergates a lot of tournament and gives meta overviews as well as decklist analysis. Please go check them out if this stuff interests you!**

This is just a brief summary of the results. If you are interested in the code and full notebook, please check it out on [GitHub](https://github.com/dlf57/pkmnworlds25_deck_sim/blob/main/worlds2025_deck_sim.ipynb)!

### Overall Meta Performance

| Deck                   | Win % vs Meta |
|------------------------|---------------|
| dragapult-dusknoir     | 55.931792     |
| grimmsnarl-froslass    | 55.109229     |
| charizard-dusknoir     | 53.742822     |
| gardevoir-ex-sv        | 51.940777     |
| charizard-pidgeot      | 51.201420     |
| dragapult-charizard    | 48.121406     |
| dragapult-ex           | 47.566340     |
| crustle-dri            | 47.122858     |
| ethan-typhlosion       | 46.639733     |
| joltik-box             | 45.639208     |
| froslass-munkidori     | 43.252245     |
| raging-bolt-ogerpon    | 40.703367     |
| gholdengo-ex           | 35.813771     |
| flareon-noctowl        | 35.778029     |
| ho-oh-armarouge        | 34.811957     |

While this does not necessiarly tell us which deck will win in our simulations, it does give a broad overview of just how well that deck does against the meta as a whole. It will be interesting to see if there are any differences or similarites when we simulate based on meta distribution. Some decks might be getting boosted by some rare, but highly favorable matchups. 

### Simulated Day 2 Meta

| Deck                   | Simulated Meta Share   | Day 1 Meta Share | 
|------------------------|------------------------|------------------|
| grimmsnarl-froslass    | 22.344081              | 11.4             |
| dragapult-dusknoir     | 17.124840              | 10.6             |
| gardevoir-ex-sv        | 10.619395              | 7.7              |
| gholdengo-ex           | 8.089174               | 11.5             |
| charizard-pidgeot      | 7.637681               | 5.3              |
| dragapult-charizard    | 7.508441               | 4.2              |
| joltik-box             | 5.116310               | 4.2              |
| ethan-typhlosion       | 4.995482               | 5.6              |
| crustle-dri            | 4.874653               | 3.5              |
| dragapult-ex           | 4.655703               | 6.4              |
| raging-bolt-ogerpon    | 2.553631               | 6.2              |
| charizard-dusknoir     | 2.412115               | 1.3              |
| flareon-noctowl        | 1.220310               | 3.1              |
| froslass-munkidori     | 0.601870               | 1.1              |
| ho-oh-armarouge        | 0.246313               | 1.6              |


### Final Results & Top Decks

| Deck                   | Top 16%  | Win %  |
|------------------------|----------|--------|
| dragapult-charizard    | 31.626   | 2.005  |
| grimmsnarl-froslass    | 31.071   | 1.939  |
| joltik-box             | 31.328   | 1.925  |
| dragapult-dusknoir     | 29.732   | 1.836  |
| charizard-dusknoir     | 27.442   | 1.319  |
| charizard-pidgeot      | 25.778   | 1.158  |
| crustle-dri            | 24.337   | 1.026  |
| gholdengo-ex           | 24.234   | 1.013  |
| gardevoir-ex-sv        | 22.792   | 0.824  |
| dragapult-ex           | 15.476   | 0.323  |
| froslass-munkidori     | 14.197   | 0.261  |
| flareon-noctowl        | 13.621   | 0.256  |
| ethan-typhlosion       | 13.105   | 0.210  |
| raging-bolt-ogerpon    | 9.835    | 0.104  |
| ho-oh-armarouge        | 6.862    | 0.039  |


## Tournament Outcome

It is impossible to say that there is one clear winner for deck choice when there is less than a 0.17% difference in chance to win Worlds between the top 4 decks. The top 4 decks, Dragapult/Charizard, Grimmsnarl, Joltik Box, and Dragapult/Dusknoir, all seem to be solid pick for this upcoming weekend.

I do think it is surprising to See Joltik Box and Dragapult/Charizard in the top choices. Their meta shares going into Day 1 were both 4.2% with a bump to 5.1% for Joltik Box and 7.5% for Dragapult/Charizard from the Day 2 conversion simulation. 

Personally, my pick for winning Worlds is Dragapult/Dusknoir. While Gardevoir was only given a 0.8% chance to win Worlds, this does not account for Day 2 Gardevoir players being some of the most skilled players having 1/3 internationals and 10/31 regional/special events this season. While Dragapult/Charizard has a better matchup into Gardevoir, I belive Dragapult/Dusknoir trades a bit off of that matchup for a better matchup against the overall field, making it my pick. 

Now if you are curious about how an open field Worlds might turn out and what you should probably be playing to your local Cups and Challenges until the next set, please go checkout the [full notebook](https://github.com/dlf57/pkmnworlds25_deck_sim/blob/main/worlds2025_deck_sim.ipynb).