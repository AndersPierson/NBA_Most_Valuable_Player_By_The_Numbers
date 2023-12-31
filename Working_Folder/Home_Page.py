import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

st.set_page_config(
    page_title="Most Valuable Player By The Numbers",
    layout= 'wide'
)

st.write("# Welcome to By The Numbers: The NBA's Most Valuable Player")

st.sidebar.success("Select a page from this menu!")

st.markdown(
    """
    Each year, the NBA deems one player from a playoff team the "Most Valuable Player"...
    
    ...However, just how valuable are players contracts according to their performance?
    
    In this project, we delve into three metrics (Points Per Game, Assists Per Game, Rebounds Per Game) in order to gain a comparison for what metrics are best for determining contract value.
"""
)

st.image('Working_Folder/JoelEmbiidMVP.jpg')

# st.write("# Grading Players by Points Per Game vs. Base Weighting Scale")

# st.markdown(
#     """
#     One of the most valuable ways of determining the value of a player is the points they can put up in each game and their average
#     (Points Per Game). 
    
#     Here we will grade players using all three metrics but give Points Per Game the highest weight to test it against our base weighted
#     scales.

#     -----------------------------------------------------------------------------------------------------------------------------------

#     Our first visualization relies on the fabricated variable of "Price Per Minimum Played_C". This takes the current salary of players and divides
#     that salary by the minimum number of games they are required to play (65 games). This then gives us a number that is an average of their value
#     for each game hypothetically.

#     From this line of thought we then examine player performance based upon the three metrics cited in the introduction, and create two new
#     varaibles to stack up against how they are supposed to be played according to their cost to play each game. 
#     The first variable, "Current Salary vs. Performance_wP", puts a higher weight on Points Per Game and follows the following formula:

#     Current Season Salary / (Points Per Game * 1.5 + AssistsPerGame * 1.25 + Rebounds Per Game * 1.25 + Games Played

#     The second variable, "Current Salary vs. Performance_wPFG", puts a a weight on the three metrics
#     according to how they are weighted in default NBA fantasy leagues and follows the following formula:

#     Current Season Salary / (Points Per Game * 1.5 + AssistsPerGame * 1.2 + Rebounds Per Game * 1 + Games Played

#     The grouped bar chart below shows the visualizations as follows (from right to left): "Price Per Minimum Played_C", "Current Salary vs. Performance_wP", 
#     and "Current Salary vs. Performance_wPFG". The data includes the top 25 players filtered by Points Per Game and the visualizations are sorted from highest
#     to lowest going left to right.
# """
# )

# melted_data_multibar_P = pd.melt(salarytopointstop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Current Salary vs. Performance_wP', 'Current Salary vs. Performance_wPFG'])


# group_barchart_P = alt.Chart(melted_data_multibar_P, title = "Player Expected Value vs. Actual Value - Top Shooters").mark_bar().encode(
#     x=alt.X('Player:N', title='Player', sort=alt.EncodingSortField(field='PTS', op='sum', order='descending'), axis=None),
#     y=alt.Y('value:Q', title='Values'),
#     color=alt.Color('variable:N', title='Metrics'),
#     column=alt.Column('variable:N', title=None)
# ).properties(
#     width=150
# )

# group_barchart_P = group_barchart_P.configure_legend(
#     titleLimit=0,  
#     labelLimit=0,  
# )

# st.altair_chart(group_barchart_P, use_container_width=False)

# st.markdown(
#     """
#     As we can see from the visualization above, our forumlas on a grand scheme seem to model the expected averages fairly well.
#     The flow of the average cost of each top 25 player almost matches that of what was calculated. These can only be assumed however at a glance, and we must go into further detail.

#     -----------------------------------------------------------------------------------------------------------------------------------

#     To really get a picture for how accurate the comparision of grading of performance of players against their salaries, we need further
#     insight into the data.

#     We have created two variables to find out if players are truly overperforming or under performing according to their current season and salary:

#     The first variable, "Accuracy Of Pay_wP", takes the current season salary of a player and there current performance cost (weighted by Points Per Game) and finds the difference
#     between the two. That formula is as follows:

#     "Price Per Minimum Played_C" - "Current Salary vs. Performance_wP"

#     The secound variable, "Accuracy Of Pay_wPFG", does the same as the first variable but the current performance cost is weigthed by the NBA Fantasy 
#     weight scales. That formula is as follows:

#     "Price Per Minimum Played_C" - "Current Salary vs. Performance_wPFG"

#     The following visualization is a line plot of the average cost of a player for each game, and the difference between how they are measuring up
#     to that cost with their current season performance.
# """
# )

# melted_data_multiline_P = pd.melt(salarytopointstop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Accuracy Of Pay_wP', 'Accuracy Of Pay_wPFG'])

# line_chart_P = alt.Chart(melted_data_multiline_P, title= "Accuracy of Current Salary - Top Shooters").mark_line().encode(
#     x='Player:N',
#     y=alt.Y('value:Q', title='Values'),
#     color=alt.Color('variable:N', title='Metrics', scale=alt.Scale(scheme='category10')),
#     tooltip=['Player:N', 'value:Q']
# ).properties(
#     width=800,
#     height=400
# )

# line_chart_P = line_chart_P.configure_legend(
#     titleLimit=0,  
#     labelLimit=0,  
# )

# st.altair_chart(line_chart_P, use_container_width=False)

# st.markdown(
#     """
#     As we can see from our accuracy visuaization, very few top shooting players overperform on their contracts. In fact most top shooting players
#     in the top 25 are missing their mark of producing the value of their contract. The average difference in performance of contract from the top 
#     25 players by points per game is around $60,000 dollars.
# """
# )
# st.markdown(
#     """
#     -----------------------------------------------------------------------------------------------------------------------------------
#     -----------------------------------------------------------------------------------------------------------------------------------
# """
# )

# st.write("# Grading Players by Assists Per Game vs. Base Weighting Scale")

# st.markdown(
#     """
#     Another valuable way of determining the value of a player is the assists they can earn in each game and their average
#     (Assists Per Game). 
    
#     Here we will grade players using all three metrics but give Assists Per Game the highest weight to test it against our base weighted
#     scales.

#     -----------------------------------------------------------------------------------------------------------------------------------

#     The following visualizations are similar to that of the other pages focusing on Points Per Game and Rebounds Per Game.
    
#     Our first visualization relies on the fabricated variable of "Price Per Minimum Played_C". This takes the current salary of players and divides
#     that salary by the minimum number of games they are required to play (65 games). This then gives us a number that is an average of their value
#     for each game hypothetically.

#     From this line of thought we then examine player performance based upon the three metrics cited in the introduction, and create two new
#     varaibles to stack up against how they are supposed to be played according to their cost to play each game. 
#     The first variable, "Current Salary vs. Performance_wA", puts a higher weight on Assists Per Game and follows the following formula:

#     Current Season Salary / (Points Per Game * 1.25 + AssistsPerGame * 1.5 + Rebounds Per Game * 1.25 + Games Played

#     The second variable, "Current Salary vs. Performance_wAFG", puts a a weight on the three metrics
#     according to how they are weighted in default NBA fantasy leagues and follows the following formula:

#     Current Season Salary / (Points Per Game * 1.5 + AssistsPerGame * 1.2 + Rebounds Per Game * 1 + Games Played

#     The grouped bar chart below shows the visualizations as follows (from right to left): "Price Per Minimum Played_C", "Current Salary vs. Performance_wA", 
#     and "Current Salary vs. Performance_wAFG". The data includes the top 25 players filtered by Assists Per Game and the visualizations are sorted from highest
#     to lowest going left to right.
# """
# )

# melted_data_multibar_A = pd.melt(salarytoassiststop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Current Salary vs. Performance_wA', 'Current Salary vs. Performance_wAFG'])


# group_barchart_A = alt.Chart(melted_data_multibar_A, title = "Player Expected Value vs. Actual Value - Top Assisters").mark_bar().encode(
#     x=alt.X('Player:N', title='Player', sort=alt.EncodingSortField(field='AST?', op='sum', order='descending'), axis=None),
#     y=alt.Y('value:Q', title='Values'),
#     color=alt.Color('variable:N', title='Metrics'),
#     column=alt.Column('variable:N', title=None)
# ).properties(
#     width=150
# )

# group_barchart_A = group_barchart_A.configure_legend(
#     titleLimit=0,  
#     labelLimit=0,  
# )

# st.altair_chart(group_barchart_A, use_container_width=False)

# st.markdown(
#     """
#     From the visualization above, we can see that the current performance of the top assisters in the league does not follow the same flow of
#     of the top shooter in the league according to the grouped bar chart. Many of the players on this over and under perform according to their
#     contracts and expected performance. Once again, we must look to more avenues of analysis to grasp what correlations are before us.

#     -----------------------------------------------------------------------------------------------------------------------------------

#     To really get a picture for how accurate the comparision of grading of performance of players against their salaries, we need further
#     insight into the data.

#     We have created two variables to find out if players are truly overperforming or under performing according to their current season and salary:

#     The first variable, "Accuracy Of Pay_wA", takes the current season salary of a player and there current performance cost (weighted by Assists Per Game) and finds the difference
#     between the two. That formula is as follows:

#     "Price Per Minimum Played_C" - "Current Salary vs. Performance_wA"

#     The secound variable, "Accuracy Of Pay_wAFG", does the same as the first variable but the current performance cost is weigthed by the NBA Fantasy 
#     weight scales. That formula is as follows:

#     "Price Per Minimum Played_C" - "Current Salary vs. Performance_wAFG"

#     The following visualization is a line plot of the average cost of a player for each game, and the difference between how they are measuring up
#     to that cost with their current season performance.
# """
# )

# melted_data_multiline_A = pd.melt(salarytoassiststop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Accuracy Of Pay_wA', 'Accuracy Of Pay_wAFG'])

# line_chart_A = alt.Chart(melted_data_multiline_A, title= "Accuracy of Current Salary - Top Assiters").mark_line().encode(
#     x='Player:N',
#     y=alt.Y('value:Q', title='Values'),
#     color=alt.Color('variable:N', title='Metrics', scale=alt.Scale(scheme='category10')),
#     tooltip=['Player:N', 'value:Q']
# ).properties(
#     width=800,
#     height=400
# )

# line_chart_A = line_chart_A.configure_legend(
#     titleLimit=0,  
#     labelLimit=0,  
# )

# st.altair_chart(line_chart_A, use_container_width=False)

# st.markdown(
#     """
#     As we can see from our accuracy line plot, the contracts of the top assisters in the league currently are way more accurate than that of
#     the top shooters in the league. Being that because over half of the top assisters in the league are performing with $100,000 over or under 
#     of their current contracts.
# """
# )
# st.markdown(
#     """
#     -----------------------------------------------------------------------------------------------------------------------------------
#     -----------------------------------------------------------------------------------------------------------------------------------
# """
# )

# st.write("# Grading Players by Rebounds Per Game vs. Base Weighting Scale")

# st.markdown(
#     """
#     Another valuable way of determining the value of a player is the rebounds they can earn in each game and their average
#     (Rebounds Per Game). 
    
#     Here we will grade players using all three metrics but give Rebounds Per Game the highest weight to test it against our base weighted
#     scales.

#     -----------------------------------------------------------------------------------------------------------------------------------

#     The following visualizations are similar to that of the other pages focusing on Points Per Game and Assists Per Game.
    
#     Our first visualization relies on the fabricated variable of "Price Per Minimum Played_C". This takes the current salary of players and divides
#     that salary by the minimum number of games they are required to play (65 games). This then gives us a number that is an average of their value
#     for each game hypothetically.

#     From this line of thought we then examine player performance based upon the three metrics cited in the introduction, and create two new
#     varaibles to stack up against how they are supposed to be played according to their cost to play each game. 
#     The first variable, "Current Salary vs. Performance_wR", puts a higher weight on Rebounds Per Game and follows the following formula:

#     Current Season Salary / (Points Per Game * 1.25 + AssistsPerGame * 1.25 + Rebounds Per Game * 1.5 + Games Played

#     The second variable, "Current Salary vs. Performance_wRFG", puts a a weight on the three metrics
#     according to how they are weighted in default NBA fantasy leagues and follows the following formula:

#     Current Season Salary / (Points Per Game * 1.5 + AssistsPerGame * 1.2 + Rebounds Per Game * 1 + Games Played

#     The grouped bar chart below shows the visualizations as follows (from right to left): "Price Per Minimum Played_C", "Current Salary vs. Performance_wR", 
#     and "Current Salary vs. Performance_wRFG". The data includes the top 25 players filtered by Rebounds Per Game and the visualizations are sorted from highest
#     to lowest going left to right.
# """
# )

# melted_data_multibar_R = pd.melt(salarytoreboundstop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Current Salary vs. Performance_wR', 'Current Salary vs. Performance_wRFG'])


# group_barchart_R = alt.Chart(melted_data_multibar_R, title = "Player Expected Value vs. Actual Value - Top Rebounders").mark_bar().encode(
#     x=alt.X('Player:N', title='Player', sort=alt.EncodingSortField(field='TRB?', op='sum', order='descending'), axis=None),
#     y=alt.Y('value:Q', title='Values'),
#     color=alt.Color('variable:N', title='Metrics'),
#     column=alt.Column('variable:N', title=None)
# ).properties(
#     width=150
# )

# group_barchart_R = group_barchart_R.configure_legend(
#     titleLimit=0,  
#     labelLimit=0,  
# )

# st.altair_chart(group_barchart_R, use_container_width=False)

# st.markdown(
#     """
#     The visualzation above is uniquely different than that of both the top shooters and top assisters in the league. While the current performance
#     overall follows a trend similar to that of the top shooters, when it comes to the players with big contracts, they are not folowing this trend of
#     where they are largely all over or laregly all under performing. When it comes to the top rebounders in the league some massively overperform, 
#     some massively underperform, and some are right on the money with their expected pace of cost of play. But in order to prove this we must 
#     once again turn to our chart of accuracy!

#     -----------------------------------------------------------------------------------------------------------------------------------

#     To really get a picture for how accurate the comparision of grading of performance of players against their salaries, we need further
#     insight into the data.

#     We have created two variables to find out if players are truly overperforming or under performing according to their current season and salary:

#     The first variable, "Accuracy Of Pay_wR", takes the current season salary of a player and there current performance cost (weighted by Rebounds Per Game) and finds the difference
#     between the two. That formula is as follows:

#     "Price Per Minimum Played_C" - "Current Salary vs. Performance_wR"

#     The secound variable, "Accuracy Of Pay_wRFG", does the same as the first variable but the current performance cost is weigthed by the NBA Fantasy 
#     weight scales. That formula is as follows:

#     "Price Per Minimum Played_C" - "Current Salary vs. Performance_wRFG"

#     The following visualization is a line plot of the average cost of a player for each game, and the difference between how they are measuring up
#     to that cost with their current season performance.
# """
# )

# melted_data_multiline_R = pd.melt(salarytoreboundstop25_df, id_vars=['Player'], value_vars=['Price Per Minimum Played_C', 'Accuracy Of Pay_wR', 'Accuracy Of Pay_wRFG'])

# line_chart_R = alt.Chart(melted_data_multiline_R, title= "Accuracy of Current Salary - Top Rebounders").mark_line().encode(
#     x='Player:N',
#     y=alt.Y('value:Q', title='Values'),
#     color=alt.Color('variable:N', title='Metrics', scale=alt.Scale(scheme='category10')),
#     tooltip=['Player:N', 'value:Q']
# ).properties(
#     width=800,
#     height=400
# )

# line_chart_R = line_chart_R.configure_legend(
#     titleLimit=0,  
#     labelLimit=0,  
# )

# st.altair_chart(line_chart_R, use_container_width=False)

# st.markdown(
#     """
#     As we can see from the visualization above, not only are the contracts of the top rebounders in the league accurate for the most part, there
#     is also a predictable trend developing from the contract accuracy lines. Here we can see the the top rebounders with the highest salaries this
#     are more than likely underperforming in their contracts and will continue to do so!
# """
# )
# st.markdown(
#     """
#     -----------------------------------------------------------------------------------------------------------------------------------
#     -----------------------------------------------------------------------------------------------------------------------------------
# """
# )