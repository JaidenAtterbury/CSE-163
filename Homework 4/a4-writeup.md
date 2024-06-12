"""
Jaiden Atterbury
CSE 163 AD
04/22/23

Contains the writeup for a4.py called "Education Data Analysis".
"""

# Education Data Analysis

## 1. Do you think the bar chart for `bar_chart_high_school` is an effective data visualization?

For the most part, the bar chart for `bar_chart_high_school` is an effective data visualization for what
it is trying to show. However, it is important to note that the visualization has flaws as its presentation
may be unnecessary in itself. First off, since humans are great at perceiving differences in length, the use
of a bar chart is good for showing the differences between the three groups. However, since the bars are so similar
in height it can be a little difficult to discern the differences between the different groups. The visualization
also does a good job at effectively answering the question at hand: "what are the differences between the completion
percentages of high school by sex?" However, it is important to note that the question at hand can simply be answered
by comparing two values, and thus a bar chart in which it is decently difficult to see the difference between the 
different groups is probably unnecessary. Some concerns about the visualization that are outside of the scope of the
target question is that the visualization also gives no information on how these percentages break down for categories
such as race. Furthermore, the visualization gives no breakdown of how these percentages have changed over time, thus
leading to no insight on why the percentages are the way they are in this given year. Nor is there any baseline for
comparison to other years.

## 2. How and why did you choose the plot for 'plot_hispanic_min_degree`?

For implementing the plot for `plot_hispanic_min_degree`, I decided to choose a line chart in which the two categories
of educational attainment, `high school` and `bachelor's`, were seperated by `hue`. The reason why I decided to use a
line chart is because we are dealing with time series data. In particular, when working with time series data, the best
way to visualize specific changes over time is through a line chart, as it is easy to see specific trends in the bigger
picture. By using a line chart, it is also easier to see specific occurrences and their accompanying time frame than any
other visualization. Lastly, the reason why I decided to choose `hue` to sperate the two different levels of educational
attainment rather than spliting them up into two seperate plots is because by putting the two lines in the same chart,
it is much easier to see the difference in magnitude percentagewise, than it would be if they were on two seperate plots.
If these two lines were on two seperate plots, in order to compare them you'd have to continuously look back and forth
between the two plots, which could be difficult if the two plots are on different scales.

## 3. Describe a possible bias present in this dataset and why it might have occurred.

One bias that might be present in the dataset comes in the form of the differeing educational attainment rates between races.
What I mean by this is that the reason for differeing rates might not chalk down to the fact that one race simply performs better
than other races. These differences may come down to the fact that certain individuals have better access to educational resources,
have better facilities, etc. than other races do. For example, many predominantly black communities don't get as much school funding
as other richer communities do. Thus, when these schools have lower educational attainment rates among their students, this may not
represent the students' actual attainment rate under ideal circumstances. 

## 4. Describe an application, analysis, or decision motivated by this dataset with the intended goal of improving educational equity but that ultimately exacerbates social injustice.

One decision motivated by this dataset with the intended goal of improving educational equity but in reality could
ultimately exacerbate social injustice is by looking at the increasing attainment rates for certain degrees among
students of a particular race as a whole and deem what is being done now as successful without looking at/taking
into account different geographical regions and how certain races are performing in those regions. By neglecting the
geography and other characteristics like the poverty rates in these certain regions, we fail to recognize that even though
these attainment rates may be increasing as a whole, marginalized communities in poorer negihborhoods might not be experiencing
these same increases. Thus it would be foolish to use a "one size fits all" approach to increasing these attainment rates for
all individuals of a given race. Hence, in order to close the gap of educational attainment across racial lines, more focused
plans need to be developed that suit the needs of each community. This is where the need for more data and more careful data
analysis comes into play.

