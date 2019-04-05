# Guidelines for ETL Project

This document contains guidelines, requirements, and suggestions for Project 1.

## The Project

For the ETL project, you will work in groups to deliver a clean set of data stored in a database (MySQL required. You can put data in Mongo, but it must be in MySQL too).

Imagine that this is an assignment at work: a bunch of data landed on your desk and you and your team are tasked with migrating it to a production database.  Your "final product" here is the refined data stored in the database. Your cleanup of the raw data could be as simple as dropping superfluous columns or as complex as splitting out a single packed CSV into multiple tables.

The data can be extracted from wherever you can find it: this is your chance to practice web scraping, API lookups, or dig deeper into CSV or Excel sheet parsing. As part of this ETL process, you will find that you need to alter the data. For example, you may identify that a CSV or Excel sheet crams multiple values into a single cell (e.g. a film spreadsheet lists genres as a comma separated list of values in a single cell) -- in order to properly clean and store that data, you would need to extract that value into an array and build a list of all unique terms (look at how the Sakila database structures). A common transformation is normalizing dates (don't just store the string: convert the value into legitimate date objects).

There is no class presentation for this! Just finish your code, write up your reports, and submit the links to your repositories.

### Example:

If your group decides that they want to deliver a normalized database of beer styles, breweries, and beers.
You figure that this should use 3 database tables, one dedicated for each type of data.  The beers table would use 
a foreign key to indicate its style and its maker (i.e. the brewery that made it).

Because there is no available API or database that has all this data for you to use (or because you recognize how incredibly valuable these skills are an you want to hone them), you decide to scrape the data available on the following web page:

https://www.beeradvocate.com/beer/styles/

Your transformation of this data is minimal because it looks to be in pretty good shape: you just need to convert the numbers to floats and trim whitespace out of the titles.

After loading the transformed data, you can enjoy your polished database of beers!  

Bonus: imagine you found a secondary set of beer data from another website that included caloric data about each beer (e.g. https://247wallst.com/special-report/2016/08/02/beers-with-the-most-and-least-calories/2/)  How could you pull that data into your existing database?  Merging more than one data source makes you really focus on how to normalize your data so as to avoid duplication.


## Team Effort

Due to the short timeline, teamwork will be crucial to the success of this project! Work closely with your team through all phases of the project to ensure that there are no surprises at the end of the week.  

Working in a group enables you to tackle more difficult problems than you'd be able to working alone. In other words, working in a group allows you to **work smart** and **dream big**. Take advantage of it!  Do your best to divide the work equally and agree up front as to who will do what and importantly, what type of data will be returned.  E.g. if one person is working on the data extraction, what will the end result of that look like? Probably it will be a list of dictionaries (i.e. an array of objects), and that's what needs to be handed off to the person working on the translations.  Plan ahead!  Pro teams will agree on a data structure before hand, often going as far as to create sample fake data that has the structure that will be used.

## Project Proposal

Your proposal should describe the data that you wish to store and indicate the sources you identified (Remember: if you can't find a source, you can't extract and transform it!). Describe which questions such a data set would be able to answer.


## Discussion 

Before you start writing any code, remember that you only have one week to complete this project!

Take advantage of your Instructor and TA support during office hours and class project work time. They are a valuable resource and can help you stay on track.

Discuss the 3 aspects of ETL: ask your group members which of the three is the most difficult and why?  Which is the most time consuming?  Can you divide these 3 tasks evenly amongst your group members?

Discuss the final destination of your data: is a relational database (MySQL) a better target than a non-relational database (Mongo)? Why or why not? Who would be potential "customers" of your final data? Do you need to store the data in Mongo as well as in MySQL? 

## Finding Data

We recommend the following sites to use as sources of data:

* [data.world](https://data.world/)

* [Kaggle](https://www.kaggle.com/)

You can also use APIs or data scraped from the web. However, get approval from your instructor first. Again, there is only a week to complete this!

## Data Cleanup & Analysis

Once you have identified your datasets, perform Extraction, Transformation, and Loading (ETL) on the data. 


Make sure to plan and document the following:

* The sources of data that you will extract from.

* The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).

* The type of final production database to load the data into (relational or non-relational).

* The final tables or collections that will be used in the production database.

You will be required to submit a final technical report with the above information and steps required to reproduce your ETL process.

## Project Report

At the end of the week, your team will submit a Final Report that describes the following:

* **E**xtract: your original data sources and how the data was formatted (CSV, JSON, MySQL, etc).

* **T**ransform: what data cleaning or transformation was required.

* **L**oad: the final database, tables/collections, and why this was chosen.

Please commit and push the report to Github and *each member* must submit a link to BootcampSpot.

## Requirements

Your repository must include:

- A `README.md` file describing the project, its contributors, its data sources, and significant files/folders.  Your summary report can be a part of this `README.md` or it can be linked from there.
- An `extract.py` file whose responsibility is to query remote APIs or databases or gather CSVs.  This file is responsible for getting your data. It would be a good idea to write some functions inside your file that can be called from another script!
- A `transform.py` file whose responsibility is to clean up, segment, normalize, or prune the extracted data.  It would be good for this file to define one or more functions -- they should receive as inputs the output of the extract process.
- A `load.py` file whose responsibility it is to take the transformed data and load it into a database.  The load script should also be responsible for implementing any database schema.
- An `app.py` file that ties the other files together: this is single file you can run that will execute all the ETL components as a single unit.
- A `schema.sql` file that will contains the necessary SQL statements to create your database tables and column definitions.

Your `README.md` must include instructions for how to execute the ETL process so others can easily get the same results as you!

- - -

### Copyright

Coding Boot Camp © 2018. All Rights Reserved.
