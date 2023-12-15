import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

plyr_salary = pd.read_csv("Dataset\RankedPlayersbySalaryNonCurr.csv", encoding="unicode_escape")
plyr_points = pd.read_csv("Dataset\RankedPlayersbyPoints.csv", encoding='unicode_escape')
plyr_assists = pd.read_csv("Dataset\RankedPlayersbyAssists.csv", encoding='unicode_escape')
plyr_rebounds = pd.read_csv("Dataset\RankedPlayersbyRebounds.csv", encoding='unicode_escape')

plyr_salary["Price Per Minimum Played_C"] = np.round(plyr_salary['Salary 2023-24'] / 65, 2)

salarytopoints_df = pd.merge(plyr_salary, plyr_points, on= 'Player')
salarytopoints_df["Current Salary vs. Performance_wP"] = np.round(salarytopoints_df['Salary 2023-24'] / (salarytopoints_df['PTS'] * 1.5 + salarytopoints_df['AST'] * 1.25 + salarytopoints_df['TRB'] * 1.25 + salarytopoints_df['G']), 2)
salarytopoints_df["Current Salary vs. Performance_wPFG"] = np.round(salarytopoints_df['Salary 2023-24'] / (salarytopoints_df['PTS'] * 1.5 + salarytopoints_df['AST'] * 1.2 + salarytopoints_df['TRB'] * 1 + salarytopoints_df['G']), 2)
salarytopoints_df["Accuracy Of Pay_wP"] = (salarytopoints_df['Price Per Minimum Played_C'] - salarytopoints_df["Current Salary vs. Performance_wP"])
salarytopoints_df["Accuracy Of Pay_wPFG"] = salarytopoints_df['Price Per Minimum Played_C'] - salarytopoints_df["Current Salary vs. Performance_wPFG"]
salarytopoints_df = salarytopoints_df.sort_values('PTS', ascending= False)

salarytoassists_df = pd.merge(plyr_salary, plyr_assists, on= 'Player')
salarytoassists_df["Current Salary vs. Performance_wA"] = np.round(salarytoassists_df['Salary 2023-24'] / (salarytoassists_df['PTS'] * 1.25 + salarytoassists_df['AST?'] * 1.5 + salarytoassists_df['TRB'] * 1.25 + salarytoassists_df['G']), 2)
salarytoassists_df["Current Salary vs. Performance_wAFG"] = np.round(salarytoassists_df['Salary 2023-24'] / (salarytoassists_df['PTS'] * 1.5 + salarytoassists_df['AST?'] * 1.2 + salarytoassists_df['TRB'] * 1 + salarytoassists_df['G']), 2)
salarytoassists_df["Accuracy Of Pay_wA"] = salarytoassists_df['Price Per Minimum Played_C'] - salarytoassists_df["Current Salary vs. Performance_wA"]
salarytoassists_df["Accuracy Of Pay_wAFG"] = salarytoassists_df['Price Per Minimum Played_C'] - salarytoassists_df["Current Salary vs. Performance_wAFG"]
salarytoassists_df = salarytoassists_df.sort_values('AST?', ascending= False)

salarytorebounds_df = pd.merge(plyr_salary, plyr_rebounds, on= 'Player')
salarytorebounds_df["Current Salary vs. Performance_wR"] = np.round(salarytorebounds_df['Salary 2023-24'] / (salarytorebounds_df['PTS'] * 1.25 + salarytorebounds_df['AST'] * 1.25 + salarytorebounds_df['TRB?'] * 1.5 + salarytoassists_df['G']), 2)
salarytorebounds_df["Current Salary vs. Performance_wRFG"] = np.round(salarytorebounds_df['Salary 2023-24'] / (salarytorebounds_df['PTS'] * 1.5 + salarytorebounds_df['AST'] * 1.2 + salarytorebounds_df['TRB?'] * 1 + salarytoassists_df['G']), 2)
salarytorebounds_df["Accuracy Of Pay_wR"] = salarytorebounds_df['Price Per Minimum Played_C'] - salarytorebounds_df["Current Salary vs. Performance_wR"]
salarytorebounds_df["Accuracy Of Pay_wRFG"] = salarytorebounds_df['Price Per Minimum Played_C'] - salarytorebounds_df["Current Salary vs. Performance_wRFG"]
salarytorebounds_df = salarytorebounds_df.sort_values('TRB?', ascending= False)

salarytopointstop25_df = salarytopoints_df[:26]
salarytoassiststop25_df = salarytoassists_df[:26]
salarytoreboundstop25_df = salarytorebounds_df[:26]

st.set_page_config(
    page_title="Most Valuable Player By The Numbers",
    layout= 'wide'
)

st.write("# Grading Players by Assists Per Game vs. Base Weighting Scale")

st.markdown(
    """
    Another valuable way of determining the value of a player is the assists they can earn in each game and their average
    (Assists Per Game). 
    
    Here we will grade players using all three metrics but give Assists Per Game the highest weight to test it against our base weighted
    scales.

    -----------------------------------------------------------------------------------------------------------------------------------

    The following visualizations are similar to that of the other pages focusing on Points Per Game and Rebounds Per Game.
    
    Our first visualization relies on the fabricated variable of "Price Per Minimum Played_C". This takes the current salary of players and divides
    that salary by the minimum number of games they are required to play (65 games). This then gives us a number that is an average of their value
    for each game hypothetically.

    From this line of thought we then examine player performance based upon the three metrics cited in the introduction, and create two new
    varaibles to stack up against how they are supposed to be played according to their cost to play each game. 
    The first variable, "Current Salary vs. Performance_wA", puts a higher weight on Assists Per Game and follows the following formula:

    Current Season Salary / (Points Per Game * 1.25 + AssistsPerGame * 1.5 + Rebounds Per Game * 1.25 + Games Played

    The second variable, "Current Salary vs. Performance_wAFG", puts a a weight on the three metrics
    according to how they are weighted in default NBA fantasy leagues and follows the following formula:

    Current Season Salary / (Points Per Game * 1.5 + AssistsPerGame * 1.2 + Rebounds Per Game * 1 + Games Played

    The grouped bar chart below shows the visualizations as follows (from right to left): "Price Per Minimum Played_C", "Current Salary vs. Performance_wA", 
    and "Current Salary vs. Performance_wAFG". The data includes the top 25 players filtered by Assists Per Game and the visualizations are sorted from highest
    to lowest going left to right.
"""
)

melted_data_multibar_A = pd.melt(salarytoassiststop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Current Salary vs. Performance_wA', 'Current Salary vs. Performance_wAFG'])


group_barchart_A = alt.Chart(melted_data_multibar_A, title = "Player Expected Value vs. Actual Value - Top Assisters").mark_bar().encode(
    x=alt.X('Player:N', title='Player', sort=alt.EncodingSortField(field='AST?', op='sum', order='descending'), axis=None),
    y=alt.Y('value:Q', title='Values'),
    color=alt.Color('variable:N', title='Metrics'),
    column=alt.Column('variable:N', title=None)
).properties(
    width=150
)

group_barchart_A = group_barchart_A.configure_legend(
    titleLimit=0,  
    labelLimit=0,  
)

st.altair_chart(group_barchart_A, use_container_width=False)

st.markdown(
    """
    From the visualization above, we can see that the current performance of the top assisters in the league does not follow the same flow of
    of the top shooter in the league according to the grouped bar chart. Many of the players on this over and under perform according to their
    contracts and expected performance. Once again, we must look to more avenues of analysis to grasp what correlations are before us.

    -----------------------------------------------------------------------------------------------------------------------------------

    To really get a picture for how accurate the comparision of grading of performance of players against their salaries, we need further
    insight into the data.

    We have created two variables to find out if players are truly overperforming or under performing according to their current season and salary:

    The first variable, "Accuracy Of Pay_wA", takes the current season salary of a player and there current performance cost (weighted by Assists Per Game) and finds the difference
    between the two. That formula is as follows:

    "Price Per Minimum Played_C" - "Current Salary vs. Performance_wA"

    The secound variable, "Accuracy Of Pay_wAFG", does the same as the first variable but the current performance cost is weigthed by the NBA Fantasy 
    weight scales. That formula is as follows:

    "Price Per Minimum Played_C" - "Current Salary vs. Performance_wAFG"

    The following visualization is a line plot of the average cost of a player for each game, and the difference between how they are measuring up
    to that cost with their current season performance.
"""
)

melted_data_multiline_A = pd.melt(salarytoassiststop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Accuracy Of Pay_wA', 'Accuracy Of Pay_wAFG'])

line_chart_A = alt.Chart(melted_data_multiline_A, title= "Accuracy of Current Salary - Top Assiters").mark_line().encode(
    x='Player:N',
    y=alt.Y('value:Q', title='Values'),
    color=alt.Color('variable:N', title='Metrics', scale=alt.Scale(scheme='category10')),
    tooltip=['Player:N', 'value:Q']
).properties(
    width=800,
    height=400
)

line_chart_A = line_chart_A.configure_legend(
    titleLimit=0,  
    labelLimit=0,  
)

st.altair_chart(line_chart_A, use_container_width=False)

st.markdown(
    """
    As we can see from our accuracy line plot, the contracts of the top assisters in the league currently are way more accurate than that of
    the top shooters in the league. Being that because over half of the top assisters in the league are performing with $100,000 over or under 
    of their current contracts.
"""
)