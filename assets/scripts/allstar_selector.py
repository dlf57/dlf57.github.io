import pandas as pd
import argparse


def data_cleaning_bref(batting, fielding):

    # Read in batting and fielding data
    df_bat = pd.read_csv(batting)
    df_field = pd.read_csv(fielding)
    # Merge batting and fielding data
    merge1_keys = ["Player", "Player-additional", "Team", "Age", "Lg", "Pos"]
    df = df_bat.merge(df_field, on=merge1_keys, how="outer", suffixes=("_bat", "_fld"))
    df["Games"] = df[["G_bat", "G_fld"]].max(axis=1)
    # Take only players that have played enough games at a specific position (* from bref)
    df = df[df["Pos"].str.contains(r"\*", na=False)].copy()
    df["Position"] = df["Pos"].str.extract(r"\*(.)")
    # Replace position codes with position names
    df["Position"] = df["Position"].replace(["7", "8", "9"], "OF")
    df["Position"] = df["Position"].replace("2", "C")
    df["Position"] = df["Position"].replace("3", "1B")
    df["Position"] = df["Position"].replace("4", "2B")
    df["Position"] = df["Position"].replace("5", "3B")
    df["Position"] = df["Position"].replace("6", "SS")
    df["Position"] = df["Position"].replace("D", "DH")

    return df


def allstar_team(data, league, c_weights, if_weights, of_weights, e_threshold=0.7):
    # Filter eligible players based on games played
    df_eligible = data[data["Games"] >= (data["Games"].max() * e_threshold)]
    df = df_eligible[df_eligible["Lg"] == league]

    # Calculate Al catchers
    df_cat = df[df["Position"] == "C"].copy()
    df_cat["Score"] = (
        (df_cat["OPS+"] / df["OPS+"].max()) * c_weights["OPS+"]
        + df_cat["rOBA"] * c_weights["rOBA"]
        + df_cat["BA"] * c_weights["BA"]
        + (df_cat["CS%"] / df["CS%"].max()) * c_weights["CS%"]
        + (df_cat["PB"] / df["PB"].max()) * c_weights["PB"]
    )
    df_c = df_cat.sort_values(by="Score", ascending=False).iloc[0]

    # Calculate Al infielders
    df_if = df[df["Position"].isin(["1B", "2B", "3B", "SS"])].copy()
    df_if["Score"] = (
        (df_if["OPS+"] / df["OPS+"].max()) * if_weights["OPS+"]
        + df_if["rOBA"] * if_weights["rOBA"]
        + df_if["BA"] * if_weights["BA"]
        + df_if["Fld%"] * if_weights["Fld%"]
        + (df_if["Ch"] / df["Ch"].max()) * if_weights["Ch"]
    )
    df_1b = (
        df_if[df_if["Position"] == "1B"]
        .sort_values(by="Score", ascending=False)
        .iloc[0]
    )
    df_2b = (
        df_if[df_if["Position"] == "2B"]
        .sort_values(by="Score", ascending=False)
        .iloc[0]
    )
    df_3b = (
        df_if[df_if["Position"] == "3B"]
        .sort_values(by="Score", ascending=False)
        .iloc[0]
    )
    df_ss = (
        df_if[df_if["Position"] == "SS"]
        .sort_values(by="Score", ascending=False)
        .iloc[0]
    )

    # Calculate Al outfielders
    df_of = df[df["Position"] == "OF"].copy()
    df_of["Score"] = (
        (df_of["OPS+"] / df["OPS+"].max()) * of_weights["OPS+"]
        + df_of["rOBA"] * of_weights["rOBA"]
        + df_of["BA"] * of_weights["BA"]
        + df_of["Fld%"] * of_weights["Fld%"]
        + (df_of["Rtot/yr"] / df["Rtot/yr"].max()) * of_weights["Rtot/yr"]
        + (df_of["Rdrs/yr"] / df["Rdrs/yr"].max()) * of_weights["Rdrs/yr"]
    )
    df_of1 = (
        df_of[df_of["Position"] == "OF"]
        .sort_values(by="Score", ascending=False)
        .iloc[0]
    )
    df_of2 = (
        df_of[df_of["Position"] == "OF"]
        .sort_values(by="Score", ascending=False)
        .iloc[1]
    )
    df_of3 = (
        df_of[df_of["Position"] == "OF"]
        .sort_values(by="Score", ascending=False)
        .iloc[2]
    )

    # Calculate Al designated hitter
    df_dh = (
        df[df["Position"] == "DH"]
        .sort_values(by=["WAR", "OPS+", "BA", "HR", "RBI"], ascending=False)
        .iloc[0]
    )

    # Put together AL team
    team = pd.DataFrame(
        [df_c, df_1b, df_2b, df_3b, df_ss, df_of1, df_of2, df_of3, df_dh],
        columns=["Player", "Position", "Team", "BA", "HR", "RBI", "OPS+"],
    )

    # Get reserves
    df_c_res = df_cat.sort_values(by="Score", ascending=False).iloc[1]
    df_1b_res = (
        df_if[df_if["Position"] == "1B"]
        .sort_values(by="Score", ascending=False)
        .iloc[1]
    )
    df_2b_res = (
        df_if[df_if["Position"] == "2B"]
        .sort_values(by="Score", ascending=False)
        .iloc[1]
    )
    df_3b_res = (
        df_if[df_if["Position"] == "3B"]
        .sort_values(by="Score", ascending=False)
        .iloc[1]
    )
    df_ss_res = (
        df_if[df_if["Position"] == "SS"]
        .sort_values(by="Score", ascending=False)
        .iloc[1]
    )
    df_of1_res = (
        df_of[df_of["Position"] == "OF"]
        .sort_values(by="Score", ascending=False)
        .iloc[3]
    )
    df_of2_res = (
        df_of[df_of["Position"] == "OF"]
        .sort_values(by="Score", ascending=False)
        .iloc[4]
    )
    df_of3_res = (
        df_of[df_of["Position"] == "OF"]
        .sort_values(by="Score", ascending=False)
        .iloc[5]
    )
    df_dh_res = (
        df[df["Position"] == "DH"]
        .sort_values(by=["WAR", "OPS+", "BA", "HR", "RBI"], ascending=False)
        .iloc[1]
    )

    # Put together AL reserves
    reserves = pd.DataFrame(
        [
            df_c_res,
            df_1b_res,
            df_2b_res,
            df_3b_res,
            df_ss_res,
            df_of1_res,
            df_of2_res,
            df_of3_res,
            df_dh_res,
        ],
        columns=["Player", "Position", "Team", "BA", "HR", "RBI", "OPS+"],
    )

    return team, reserves


# weighting factors for each area
c_weights = {
    "OPS+": 0.4,
    "rOBA": 0.3,
    "BA": 0.2,
    "CS%": 0.2,
    "PB": -0.1,
}

if_weights = {"OPS+": 0.4, "rOBA": 0.3, "BA": 0.2, "Fld%": 0.2, "Ch": 0.1}

of_weights = {
    "OPS+": 0.4,
    "rOBA": 0.3,
    "BA": 0.2,
    "Fld%": 0.3,
    "Rtot/yr": 0.1,
    "Rdrs/yr": 0.1,
}


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-bat", "--batting", required=True, help="Batting csv file")
    parser.add_argument("-field", "--fielding", required=True, help="Fielding csv file")
    parser.add_argument("-ref", "--refsite", required=True, help="Site csv are from")
    args = parser.parse_args()

    # Read in and clean data
    if args.refsite == "Baseball-Reference" or args.refsite == "bref":
        df = data_cleaning_bref(args.batting, args.fielding)
    else:
        raise ValueError("Unsupported reference site. Only Baseball Reference is currently supported.")

    # Calculate All-Star teams
    al_1st, al_2nd = allstar_team(df, "AL", c_weights, if_weights, of_weights)
    nl_1st, nl_2nd = allstar_team(df, "NL", c_weights, if_weights, of_weights)
    print("AL All-Star Team:")
    print(al_1st)
    print("\nAL Reserves:")
    print(al_2nd)
    print("NL All-Star Team:")
    print(nl_1st)
    print("\nNL Reserves:")
    print(nl_2nd)


if __name__ == "__main__":
    main()
