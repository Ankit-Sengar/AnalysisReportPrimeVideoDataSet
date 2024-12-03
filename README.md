# AnalysisReportPrimeVideoDataSet
Did this project for performing some handson using Pandas and PowerBI. Repo consist of a dataset I downloaded from Kaggle which contains data for movie and shows hosted on prime.

Steps Used for the PrimeVideoDataAnalysis

1.Analysing and Cleaning Titles Data:
	a.Faced Issues in importing as there is blank lines and new line in CSV File
	--Fixed in Notepad++ by using Regex (Replacing \n\s with nothing)
	b.Create a new file using Pandas by performing the following processing steps:(CleaningAndProcessingData)
	i.Selecting only useful columns from the dataset
	id
	title
	type
	release_year
	runtime
	genres
	imdb_score
	ii.Now Since genres contain data as a list of values we process it by concatenating the values to create a single value that will be used later for data analysis.
	iii.Exported the final dataset to the csv file

2.Imported the data into Power BI:
	a.Removed the rows where data was incomplete like having no genre and IMDB score.
	b.Creating a Date Dimension table based on the min and max year of the data. Though we are not going to use the date dimension table
	just creating it for any future addition of dataset/ general practice.
	
3.Create Visuals to the PowerBI:
	a. Line chart to show the increase trend in the no of shows and movies
	b. Bar chart to show No. of shows and movies of Top 5 Genres.
	c. 2 KPI showing the Highest and Lowest IMDB score achieved by the movies hosted on prime.
	d. Filter to filter the visuals on the basis of year range.

![AnalysisReportPrimeVideoDataSetDashBoard](https://github.com/user-attachments/assets/09d31f5b-b999-4e5b-94b7-04a9b64b7147)

