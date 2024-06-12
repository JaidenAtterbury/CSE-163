"""
Jaiden Atterbury
CSE 163 AD
04/22/23

Implements the functions for Education. In particular, these functions provide
and compute descriptive statistics as well as plotting informative
visualizations for summarizing the National Center for Education Statistics
dataset that covers perecntages of educational attainment for certian types of
people aged 25-29 years old in the years 1920-2018. These functions include:
compare_bachelors_1980, top_2_2000s, line_plot_bachelors,
bar_chart_high_school, plot_hispanic_min_degree, and fit_and_predict_degrees.
"""

# Your imports here:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Load seaborn's default theme and color palette to the session:
sns.set()


# Define your functions here:
def compare_bachelors_1980(df: pd.DataFrame) -> pd.DataFrame:
    """
    Takes in a DataFrame representing the nces dataset and computes the
    percentages of men and women who achieved a minimum degree of a
    Bachelors degree in 1980. Returns a 2-by-2 DataFrame with rows
    corresponding to Males and Females and columns corresponding to
    Sex and Total.
    """
    # Filter the data:
    is_1980 = df['Year'] == 1980
    is_bachelors = df['Min degree'] == "bachelor's"
    is_m_or_f = df['Sex'] != 'A'
    filtered_df = df[is_1980 & is_bachelors & is_m_or_f]

    # Select the columns:
    selected_df = filtered_df[['Sex', 'Total']]

    return selected_df


def top_2_2000s(df: pd.DataFrame, sex: str = 'A') -> pd.Series:
    """
    Takes in a DataFrame representing the nces dataset and a string called sex
    with default value 'A' and computes the two most commonly earned degrees
    for that given sex between the years 2000 and 2010 (inclusive). Returns a
    2 element Series with the index being the Min Degree and the values being
    the mean of the Total educational attainement of the given Min degree.
    """
    # Filter the data:
    is_2000 = df['Year'] >= 2000
    is_2010 = df['Year'] <= 2010
    is_sex = df['Sex'] == sex
    filtered_df = df[is_2000 & is_2010 & is_sex]

    # Get the top 2 degree types:
    degree_series = filtered_df.groupby('Min degree')['Total'].mean()
    top_2_largest = degree_series.nlargest(n=2)

    return top_2_largest


def line_plot_bachelors(df: pd.DataFrame) -> None:
    """
    Takes in a DataFrame representing the nces dataset and plots a line chart
    of the total percentages of all people of Sex 'A' with a Min Degree of
    bachelor's over time.
    """
    # Filter the data:
    is_sex = df['Sex'] == 'A'
    is_bachelors = df['Min degree'] == "bachelor's"
    filtered_df = df[is_sex & is_bachelors]

    # Plot the data:
    sns.relplot(data=filtered_df, x="Year", y="Total", kind="line")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("Percentage Earning Bachelor's over Time")
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(df: pd.DataFrame) -> None:
    """
    Takes in a DataFrame representing the nces dataset and plots a bar chart
    comparing the total percentages of all people of Sex F, M, and A with a
    Min degree of high school in the Year 2009.
    """
    # Filter the data:
    is_year = df["Year"] == 2009
    is_highschool = df['Min degree'] == 'high school'
    filtered_df = df[is_year & is_highschool]

    # Plot the data:
    sns.catplot(data=filtered_df, x="Sex", y="Total", kind="bar")
    plt.xlabel("Sex")
    plt.ylabel("Percentage")
    plt.title("Percentage Completed High School by Sex")
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(df: pd.DataFrame) -> None:
    """
    Takes in a DataFrame representing the nces dataset and plots how the
    percentages of all Hispanic students with degress have changed between
    1990-2010 (inclusive) for students with Min degree of high school and
    bachelor's.
    """
    # Filter the data:
    is_year = (df['Year'] >= 1990) & (df['Year'] <= 2010)
    is_sex = df['Sex'] == 'A'
    is_highschool = df['Min degree'] == 'high school'
    is_bachelors = df['Min degree'] == "bachelor's"
    filtered_df = df[is_sex & is_year & (is_highschool | is_bachelors)]

    # Plot the data:
    sns.relplot(data=filtered_df, x="Year", y="Hispanic", hue="Min degree",
                style="Min degree", kind="line")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("Percentage of Hispanic Students Earning Degrees (1990-2010)")
    plt.xticks(rotation=-45)
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(df: pd.DataFrame) -> float:
    """
    Takes in a DataFrame representing the nces dataset and trains/tests a
    DecisionTreeRegressor to predict the percentage of degrees attained for
    a given Sex, Min degree, and Year. Returns the test mean squared error of
    this model as a float.
    """
    # Get the required columns and drop rows with NaN values:
    filtered_df = df[['Year', 'Min degree', 'Sex', 'Total']]
    removed_df = filtered_df.dropna()

    # Get the features and labels after the one-hot encoding:
    X_categorical = removed_df.loc[:, removed_df.columns != 'Total']
    X = pd.get_dummies(X_categorical)
    Y = removed_df['Total']

    # Randomly split the data into test and training sets:
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # Create and fit the model to the training set:
    model = DecisionTreeRegressor()
    model.fit(X_train, Y_train)

    # Calculate the MSE of the model's test set predicitons:
    test_predictions = model.predict(X_test)
    test_mse = mean_squared_error(Y_test, test_predictions)

    return test_mse


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    compare_bachelors_1980(data)
    top_2_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
