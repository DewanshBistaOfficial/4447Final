import pandas as pd

# load datasets 
job_postings = pd.read_csv("linkedin_job_postings.csv") # linkedin job postings
ai_threat_data = pd.read_csv("ai_threat_data.csv") # AI threat index

# only keep relevant columns
job_postings = job_postings[['normalized_salary', 'work_type', 'title']]

# rename columns for consistency
ai_threat_data.rename(columns={'Job titiles': 'title', 'AI_Workload_Ratio': 'AI Workload Ratio'}, inplace=True)

# drop missing values
job_postings = job_postings.dropna()
ai_threat_data = ai_threat_data.dropna()

# map job titles
def replace_titles(input):
    for str in ai_threat_data["title"]:
        if str in input:
            return str
    return None

# reformat work type values
def format_work_type(work_type):
    if "FULL" in work_type:
        return "Full Time"
    elif "PART" in work_type:
        return "Part Time"
    else:
        return "Other"


# clean data
job_postings["title_1"] = job_postings["title"].apply(replace_titles)
job_postings = job_postings.dropna()

job_postings["work_type"] = job_postings["work_type"].apply(format_work_type)

# aggregate salary by title and work type
job_postings = job_postings.groupby(['title_1', 'work_type'])['normalized_salary'].mean().reset_index(name='average_normalized_salary')


# merged both dataset
merged_df = pd.merge(job_postings, ai_threat_data, left_on='title_1', right_on='title', how='left')

merged_df = merged_df.rename(columns={'title_1': 'Job Title', 'work_type': 'Work Type', 'average_normalized_salary': 'Average Normalized Salary', 'AI models': 'AI Models'}) # rename columns
merged_df = merged_df.drop(columns=['title'])  # remove duplicate title column

merged_df.to_csv("cleaned_data.csv", index=False)

# print first few rows to verify
print(merged_df.head())
