"""
Jaiden Atterbury
CSE 163 AD
05/13/23

Implements the functions for Mapping. In particular, these functions provide
and compute statistics for food deserts as well as plotting informative
visualizations for summarizing the food desert datatset. These functions
include: load_in_data, percentage_food_data, plot_map, plot_population_map,
plot_population_county_map, plot_food_access_by_county, and lastly
plot_low_access_tracts.
"""

import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd


def load_in_data(shp_file_name: str, csv_file_name: str) -> gpd.GeoDataFrame:
    """
    Takes in the filename for the census data called shp_file_name, and a
    filename for the food access datatset. Returns a merged GeoDataFrame
    based on the CTIDFP00/CensusTract columns. Keeps all of the US census
    tracts even if they don't have corresponding food accesss data.
    """
    # Turn the files into a GeoDataFrame and/or DataFrame:
    census = gpd.read_file(shp_file_name)
    food = pd.read_csv(csv_file_name)

    # Merge and return the data:
    merged_data = census.merge(food, left_on='CTIDFP00',
                               right_on='CensusTract', how='left')
    return merged_data


def percentage_food_data(state_data: gpd.GeoDataFrame) -> float:
    """
    Takes in the merged census and food GeoDataFrame and returns the
    percentage of census tracts in Washington for which we have food
    access data. The percentage should be a float between 0 and 100
    unrounded.
    """
    # Find the number of unique Census Tracts:
    total = len(state_data['CTIDFP00'].unique())

    # Find the number of unique Census Tracts with food data:
    with_data = len(state_data['CensusTract'].dropna().unique())

    # Find the percentage with food data:
    percentage = 100 * (with_data / total)

    return percentage


def plot_map(state_data: gpd.GeoDataFrame) -> None:
    """
    Takes in the merged census and food GeoDataFrame and plots the shapes of
    all the census tracts in Washington in a file called map.png.
    """
    # Set up figures and axes:
    fig, ax = plt.subplots(1)

    # Plot the data:
    state_data.plot(ax=ax)
    plt.title('Washington State')

    # Save the figure:
    plt.savefig('map.png')


def plot_population_map(state_data: gpd.GeoDataFrame) -> None:
    """
    Takes in the merged census and food GeoDataFrame and plots the shapes of
    all census tracts in Washington where each census tract is colored
    according to population in a file called population_map.png.
    """
    # Set up figures and axes:
    fig, ax = plt.subplots(1)

    # Plot the data:
    state_data.plot(ax=ax, color='#EEEEEE')
    state_data.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington Census Tract Populations')

    # Save the figure:
    plt.savefig('population_map.png')


def plot_population_county_map(state_data: gpd.GeoDataFrame) -> None:
    """
    Takes in the merged census and food GeoDataFrame and plots the shapes of
    all the census tracts in Washington where each county is colored according
    to population in a file called county_population_map.png.
    """
    # Retrieve relevant columns:
    counties = state_data[['POP2010', 'County', 'geometry']]

    # Run the dissolve (groupby) operation:
    grouped_data = counties.dissolve(by='County', aggfunc='sum')

    # Set up figures and axes:
    fig, ax = plt.subplots(1)

    # Plot the data:
    state_data.plot(ax=ax, color='#EEEEEE')
    grouped_data.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington County Populations')

    # Save the figure:
    plt.savefig('county_population_map.png')


def plot_food_access_by_county(state_data: gpd.GeoDataFrame) -> None:
    """
    Takes in the merged census and food GeoDataFrame and produces 4 plots on
    the same figure showing information about food access across income level.
    These 4 levels are lapophalf_ratio, lapop10_ratio, lalowihalf_ratio, and
    lalowi10_ratio.
    """
    # Slice the data to keep only relevant columns:
    state_slice = state_data[['County', 'geometry', 'POP2010', 'lapophalf',
                             'lapop10', 'lalowihalf', 'lalowi10']].copy()

    # Aggregate this data by country by summing:
    group = state_slice.dissolve(by='County', aggfunc='sum')

    for col, new in zip(['lapophalf', 'lalowihalf', 'lapop10', 'lalowi10'],
                        ['lapophalf_ratio', 'lapop10_ratio',
                         'lalowihalf_ratio', 'lalowi10_ratio']):
        group[new] = group[col] / group['POP2010']

    # Plot all of the different figures through the use of a for loop to
    # eliminate redundancy:
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))

    for ax, col, title in zip([ax1, ax2, ax3, ax4],
                              ['lapophalf_ratio', 'lapop10_ratio',
                               'lalowihalf_ratio', 'lalowi10_ratio'],
                              ['Low Access: Half',
                               'Low Access + Low Income: Half',
                               'Low Access: 10',
                               'Low Access + Low Income: 10']):
        state_data.plot(ax=ax, color='#EEEEEE')
        group.plot(ax=ax, column=col, legend=True, vmin=0, vmax=1)
        ax.set_title(title)

    # Save the figure:
    plt.savefig('county_food_access.png')


def plot_low_access_tracts(state_data: gpd.GeoDataFrame) -> None:
    """
    Takes in the merged census and food GeoDataFrame and plots all census
    tracts considered "low access" in a file called low_access.png.
    """
    # Set up the figure and axes:
    fig, ax = plt.subplots(1)

    # Plot the blank state:
    state_data.plot(ax=ax, color='#EEEEEE')

    # Plot the food access data:
    state_data.dropna().plot(ax=ax, color='#AAAAAA')

    # Create the masks for the plotting data through the use of a for loop
    # to reduce redundancy:
    for label, column, new_column in zip(['Urban', 'Rural'],
                                         ['lapophalf', 'lapop10'],
                                         ['low_urban', 'low_rural']):
        is_type = state_data[label] == 1
        is_500 = state_data[column] >= 500
        is_33_perc = (state_data[column] / state_data['POP2010']) >= 1/3
        state_data[new_column] = 0
        state_data.loc[is_type & (is_500 | is_33_perc), new_column] = 1

    # Create a new column to find where low access tracts are:
    state_data['low_access'] = state_data['low_urban'] + \
        state_data['low_rural']

    # Plot all of the low access tracts:
    state_data[state_data['low_access'] == 1].plot(ax=ax)
    plt.title('Low Access Census Tracts')

    # Save the figure
    plt.savefig('low_access.png')


def main():
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
