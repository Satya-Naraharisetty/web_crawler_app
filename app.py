import streamlit as st
import requests
import json
import io


# Function to call your API for web crawling
def call_crawler_api(root_url, max_depth):
    try:
        # Make a POST request to the Flask API
        response = requests.post(
            "http://127.0.0.1:5000/api/v1/crawl",  # Update this URL if you're hosting elsewhere
            json={
                "root_url": root_url,
                "max_depth": max_depth
            },
            headers={"Content-Type": "application/json"}
        )

        # Check if the response is successful
        if response.status_code == 200:
            return response.json()  # Return the JSON response (crawled links)
        else:
            return {"error": "Failed to fetch data. Please check the URL or depth."}
    except Exception as e:
        return {"error": str(e)}


# Streamlit UI
st.title("Web Crawler App")

# User inputs for URL and depth
root_url = st.text_input("Enter the root URL to crawl", "https://example.com")
max_depth = st.number_input("Enter the crawl depth", min_value=1, max_value=10, value=2)

# State to store if the file has been downloaded
if "file_downloaded" not in st.session_state:
    st.session_state["file_downloaded"] = False

# Button to trigger crawling
if st.button("Crawl"):
    if st.session_state["file_downloaded"]:
        st.warning("You have already downloaded the file for this session.")
    else:
        with st.spinner('Crawling in progress...'):
            # Call the API with user inputs
            result = call_crawler_api(root_url, max_depth)

            # Check if there was an error
            if "error" in result:
                st.error(result["error"])
            else:
                st.success("Crawl successful!")
                # Display the crawled links
                st.json(result)

                # Convert the result to a bytes stream (so we don't use any disk space)
                result_bytes = io.BytesIO()
                result_bytes.write(json.dumps(result, indent=4).encode('utf-8'))
                result_bytes.seek(0)  # Go back to the start of the stream

                # Provide the result as a downloadable JSON file
                st.download_button(
                    label="Download Crawled Data as JSON",
                    data=result_bytes,
                    file_name="crawled_data.json",
                    mime="application/json"
                )

                # Mark the file as downloaded so user cannot download it again in this session
                st.session_state["file_downloaded"] = True
