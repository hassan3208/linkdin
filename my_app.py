import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import get_jobs

# Streamlit title
st.title("Welcome to Job Finder")

# Job input
job = st.text_input("Enter Job title to search", "Type Here ...")

if st.button('Submit'):
    result = job.title()
    st.success(f"Searching for: {result}")

    # Fetch job data
    df = get_jobs.get_job_list(job)

    # Convert dataframe to CSV for download
    csv = df.to_csv(index=False)

    # Download button for CSV
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='jobs.csv',
        mime='text/csv'
    )

    # Get the count of jobs by corporation
    job_count = df['COORPORATION'].value_counts()

    # Bar Chart
    fig, ax = plt.subplots(figsize=(12, 8))  # Increased figure size
    ax.bar(job_count.index, job_count.values, color='skyblue')
    ax.set_xlabel('Corporation')
    ax.set_ylabel('Number of Jobs')
    ax.set_title('Number of Job Listings per Corporation')
    ax.tick_params(axis='x', rotation=90)  # Rotate x labels if needed for better readability
    st.pyplot(fig)
    
    # Pie Chart
    fig_pie, ax_pie = plt.subplots(figsize=(12, 8))  # Increased figure size
    ax_pie.pie(job_count.values, labels=job_count.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    ax_pie.set_title('Distribution of Job Listings by Corporation')
    st.pyplot(fig_pie)


    # Print the counts if needed (can be removed)
    print(job_count.tolist())

