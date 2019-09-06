# dyno
An app that allow a user to search a DB of FASTA genomes for a specific DNA sequence, returning: 
- exact matches
- hamming distance 1 matches (including exact matches)
- and edit distance 1 matches (insertion, substition, and deletion as well as exact matches)
To visit the site: https://dyno-lex.herokuapp.com/

## SQL Query Generation
example = "AGCC"
- exactSQL(example)
  - "SELECT * FROM VIRUSES WHERE SEQUENCE LIKE '%AGCC%'"
- hamSQL(example)
  - "SELECT * FROM VIRUSES WHERE SEQUENCE LIKE '%_GCC%' OR SEQUENCE LIKE '%A_CC%' 
  OR SEQUENCE LIKE '%AG_C%' OR SEQUENCE LIKE '%AGC_%'"
- editSQL(example)
  - "SELECT * FROM VIRUSES WHERE SEQUENCE LIKE '%_GCC%' OR SEQUENCE LIKE '%GCC% 
  OR SEQUENCE LIKE '%A_CC%' OR SEQUENCE LIKE '%ACC%' OR SEQUENCE LIKE '%A_GCC%' 
  OR SEQUENCE LIKE '%AG_C%' OR SEQUENCE LIKE '%AGC%' OR SEQUENCE LIKE '%AG_CC%' 
  OR SEQUENCE LIKE '%AGC_%' OR SEQUENCE LIKE '%AGC%' OR SEQUENCE LIKE '%AGC_C%'"
 
## App Design
- app
  - templates
    - home.html
  - app.py
  - config.py
  - data.py
  - etl.py
  - models.py
- .gitignore
- Procfile
- requirements.txt
- runtime.txt
  

## Database Design
- Heroku Postgres DB
  - viruses
    - header: str, primary key
    - sequence: str
    
# Decisions
- Overall Approach
  - To use Python as much as possible I decided to make a Flask app and use Heroku to host it. I wanted to modularize the code as much as possible, separating differing functionalities into their own files. In terms of populating the database, I made add_rows() as only an if statement, so that it would only populate my table if it was empty. For the purposes of this exercise, I ended up with a table that only separated header and sequence, but in the future, I would expand this!
- ETL
  - I wanted to transform the data into a pandas DF because they can be mass added to databases quickly!


# Next Steps
- add unittesting!!!!!
  - I unittested by comparing SQL query results to str.contains in df, but want to add a robust testing system
  - create tests for making sure that data is cleaned correctly 
- create an ETL pipeline for adding new entries into the system
- separate header into different columns in table 
- add JS to clean up HTML
- create a separate stylesheet
