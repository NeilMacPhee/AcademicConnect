# AcademicConnect Recommendation System

## Overview
AcademicConnect is a recommendation system designed to connect students and professors based on their research interests and university fields. The system utilizes natural language processing techniques and cosine similarity to suggest potential matches.

## Model Development Components

### 1. Data Preprocessing
- The system reads university data from an Excel file containing information about students and professors, including their research interests and university fields.
- Research interests and university fields are cleaned by converting text to lowercase and removing special characters.

### 2. Embedding with BERT
- The system uses BERT (Bidirectional Encoder Representations from Transformers) for embedding research interests.
- BERT tokenizer and model are employed to tokenize and embed research interests into numerical vectors.

### 3. Similarity Calculation
- Cosine similarity is calculated between the embedded features of each student/professor pair.
- The similarity matrix is generated to represent the similarity scores between all pairs of students/professors.

### 4. Recommendation Functionality
- A function is implemented to retrieve the top matches for a given student or professor based on their similarity scores.
- Top matches are determined by sorting the similarity scores and selecting the highest ones, excluding the individual being examined.

### 5. Data Preparation for API
- Another function is developed to prepare data for API consumption.
- This function preprocesses input data, embeds it using BERT, scales the features, calculates similarity scores, and returns the best match.

### 6. Testing
- The system includes test cases to ensure the correctness of the recommendation and data preparation functionalities.
- Test cases involve comparing the system's recommendations with manually verified results and testing data preparation with synthetic data.

### 7. Serialization
- Various components of the model, including encoder, tokenizer, scaler, and model itself, are serialized using pickle for future use and deployment.

## Usage
1. **Data Preparation**: Ensure that the university data is available in the correct format (Excel file) and has been preprocessed.
2. **Model Training**: Execute the provided code to train the recommendation system.
3. **Testing**: Verify the correctness of the recommendation and data preparation functionalities using test cases.
4. **Serialization**: Serialize the trained model components using pickle for deployment.
5. **API Deployment**: Deploy the recommendation system as an API, utilizing the prepared data function for real-time recommendations.

## Dependencies
- pandas
- tensorflow
- numpy
- scikit-learn
- transformers (for BERT)
- pickle (for serialization)

## API Deployment

Academic Connect uses FastAPI and Docker to deploy an API to utilize the recommendor model. The code for deploying the Dockerfile was adapted from [ml-fastapi-docker-heroku](https://github.com/AssemblyAI-Examples/ml-fastapi-docker-heroku/tree/main) by `ploeber`.

1. ### Create Docker container
`docker build -t academic-connect-app .`

2. ### Run Docker container
`docker run -p 80:80 academic-connect-app`

3. ### Navigate to [`0.0.0.0/docs`](0.0.0.0/docs)
Once on the `/docs` page, naviagte to the green **POST** section and click on the drop down menu. Click on "Try it out", and input an example of a student in the following format.
```json
{
  "student_guid": "a73e3d91-8f7c-4d8a-bb1e-e96f7212f6c2",
  "name": "John Doe",
  "research_interests": "Topology, Calculus, Mathematical Physics, Geometry, Number Theory, Probability, Applied Mathematics, Statistics, Differential Equations",
  "university_field": "Mathematics"
}
```
4. ### Evaluate results
In the reponses section below, evaluate the response from the recommender system. The output should be in the following format.
```json
{
  "student_guid": "c62f086d-6e88-4b4f-ac06-d53d56040929",
  "name": "John Kelly",
  "research_interests": "Topology, Calculus, Mathematical Physics, Geometry, Number Theory, Algebra, Probability, Applied Mathematics, Statistics, Differential Equations",
  "university_field": "Mathematics",
  "similarity_score": 0.9830063257106761
}
```

