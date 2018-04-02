# Hellofresh machine learning engineer tasks
# 2. Apache Spark
#
# Author: Kai Chen
# Date: Apr, 2018
#

# 1. Download the following dataset of Open Recipes from https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json
#
# 2. Write an Apache Spark application in Python that reads the recipes json, extracts every recipe that has “Chilies” as one
# of the ingredients. Please allow for mispelling of the word for example Chiles as well as the singular form of the word.
#
# 3. Add an extra field to each of the extracted recipes with the name difficulty. The difficulty field would have a value of "Hard"
#if the total of prepTime and cookTime is greater than 1 hour, "Medium" if the total is between 30 minutes and 1 hour,
#"Easy" if the total is less than 30 minutes, and "Unknown" otherwise.
#
#4. The resulting dataset should be saved as parquet file.
#5. Your Spark application could run in Stand-alone mode or it could run on YARN.
#
#6. Place your answer in a directory called "recipes-etl" in the root of this repository, with a README.md file that outlines the
# instructions to run your Spark Application.
#

from pyspark.sql import SparkSession
from fastparquet import write

def get_mins(str_time):
    str_time = str_time.upper().replace('PT', '')

    hours = 0
    minutes = 0

    index_hour = str_time.find('H')
    index_minute = str_time.find('M')

    if index_hour > 0 and index_hour < len(str_time):
        hours = int(str_time[0:index_hour])
        if index_minute > 0 and index_minute < len(str_time):
            minutes = int(str_time[index_hour+1:index_minute])
    else:
        if index_minute > 0 and index_minute < len(str_time):
            minutes = int(str_time[0:index_minute])

    minutes += 60*hours
    return minutes

def add_extra_field(data):
    # Add an extra field to each of the extracted recipes with the name difficulty.
    # The difficulty field would have a value of "Hard" if the total of prepTime and cookTime is greater than 1 hour,
    # "Medium" if the total is between 30 minutes and 1 hour,
    # "Easy" if the total is less than 30 minutes, and "Unknown" otherwise.

    total_time_mins = data['prepTime_mins'] + data['cookTime_mins']
    if total_time_mins > 60:
        return 'Hard'
    elif total_time_mins >= 30:
        return 'Medium'
    elif total_time_mins > 0:
        return 'Easy'
    else:
        return 'Unknown'


if __name__ == "__main__":

    session = SparkSession.builder.appName("recipes-etl").getOrCreate()

    dataFrameReader = session.read

    responses = dataFrameReader \
        .option("header", "true") \
        .option("inferSchema", value = True) \
        .json("in/recipes.json")

    print("=== Schema ===")
    print("number of rows {}".format(responses.count()))
    responses.printSchema()
    responses.show()


    # Task
    # Extract every recipe that has “Chilies” as one of the ingredients.
    # Allow for mispelling of the word for example Chiles as well as the singular form of the word.
    print("=== Extract every recipe (chilies) ===")
    df_recipes = responses.filter(responses["ingredients"].contains("Chilies")
                                  | responses["ingredients"].contains("chilies")
                                  | responses["ingredients"].contains("Chiles")
                                  | responses["ingredients"].contains("chiles")
                                  | responses["ingredients"].contains("Chilis")
                                  | responses["ingredients"].contains("chilis")
                                  | responses["ingredients"].contains("Chili")
                                  | responses["ingredients"].contains("chili")
                                  )
    #print("number of rows {}".format(df_recipes.count()))
    df_recipes.show()


    # Task
    # Add an extra field to each of the extracted recipes with the name difficulty.
    # The difficulty field would have a value of "Hard" if the total of prepTime and cookTime is greater than 1 hour,
    # "Medium" if the total is between 30 minutes and 1 hour,
    # "Easy" if the total is less than 30 minutes, and "Unknown" otherwise.
    df_recipes = df_recipes.toPandas()

    df_recipes['cookTime_mins'] = df_recipes['cookTime'].apply(get_mins)
    df_recipes['prepTime_mins'] = df_recipes['prepTime'].apply(get_mins)

    df_recipes['Level'] = df_recipes.apply(add_extra_field, axis=1)

    print("=== Adding extra filed ===")
    print(df_recipes.head())
    print(df_recipes.describe())

    # Task
    # Save the resulting dataset as parquet file
    print("=== Saving resulting dataset as parquet file ===")
    out_parquet_file = 'out/recipes.parquet'
    write(out_parquet_file, df_recipes)
    print("save the resulting dataset to {}".format(out_parquet_file))


    # Task
    # Your Spark application could run in Stand-alone mode or it could run on YARN.




