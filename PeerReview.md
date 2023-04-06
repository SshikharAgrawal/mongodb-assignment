**Mohan's Review**

```create_collection_if_not_exits()```: This function takes a collection name as input and creates a new collection in the database if it does not already exist. It uses a try-except block to handle the case where the collection already exists. Overall, this function is a simple and useful utility that helps to avoid errors caused by trying to create a collection that already exists.

```import_documets_from_files()```: This function takes a database name, collection name, and file path as input and loads the data from the file into the specified collection in the database using the mongoimport command. This function is a great way to quickly load large amounts of data into a database from JSON files without having to write custom code to parse the files and insert the data.

```insert_record()```: This function takes a collection number as input and inserts a new record into the corresponding collection based on user input. The function prompts the user to enter data for each field in the record and then inserts the record into the collection using the insert_one() method. This function provides a simple way to insert new data into the database without having to write custom code for each collection.

```find_top_n_movies_with_the_highest_IMDB_rating()```: This function finds the top N movies with the highest IMDB rating by using an aggregation pipeline that matches movies with a non-empty IMDB rating, sorts them in descending order of rating, limits the results to the top N, and projects the title and IMDB rating fields. This function is a useful utility for quickly finding the top rated movies in the database.

```find_top_n_movies_with_the_highest_IMDB_rating_in_year()```: This function finds the top N movies with the highest IMDB rating in a given year by using a similar aggregation pipeline to the previous function, but also adds a match stage that filters the movies by the specified year. This function is a great way to find the top rated movies in a particular year.

```find_top_n_movies_with_the_highest_IMDB_rating_and_votes_greater_than_1000()```: This function is designed to find the top N movies based on their IMDB ratings, while also filtering out movies with less than 1000 votes. It works well and provides accurate results. The use of the aggregation pipeline makes it easy to understand and modify if needed.

```find_top_n_movies_with_title_matching_pattern_sorted_by_highest_tomatoes_ratings()```: This function is designed to find the top N movies whose titles match a given pattern, sorted by their highest Tomatoes ratings. It is a useful function for those who are looking for movies that fit a specific theme or genre. The function works well and provides accurate results. The use of the aggregation pipeline with regular expressions makes it easy to customize the search criteria.

```find_top_n_directors_with_maximum_no_of_movies()```: This function is designed to find the top N directors who created the maximum number of movies. It works well and provides accurate results. The use of the aggregation pipeline with the $unwind and $group stages makes it easy to understand and modify if needed. Overall, this function is a useful tool for those who want to know more about the most prolific directors in the film industry.

```find_top_n_directors_who_created_maximum_no_of_movies_in_an_year(year)```:
This function takes a year as input and finds the top N directors who created the maximum number of movies in that year. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N. Overall, this function seems to be well-implemented and should work as expected.

```find_top_n_directors_who_created_maximum_no_of_movies_in_given_genre(genre)```:
This function takes a genre as input and finds the top N directors who created the maximum number of movies in that genre. It also uses MongoDB's aggregation pipeline to perform the required queries. Similar to the previous function, the user is prompted to enter the value of N. This function seems to be a good implementation and should work as expected.

```find_top_n_actors_with_maximum_no_of_movies()```:
This function finds the top N actors who starred in the maximum number of movies. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N. This function is well-implemented and should work as expected.

```find_top_n_actors_with_maximum_no_of_movies_in_given_year(year)```:
This function takes a year as input and finds the top N actors who starred in the maximum number of movies in that year. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N. This function also seems to be well-implemented and should work as expected.

```find_top_n_actors_with_maximum_no_of_movies_in_give_genre(genre)```:
This function takes a genre as input and finds the top N actors who starred in the maximum number of movies in that genre. It also uses MongoDB's aggregation pipeline to perform the required queries. The user is prompted to enter the value of N. This function is also well-implemented and should work as expected.

```top_n_movies_for__every_genre()```:
This function finds the top N movies for each genre with the highest IMDB rating. It uses MongoDB's aggregation pipeline to perform the required queries. The function prompts the user to enter the value of N for each genre. This function seems to be well-implemented and should work as expected.

```top10_users_with_max_number_of_comments()```:
This function finds the top 10 users who made the maximum number of comments. It uses MongoDB's aggregation pipeline to perform the required queries. The function returns the results in the form of an iterator. This function is well-implemented and should work as expected.

```top10_movies_With_most_comment()```:
This function finds the top 10 movies with the most comments. It uses MongoDB's aggregation pipeline to perform the required queries. The function returns the results by printing the title and number of comments for each movie. This function seems to be well-implemented and should work as expected.
