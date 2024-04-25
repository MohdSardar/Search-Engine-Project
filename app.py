import pandas as pd
import streamlit as st

def main():
    st.title("Subtitle Viewer")

    # Load data
    df = pd.read_csv(r"C:\Users\abdul\Desktop\Sardar\Search Engine Project\Search-Engine")
    df['Movies&WebSeries'].fillna('', inplace=True)

    # Search functionality
    search_text = st.text_input("Enter search text:")
    if st.button("Search"):
        if search_text:
            # Filter the DataFrame and display search results
            results = df[df['Movies&WebSeries'].str.contains(search_text, case=False, na=False)]['Subtitles'].tolist()
            if results:
                st.write("Search Results:")
                for result in results:
                    st.write(result)
            else:
                st.write("No results found.")
        else:
            st.write("Please enter a search term.")

if __name__ == "__main__":
    main()
