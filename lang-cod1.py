import streamlit as st
from llama_index import GPTVectorStoreIndex, download_loader

# Load the GoogleDocsReader
GoogleDocsReader = download_loader('GoogleDocsReader')

# Define the GDoc IDs
gdoc_ids = ['1wf-y2pd9C878Oh-FmLH7Q_BQkljdm6TQal-c1pUfrec']

# Initialize the loader and load the documents
loader = GoogleDocsReader()
documents = loader.load_data(document_ids=gdoc_ids)

# Build the index and query engine
index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Define the Streamlit app
def main():
    st.title("Chatbot App")
    st.write("Ask me anything!")

    # Get user input
    user_input = st.text_input("Enter your question")

    if st.button("Ask"):
        # Perform the query
        results = query_engine.query(user_input)

        # Display the top result
        if len(results) > 0:
            answer = results[0]
            st.write("Answer:")
            st.write(answer)
        else:
            st.write("Sorry, I couldn't find an answer.")

# Run the app
if __name__ == "__main__":
    main()

