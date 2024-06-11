import streamlit as st
import pandas as pd
import plotly.express as px


#Import vehicles_us.csv
vehicles = pd.read_csv('vehicles_us.csv')

#cleaning of 'vehicles' dataframe

#converting the columns to the correct data types

vehicles['price'] = vehicles['price'].astype('float64')
vehicles['model_year'] = vehicles['model_year'].fillna(0).astype('int64')
vehicles['cylinders'] = vehicles['cylinders'].fillna(0).astype('int64')
vehicles['is_4wd'] = vehicles['is_4wd'].fillna(0).astype('bool')




#header
st.header('Vehicle Prices vs Odometer Reading')

# Filter the data to include only odometer readings less than 500,000
filtered_data = vehicles[vehicles['odometer'] < 500000]

# Create the scatter plot
fig = px.scatter(filtered_data, x='odometer', y='price', 
                 title='Vehicle Prices vs Odometer Reading', 
                 labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})

# Adjust the layout
fig.update_layout(width=800, height=600)

# Show the plot
fig.show()

# Display the plot in Streamlit
st.plotly_chart(fig)

# Add a checkbox to toggle the display of the histogram
show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    # Filter the data to include only odometer readings less than 500,000
    filtered_vehicles = vehicles[vehicles['odometer'] < 500000]

    # Group the filtered data by odometer and calculate the mean price for each group
    grouped = filtered_vehicles.groupby(pd.cut(filtered_vehicles['odometer'], bins=20))['price'].mean().reset_index()

    # Convert Interval objects to string representation
    grouped['odometer'] = grouped['odometer'].apply(lambda x: str(x))

    # Create the histogram
    fig = px.bar(grouped, x='odometer', y='price', labels={'odometer': 'Odometer', 'price': 'Average Price'},
                 title='Histogram of Average Price vs. Odometer (Odometer < 500,000 miles)')

    # Adjust the layout
    fig.update_layout(width=800, height=600)

    # Display the plot in Streamlit
    st.plotly_chart(fig)