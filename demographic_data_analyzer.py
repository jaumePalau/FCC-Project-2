import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    count_race = df['race'].value_counts()
    race_count = pd.Series(count_race.values, index=count_race.index)
    # What is the average age of men?
    man = df[df['sex'] == 'Male']
    average_age_men = man['age'].mean()
    # What is the percentage of people who have a Bachelor's degree?
    bach = len(df['education'][df['education'] == 'Bachelors'])
    total = len(df['education'])
    percentage_bachelors = (bach/total)*100
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['education'][df['education'].isin(['Bachelors', 'Masters','Doctorate'])]
    lower_education =   df['education'][~df['education'].isin(['Bachelors', 'Masters','Doctorate'])]
    # percentage with salary >50K
    higher_education_rich = (len(df['education'][(df['education'].isin(['Bachelors', 'Masters','Doctorate']) & (df['salary'] == '>50K'))])/len(higher_education)) * 100
    lower_education_rich =  (len(df['education'][(~df['education'].isin(['Bachelors', 'Masters','Doctorate']) & (df['salary'] == '>50K'))])/len(lower_education)) * 100
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df[df['hours-per-week'] == min_work_hours])
    print(num_min_workers)
    rich_percentage = (len(num_min_workers[num_min_workers['salary'] == '>50K'])/len(num_min_workers)) * 100
    # What country has the highest percentage of people that earn >50K?
    count_country = df.groupby('native-country').size()
    count_country_rich = df[df['salary'] == '>50K'].groupby('native-country').size()
    country_percentage = (count_country_rich / count_country) * 100
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = country_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df['occupation'][(df['native-country'] == 'India') & (df['salary'] == '>50K')].value_counts().idxmax()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", round(average_age_men,1))
        print(f"Percentage with Bachelors degrees: { round(percentage_bachelors, 1)}%")
        print(f"Percentage with higher education that earn >50K: { round(higher_education_rich,1)}%")
        print(f"Percentage without higher education that earn >50K: {round(higher_education_rich,1)}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {round(rich_percentage,1)}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {round(highest_earning_country_percentage,1)}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men,1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich,1),
        'lower_education_rich': round(lower_education_rich,1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage,1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        round(highest_earning_country_percentage,1),
        'top_IN_occupation': top_IN_occupation
    }
data = calculate_demographic_data(print_data = True)
