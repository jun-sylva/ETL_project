# ETL_project

## extract:
***
**Extract** dataset on GitHub: [movies](https://raw.githubusercontent.com/jun-sylva/data/main/movies.csv)

## transform:
***
**Cleaning Data** delete empty columns, nan columns and columns with incorrect values

**Data modeling** transform data (transform column 'genres' ({'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'})
    to ['Animation', 'Comedy']) ), convert column to the correct type

## Load:
***
**Export** cleaning dataset with condition: create Excel file abd load dateset on sheet
(sheet only for comedy film, for action film, for film with popularity > 75,
with release date year > 2000 and sort DSC, ...)

## Bash
***
Create bash file for install python and libraries to windows or linux and launch 
script if you want to execute script without editor

