#######################################################################################

# Prediction: Are Movies geting of shorter ??
#######################################################################################


# 1. Loading my friend's data into a dictionary
#######################################################################################
# Create the years and durations lists
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {"years": years, "durations" : durations}

# Print the dictionary
print(movie_dict)



# 2. Creating a DataFrame from a dictionary
#######################################################################################
# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame
print(durations_df)

import matplotlib
gui_env = ['TKAgg']
for gui in gui_env:
    try:
        print("testing", gui)
        matplotlib.use( 'TkAgg')
        from matplotlib import pyplot as plt
        break
    except:
        continue
print("Using:",matplotlib.get_backend())

# 3. A visual inspection of our data
#######################################################################################
# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(durations_df['years'], durations_df['durations'])

# Create a title
plt.title("Netflix Movie Durations 2011-2020")

# Show the plot
plt.show()




# 4. Loading the rest of the data from a CSV
#######################################################################################
# Read in the CSV as a DataFrame
netflix_df =  pd.read_csv('datasets/netflix_data.csv')


# Print the first five rows of the DataFrame
netflix_df.head()



#fig = plt.figure()
#plt.show()



#5. Filtering for movies!
#######################################################################################
# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title','country', 'genre', 'release_year','duration']]

# Print the first five rows of the new DataFrame
netflix_movies_col_subset.head()


#6. Creating a scatter plot
#######################################################################################
# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'])

# Create a title
plt.xlabel('Year')
plt.ylabel('Duration')
plt.title('Movie Duration by Year of Releas')

# Show the plot
plt.show()


#7. Digging deeper
#######################################################################################
# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[ netflix_movies_col_subset['duration'] <60]

# Print the first 20 rows of short_movies
print(short_movies)



#8. Marking non-feature films
#######################################################################################
# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for movie, row in netflix_movies_col_subset.iterrows() :
    if row['genre']  == 'Children':
         colors.append("Red")
    elif  row['genre']  == 'Documentaries':
        colors.append( "blue")
    elif  row['genre']  == 'Stand-Up':
        colors.append("green")
    else:
        colors.append("black")
        
# Inspect the first 10 values in your list        
print(colors[0:10])




#9. Plotting with color!
#######################################################################################
# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
netflix_movies_col_subset
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], c=colors)

# Create a title and axis labels
plt.xlabel('Release Year')
plt.ylabel('Duration (min)')
plt.title('Movie duration by year of release')


# Show the plot
plt.show()


#10. Coclusion
#######################################################################################
# Probably YES


