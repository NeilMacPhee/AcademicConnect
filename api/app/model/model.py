### Code adapted from https://github.com/AssemblyAI-Examples/ml-fastapi-docker-heroku
import pickle
import re
import pandas as pd
import numpy as np
from pathlib import Path
from transformers import TFAutoModel, AutoTokenizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

with open(f"{BASE_DIR}/combined_features.pkl", "rb") as f:
    combined_features = pickle.load(f)

with open(f"{BASE_DIR}/embedding_scaler.pkl", "rb") as f:
    e_scaler = pickle.load(f)

with open(f"{BASE_DIR}/field_scaler.pkl", "rb") as f:
    f_scaler = pickle.load(f)

# with open(f"{BASE_DIR}/prep_student_data.pkl", "rb") as f:
#     prep_student_data = pickle.load(f)


tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = TFAutoModel.from_pretrained('bert-base-uncased')

uni_data_raw = pd.read_excel(f"{BASE_DIR}/university_data.xlsx")


def recommender_pipeline(payload):
    student_data = pd.Series(
        [payload.student_guid, payload.name, payload.research_interests, payload.university_field],
        index=["Student GUID", "Name", "Research Interests", "University Field"]
    )
    # pred = prep_student_data(student_data)

    # Clean up the data in student_data
    student_data['Research Interests'] = student_data["Research Interests"].lower().replace(r'[^\w\s]+', '')
    student_data['University Field'] = encoder.transform([student_data['University Field']])

    # Tokenize and embed the test_student data
    student_input = tokenizer(student_data["Research Interests"], padding=True, truncation=True, max_length=512, return_tensors="tf")
    student_output = model(student_input)
    student_embedding = student_output.last_hidden_state[:, 0, :].numpy()

    # Scale the embedding and the field features
    student_embedding_scaled = e_scaler.transform(student_embedding)
    student_field_scaled = f_scaler.transform([student_data[['University Field']]])

    # Combine embeddings with scaled field
    student_combined_features = np.hstack((student_embedding_scaled, student_field_scaled))

    # Calculate cosine similarity between test_student_combined_features and combined_features
    student_cos_similarities = cosine_similarity(student_combined_features.reshape(1, -1), combined_features)

    # Find the index of the row with the highest cosine similarity
    best_match_index = np.argmax(student_cos_similarities)

    best_match = uni_data_raw.iloc[best_match_index]

    best_match["Similarity Score"] = student_cos_similarities[0, best_match_index]
    return best_match



