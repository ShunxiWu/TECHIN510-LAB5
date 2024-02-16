import streamlit as st
import pandas as pd
import altair as alt
import folium
from streamlit_folium import st_folium
from db import conn_str

st.title("Seattle Events")

# Read data from database
df = pd.read_sql_query("SELECT * FROM events", conn_str)

# Chart 1: Most common event categories
chart1 = alt.Chart(df).mark_bar().encode(
    x=alt.X('count():Q', title='Number of Events'),
    y=alt.Y('category:N', title='Event Category', sort='-x')
).properties(
    title='Most Common Event Categories'
).interactive()
st.altair_chart(chart1, use_container_width=True)

# Chart 2: Events by month
df['month'] = pd.to_datetime(df['date']).dt.month_name()
chart2 = alt.Chart(df).mark_bar().encode(
    x=alt.X('count():Q', title='Number of Events'),
    y=alt.Y('month:N', title='Month', sort=alt.EncodingSortField(field='date', op='count', order='ascending'))
).properties(
    title='Events by Month'
).interactive()
st.altair_chart(chart2, use_container_width=True)

# Chart 3: Events by day of the week
df['day_of_week'] = pd.to_datetime(df['date']).dt.day_name()
chart3 = alt.Chart(df).mark_bar().encode(
    x=alt.X('count():Q', title='Number of Events'),
    y=alt.Y('day_of_week:N', title='Day of the Week', sort=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
).properties(
    title='Events by Day of the Week'
).interactive()
st.altair_chart(chart3, use_container_width=True)

# Control 1: Dropdown to filter category
selected_category = st.selectbox("Filter by Category", df['category'].unique())
filtered_df = df[df['category'] == selected_category]

# Control 2: Date range selector for event date
start_date = pd.to_datetime(st.date_input("Start date", df['date'].min()))
end_date = pd.to_datetime(st.date_input("End date", df['date'].max()))
filtered_df['date'] = pd.to_datetime(filtered_df['date'])
# filtered_df = filtered_df[(filtered_df['date'] >= start_date) & (filtered_df['date'] <= end_date)]

# Control 3: Filter by location
selected_location = st.selectbox("Filter by Location", df['location'].unique())
# Drop rows with missing latitude or longitude values
filtered_df = filtered_df.dropna(subset=['latitude', 'longitude'])

# Create a map object
m = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=10)

# Add markers for each venue
for index, row in filtered_df.iterrows():
    if row['latitude'] and row['longitude'] == True:
        folium.Marker([row['latitude'], row['longitude']], popup=row['venue']).add_to(m)

# Display the map
# m

# Display filtered data
st.write(filtered_df)

# Map: Events locations
map_center = [47.6062, -122.3321]
m = folium.Map(location=map_center, zoom_start=11)
for index, row in filtered_df.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['venue']).add_to(m)
st_folium(m)
