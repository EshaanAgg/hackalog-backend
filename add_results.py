import pandas as pd
import psycopg2

# Read the excel to get the results
df = pd.read_excel('Results.xlsx')

# Connect to the relevant database
connection = psycopg2.connect(user="EshaanAgg",
                              password="tnl2WZcI0gbC",
                              host="ep-damp-mode-975827.us-east-2.aws.neon.tech",
                              port="5432",
                              database="neondb")
cursor = connection.cursor()

# Updates a single record


def updateSubmission(id, review, score):
    postgres_insert_query = """ UPDATE core_submission SET score = %s, review = %s WHERE id = %s"""
    cursor.execute(postgres_insert_query, (score, review, id))
    connection.commit()


# Loop over all the entries
for ind in df.index:
    id = int(df['id'][ind])
    # If condition to make the queries selectively as per use case
    if id >= 0:
        review = df['Review'][ind]

        # Try block to handle NaN "" value for score
        try:
            score = int(df['Score'][ind])
        except:
            score = 0

        # Update the submission
        try:
            updateSubmission(id, review, score)
            print(f"Record with {id} updated successfully")
        except:
            print(f"Error for {id}!")

# Close the database connection
connection.close()
