# Automated MCQ Generation Project

## Overview

The project aims to automate the generation of multiple-choice questions (MCQs) with efficient distractors from textual content. Leveraging natural language processing (NLP) techniques, our goal is to develop a pipeline that can parse articles and automatically generate sets of MCQs. This automation process enhances educational platforms and information retrieval systems.

## Problem Statement

Manual creation of MCQs is a time-consuming and labor-intensive task. Automating the question generation process from text can significantly reduce this workload. It not only enables the rapid creation of assessment materials but also aids in comprehension evaluation, facilitating interactive learning experiences. The project addresses the pressing need for efficient systems capable of extracting key information from text and formulating contextually relevant questions.

## Pipeline Overview

The project involves a four-step pipeline to achieve automated question generation:

1. **Extractive Text Summarization:**
   - Summarize the given text to extract key information.

2. **Keyword Extraction:**
   - Identify and extract important keywords from the summarized content.

3. **Distractor Generation:**
   - Generate efficient distractors for the MCQs based on the extracted keywords.

4. **Question Generation:**
   - Formulate multiple-choice questions using the summarized content, extracted keywords, and generated distractors.

## Input

The input to the system is a text article.

## How to Use

To utilize the automated MCQ generation system, follow these steps:

1. Input a text article into the system.
2. Run the provided scripts to initiate the automated pipeline.
3. Retrieve the generated MCQs with distractors.

Feel free to explore and contribute to the development of this educational enhancement tool.

## Dependencies

Ensure you have the required dependencies installed before running the system:

- [NLP Library]
- [Summarization Tool]
- [Keyword Extraction Library]

