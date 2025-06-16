---
layout: single
title:  "2025 MLB All Star Game Selector"
excerpt: "Select your votes for the upcoming 2025 All Star Game using batting and fielding statistics."
date:   2025-06-15
categories: projects
author_profile: true
---

# Making My MLB All Star Selections with Data
This project uses real MLB batting and fielding statistics to pick the most deserving All Star players in each league. By combining performance metrics and positional eligibility rules, the script automatically selects starters and reserves for both the American and National League All Star teams. (Reserves to give you options if there is a player you really do not want to select in your fan vote.)

## Project Overview
The goal of this script is to provide a data-driven approach to selecting MLB All Stars. Rather than relying on name recognition or market size, this tool evaluates each player's performance using advanced metrics from both offensive and defensive perspectives.

#### Key Features
- Data Cleaning: Merges and filters batting and fielding CSVs.
- Scoring System: Computes a custom performance score for each position using weighted stats.
- Eligibility Filter: Only considers players with a minimum number of games at a given position.
- All Star Team Selection: Selects starters and backups for each position across both AL and NL.

## Scoring System
Each position has a custom set of weighted metrics that best reflect player value:

Catcher

| Stat | Weight |
| ---- | ------ |
| OPS+ | 0.4    |
| rOBA | 0.3    |
| BA   | 0.2    |
| CS%  | 0.2    |
| PB   | -0.1   |

Infielders (1B, 2B, SS, 3B)

| Stat | Weight |
| ---- | ------ |
| OPS+ | 0.4    |
| rOBA | 0.3    |
| BA   | 0.2    |
| Fld% | 0.2    |
| Ch   | 0.1    |

Outfielders

| Stat    | Weight |
| ------- | ------ |
| OPS+    | 0.4    |
| rOBA    | 0.3    |
| BA      | 0.2    |
| Fld%    | 0.3    |
| Rtot/yr | 0.1    |
| Rdrs/yr | 0.1    |

For DH, performance is based on a simple sort of WAR, OPS+, BA, HR, and RBI.

##### Note on Weights
The statistical weights used in this project reflect my personal perspective on how to evaluate players at each position. I selected metrics that align with what I value in player performance, and weighted them accordingly. However, this area presents a strong opportunity for refinement. Further analysis could explore more sophisticated tuning of these parameters and include additional metrics such as wOBA.

## How It Works
1. Run the script via command line:
```
python allstar_predictor.py -bat batting_stats.csv -field fielding_stats.csv -ref Baseball-Reference
```

2. The script:
- Reads and merges batting and fielding data
- Filters for players who have played enough at a given position
- Scores players by position
- Selects the top performer (starter) and runner-up (reserve) at each position
- Outputs predicted AL and NL All Star rosters

Example of NL All Star Team:

| Player              | Position | Team | BA    | HR   | RBI  | OPS+  |
| ------------------- | -------- | ---- | ----- | ---- | ---- | ----- |
| Will Smith	      | C	     | LAD	| 0.324 | 6.0  | 37.0 | 166.0 |
| Pete Alonso	      | 1B       | NYM	| 0.298 | 17.0 | 63.0 | 180.0 |
| Brice Turang	      | 2B	     | MIL	| 0.265 | 4.0  | 26.0 | 99.0  |
| Matt Chapman	      | 3B	     | SFG	| 0.243 | 12.0 | 30.0 | 135.0 |
| Francisco Lindor	  | SS	     | NYM	| 0.279 | 14.0 | 38.0 | 137.0 |
| Pete Crow-Armstrong |	OF	     | CHC	| 0.271 | 18.0 | 57.0 | 142.0 |
| Juan Soto	          | OF	     | NYM	| 0.253 | 13.0 | 35.0 | 147.0 |
| James Wood	      | OF	     | WSN	| 0.281 | 16.0 | 45.0 | 157.0 |
| Shohei Ohtani	      | DH	     | LAD	| 0.290 | 23.0 | 39.0 | 183.0 |


## Data Requirements
The script expects two CSV files:
- Batting: Must include columns like Player, OPS+, rOBA, BA, etc.
- Fielding: Should contain Fld%, Ch, CS%, PB, Rtot/yr, Rdrs/yr, and similar.

Currently, the data cleanup is for Baseball Reference but working on Fangraphs inclusion for more advanced stats.

## Customization
You can easily tune the weighting dictionaries (c_weights, if_weights, of_weights) to explore different philosophies whether you want to favor defense, slugging, or balance.

## Try it Out!
[Download the Script](../../assets/scripts/allstar_selector.py)