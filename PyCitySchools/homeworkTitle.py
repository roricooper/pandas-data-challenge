
# Rori Cooper - Homework Unit 4 Pandas (PyCitySchools)

# Dependencies
import pandas as pd
import numpy as np

# Load resource files
school_resource_data = "Resources/schools_complete.csv"
student_resource_data = "Resources/students_complete.csv"

# Read school_data files and set data frames
school_data = pd.read_csv(school_resource_data)

# >Validate results with head
#school_data.head()

# Read student_data files and set data frames
student_data = pd.read_csv(student_resource_data)

# >Validate results with head
#students.head()

# Merge school_ and student_ data sets
school_data_merged = pd.merge(school_data, student_data, how="left", on=["school_name"])

# >Validate results with head
#school_data_merged.head()

## Part I - District Summary

# Calculate the total number of schools
school_count = school_data_merged["school_name"].nunique()

# >Validate results with print
#print(school_count)

# Calculate the total number of students
student_count = school_data_merged["Student ID"].nunique()

# >Validate results with print
#print(student_count)

# Calculate the total budget
total_budget = school_data["budget"].sum()

# >Validate results with print
#print(total_budget)

# Calculate the average math score
avg_math_score = student_data["math_score"].mean()

# >Validate results with print
#print(avg_math_score)

# Calculate the average reading score
avg_reading_score = student_data["reading_score"].mean()

# >Validate results with print
#print(avg_reading_score)

# Calculate the percentage of students with a passing math score (70 or greater)
students_passing_math = school_data_merged[school_data_merged["math_score"] >= 70].count()["school_name"]
percent_passing_math = (students_passing_math / student_count) * 100

# >Validate results with print
#print(percent_passing_math)

# Calculate the percentage of students with a passing reading score (70 or greater)
students_passing_reading = school_data_merged[school_data_merged["reading_score"] >= 70].count()["school_name"]
percent_passing_reading = (students_passing_reading / student_count) * 100

# >Validate results with print
#print(percent_passing_reading)

# Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
avg_overall_score = (avg_math_score + avg_reading_score)/2

# >Validate results with print
#print(avg_overall_score)

# Set a District Summary dataframe
District_Summary = pd.DataFrame({"Total Schools"               :[school_count], 
                                 "Total Students"              :[student_count],
                                 "Total Budget"                :[total_budget], 
                                 "Average Math Score"          :[avg_math_score],
                                 "Average Reading Score"       :[avg_reading_score], 
                                 "% Passing Math"              :percent_passing_math,
                                 "% Passing Reading"           :percent_passing_reading, 
                                 "Overall Average Score"       :avg_overall_score})
# Set index to show results
District_Summary = District_Summary[["Total Schools", "Total Students", "Total Budget", "Average Math Score",
                                 "Average Reading Score", "% Passing Math", "% Passing Reading", "Overall Average Score"]]

# Display results
District_Summary

## Part I - District Summary - Solution

## Part II - School Summary

# >View dataframe with head
#school_data_merged.head()

# Determine the school type
school_types = school_data.set_index(["school_name"])["type"]

# >Validate results with print
#print(school_types)

# Calculate total students per school
per_school_counts = school_data.set_index(["school_name"])["size"]

# >Validate results with print
#print(per_school_counts)

# Calculate total budget per school
school_budgets = school_data.set_index(["school_name"])["budget"]

# >Validate results with print
#print(school_budgets)

# Calculate per student budget
per_student_budget = school_budgets/ per_school_counts

# >Validate results with print
#print(per_student_budget)

# Average math score per school
avg_math_per_school = school_data_merged.groupby(["school_name"]).mean()["math_score"]

# >Validate results with print
#print(avg_math_per_school)

# Average reading score per school
avg_reading_per_school = school_data_merged.groupby(["school_name"]).mean()["reading_score"]

# >Validate results with print
#print(avg_reading_per_school)

# Count of students passing math
students_passing_math =  school_data_merged[school_data_merged["math_score"] >= 70].groupby("school_name").count()["Student ID"]

# >Validate results with print
#print(students_passing_math)

# Count of students passing reading
students_passing_reading =  school_data_merged[school_data_merged["reading_score"] >= 70].groupby("school_name").count()["Student ID"]

# >Validate results with print
#print(students_passing_reading)

# Percent of students passing math
percent_passing_math = students_passing_math / per_school_counts * 100

# >Validate results with print
#print(percent_passing_math)

# Percent of students passing reading
percent_passing_reading = students_passing_reading / per_school_counts * 100

# >Validate results with print
#print(percent_passing_reading)

# Calculate average overall score per school
avg_overall_score_per_school = (percent_passing_math + percent_passing_reading) / 2

# >Validate results with print
#print(avg_overall_score_per_school)

# Set School Summary dataframe
School_Summary = pd.DataFrame({"School Type"             : school_types, 
                               "Total Students"          : per_school_counts, 
                               "Total School Budget"     : school_budgets, 
                               "Per Student Budget"      : per_student_budget,
                               "Average Math Score"      : avg_math_per_school, 
                               "Average Reading Score"   : avg_reading_per_school,
                               "% Passing Math"          : percent_passing_math, 
                               "% Passing Reading"       : percent_passing_reading,
                               "Overall Passing Rate"    : avg_overall_score_per_school})  

# >Validate results with print
#print(School_Summary)

# Set index to show results
School_Summary = School_Summary[["School Type","Total Students","Total School Budget","Per Student Budget",
                                "Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                 "Overall Passing Rate"]]

# Display results
School_Summary.head(15)

## Part II - School Summary - Solution

## Part III - Top Performing Schools (by Overall Passing Rate)

# Apply sorting to show overall passing rates in descending order
Top_Schools = School_Summary.sort_values("Overall Passing Rate", ascending=False)

# Display results
Top_Schools.head(5)

## Part III - Top Performing Schools - Solution

## Part IV - Bottom Performing Schools (by Overall Passing Rate)

# Apply sorting to show verall passing rates in ascending order
Bottom_Schools = School_Summary.sort_values("Overall Passing Rate")

# Display results
Bottom_Schools.head(5)

## Part IV - Bottom Performing Schools - Solution

## Part V - Math Scores by Grade

# Summarize math scores in table
ninth_grd_score =  school_data_merged[school_data_merged["grade"] == "9th"].groupby("school_name").mean()["math_score"]
tenth_grd_score =  school_data_merged[school_data_merged["grade"] == "10th"].groupby("school_name").mean()["math_score"]
eleventh_grd_score =  school_data_merged[school_data_merged["grade"] == "11th"].groupby("school_name").mean()["math_score"]
twelfth_grd_score =  school_data_merged[school_data_merged["grade"] == "12th"].groupby("school_name").mean()["math_score"]

# Set Math Summary datadframe
Math_Summary = pd.DataFrame({"9th Grade"             : ninth_grd_score, 
                             "10th Grade"            : tenth_grd_score, 
                             "11th Grade"            : eleventh_grd_score,
                             "12th Grade"            : twelfth_grd_score})  

# Set index to show results
Math_Summary = Math_Summary[["9th Grade","10th Grade","11th Grade","12th Grade"]]

# Display results
Math_Summary.head(15)

## Part V - Math Scores by Grade - Solution

## Part VI - Reading Scores by Grade

# Summarize reading scores in table
ninth_grd_score =  school_data_merged[school_data_merged["grade"] == "9th"].groupby("school_name").mean()["reading_score"]
tenth_grd_score =  school_data_merged[school_data_merged["grade"] == "10th"].groupby("school_name").mean()["reading_score"]
eleventh_grd_score =  school_data_merged[school_data_merged["grade"] == "11th"].groupby("school_name").mean()["reading_score"]
twelfth_grd_score =  school_data_merged[school_data_merged["grade"] == "12th"].groupby("school_name").mean()["reading_score"]

# Set Reading Summary datafram
Reading_Summary = pd.DataFrame({"9th Grade"             : ninth_grd_score, 
                                "10th Grade"            : tenth_grd_score, 
                                "11th Grade"            : eleventh_grd_score,
                                "12th Grade"            : twelfth_grd_score})  

# Set index to show results
Reading_Summary = Reading_Summary[["9th Grade","10th Grade","11th Grade","12th Grade"]]

# Display results
Reading_Summary.head(15)

## Part VI - Reading Scores by Grade - Solution

## Part VII - Scores by School Spending

# Set bins and ranges
spend_bins = [0, 585, 615, 645, 675]
spend_ranges = ["<$585","$585-615","$615-645","$645-675"]

# >Validate ranges
#pd.cut(School_Summary["Per Student Budget"], spend_bins, labels=spend_ranges)

# >Validate results with head
#School_Summary.head(100)

# Segment the the School Summary data frame into spend ranges (bins)
School_Summary["Spending Ranges"] = pd.cut(per_student_budget, spend_bins, labels=spend_ranges)

# Calculations for each spend range
spending_math_score = School_Summary.groupby(["Spending Ranges"]).mean()['Average Math Score']
spending_reading_score = School_Summary.groupby(["Spending Ranges"]).mean()['Average Reading Score']
spending_passing_math = School_Summary.groupby(["Spending Ranges"]).mean()['% Passing Math']
spending_passing_reading = School_Summary.groupby(["Spending Ranges"]).mean()['% Passing Reading']
spending_overall_passing_rate = (spending_passing_math + spending_passing_reading) / 2

# >Validate results with head
#School_Summary.head(15)

# Set index to show results
Spending_Summary = School_Summary[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading", "Overall Passing Rate"]]

# Set Spending Summary dataframe
Spending_Summary = pd.DataFrame({"Average Math Score"        :spending_math_score,
                                 "Average Reading Score"     :spending_reading_score,
                                 "% Passing Math"            :spending_passing_math,
                                 "% Passing Reading"         :spending_passing_reading,
                                 "Overall Passing Rate"      :spending_overall_passing_rate}) 


# Display Scores grouped by School Spending
Spending_Summary.groupby("Spending Ranges").head(15)

## Part VII - Scores by School Spending - Solution

## Part VIII - Scores by School Size

# Describe School Summary dataframe to view min and max total students
#School_Summary.describe()

# Set bins and ranges
size_bins = [0, 1000, 2000, 5000]
size_ranges = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# >Validate ranges
#School_Summary["Size Ranges"] = pd.cut(per_school_counts, size_bins, labels=size_ranges)

# >Validate results with head
#School_Summary.head(15)

# Segment the the School Summary data frame into spend ranges (bins)
School_Summary["Size Ranges"] = pd.cut(per_school_counts, size_bins, labels=size_ranges)

# Calculations for each size range
size_math_score = School_Summary.groupby(["Size Ranges"]).mean()['Average Math Score']
size_reading_score = School_Summary.groupby(["Size Ranges"]).mean()['Average Reading Score']
size_passing_math = School_Summary.groupby(["Size Ranges"]).mean()['% Passing Math']
size_passing_reading = School_Summary.groupby(["Size Ranges"]).mean()['% Passing Reading']
size_overall_passing_rate = (size_passing_math + size_passing_reading) / 2

# >Validate results with head
#School_Summary.head(15)

# Set index to show results
Size_Summary = School_Summary[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading", "Overall Passing Rate"]]

# Set Size Summary dataframe
Size_Summary = pd.DataFrame({"Average Math Score"            :size_math_score, 
                             "Average Reading Score"         :size_reading_score,
                             "% Passing Math"                :size_passing_math,
                             "% Passing Reading"             :size_passing_reading,
                             "Overall Passing Rate"          :size_overall_passing_rate}) 

# Display Scores grouped by School Size
#Size_Summary.groupby("Size Ranges").head(15)

# Display Scores grouped by School Size
Size_Summary.groupby("Size Ranges").head(15)

## Part VIII - Scores by School Size - Solution

##IX Summarize by School Type

# Calculations for each school type
type_math_score = School_Summary.groupby(["School Type"]).mean()['Average Math Score']
type_reading_score = School_Summary.groupby(["School Type"]).mean()['Average Reading Score']
type_passing_math = School_Summary.groupby(["School Type"]).mean()['% Passing Math']
type_passing_reading = School_Summary.groupby(["School Type"]).mean()['% Passing Reading']
type_overall_passing_rate = (type_passing_math + type_passing_reading) / 2

# >Validate results with head
#School_Summary.head(15)

# Set index to show results
Type_Summary = School_Summary[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading", "Overall Passing Rate"]]

# Set Type Summary dataframe
Type_Summary = pd.DataFrame({"Average Math Score"            :type_math_score, 
                             "Average Reading Score"         :type_reading_score,
                             "% Passing Math"                :type_passing_math,
                             "% Passing Reading"             :type_passing_reading,
                             "Overall Passing Rate"          :type_overall_passing_rate}) 

# Display Scores grouped by School Type
Type_Summary.groupby("School Type").head(15)

## Part IX - Scores by School Size - Solution

## Part X - Observations - see README in folder