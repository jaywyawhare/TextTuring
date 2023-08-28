import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def is_likely_machine_generated(sentence, top_n=3):
    """
    Determines whether a given sentence is likely to be machine-generated or human-generated.

    Parameters:
        sentence (str): The input text sentence to be analyzed.
        top_n (int): The number of top tokens to consider when analyzing the text.

    Returns:
        bool: True if the text is likely machine-generated, False otherwise.
    """
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    input_ids = tokenizer.encode(sentence, return_tensors="pt")
    num_top_matches = 0

    for i in range(len(input_ids[0]) - 1):
        with torch.no_grad():
            outputs = model(input_ids[:, :i+1])
            predictions = outputs.logits

        predicted_prob = torch.nn.functional.softmax(predictions[0, -1], dim=-1)
        top_tokens = torch.argsort(predicted_prob, descending=True)[:top_n]

        if input_ids[0, i+1] in top_tokens:
            num_top_matches += 1

    percent_top_matches = (num_top_matches / (len(input_ids[0]) - 1)) * 100

    return percent_top_matches > 60

st.title("TextTuring App")
user_input = st.text_area("Enter your text here:", value="", height=200)

if st.button("Analyze"):
    if len(user_input) < 50:
        st.write("Please enter a longer text (at least 50 characters).")
    else:
        if is_likely_machine_generated(user_input):
            st.write("This text is likely machine-generated.")
        else:
            st.write("This text is likely human-generated.")
