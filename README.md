# TextTuring: Distinguishing Human from Machine

<p align="center">
  <img src="image.jpeg" alt="TextTuring Logo">
</p>

## Overview

TextTuring is an innovative project designed to distinguish human-generated text from machine-generated text. It leverages state-of-the-art natural language processing (NLP) techniques and machine learning models to accomplish this objective. With the ever-increasing generation of AI-generated content, TextTuring offers a powerful solution to identify and verify human-authored text.

## Inspiration

TextTuring's inspiration draws from catching chess cheaters who use AI engines to assist them during games. Cheaters can be caught if they use top engine lines, similar to how TextTuring identifies text that closely resembles AI-generated content.

## Project Features

- **Data Collection**: TextTuring provides a comprehensive dataset that includes a wide range of text samples. This dataset comprises both human-written and AI-generated content, ensuring diversity and accuracy in the model's training and evaluation.

- **Feature Engineering**: The project incorporates advanced feature engineering techniques to analyze and extract meaningful characteristics from text data. These features include n-gram analysis and the computation of weak Language Model (LLM) scores.

- **Threshold Calculation**: TextTuring dynamically calculates threshold values based on the provided data. This enables precise differentiation between human and machine-generated text.

- **Model Evaluation**: The project employs various machine learning techniques to assess text samples against the calculated threshold. This evaluation process results in clear predictions, helping users determine the authenticity of the text.

- **Scalability**: TextTuring is designed with scalability in mind, allowing it to efficiently process vast volumes of text data.

## How to Use

### Installation for Development

1. Clone the repository

    ```bash
    git clone https://github.com/jaywyawhare/TextTuring
    ```

1. Install the required packages

    ```bash
    pip install -r requirements.txt
    ```

1. Generate the dataset

    ```bash
    python3 main.py --generate
    ```

1. Decide the threshold

    ```bash
    python3 main.py --threshold
    ```

1. Go through the juptyer notebook

1. Deploy the web app

    ```bash
    streamlit run app.py
    ```

### For Using the web app

- Go to the [web app](https://turing.streamlit.app/)


## Contributors

- Arinjay Wyawhare - [jaywyawhare](https://github.com/jaywyawhare)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- I extend my gratitude to the open-source NLP and machine learning communities for their invaluable contributions to the field.

_No Need to check my readme as they are written by me because they arent! 😉_ 