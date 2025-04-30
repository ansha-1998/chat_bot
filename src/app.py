import streamlit as st
from chat_bot_llm import open_ai_bot, mistral_bot, gemini_bot

def main():
    st.title("LLM Selection App")
    
    # Initialize chat history in session state if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    st.write("Select an LLM model to use:")
    
    llm_option = st.selectbox(
        "Choose LLM",
        options=["open_ai_bot", "mistral_bot", "gemini_bot"],
        index=0
    )
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        input_prompt = ''
        for element in st.session_state.messages:
            input_prompt += str(element)
            input_prompt += "\n"
            if element["role"] == "user":
                input_prompt += element["content"] + "\n"
        
        # Display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                if llm_option == "open_ai_bot":
                    response = open_ai_bot(input_prompt)
                elif llm_option == "mistral_bot":
                    response = mistral_bot(input_prompt)
                elif llm_option == "gemini_bot":
                    response = gemini_bot(input_prompt)
                
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Add a button to clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main()
