# AcademicConnect
A recommendation system tailored for an academic environment to match professors and students with shared interests.

### Building Docker Image

Build Docker image
`docker build -t academic-connect-app .`

Run Docker image on 0.0.0.0
`docker run -p 80:80 academic-connect-app`

### Testing the API

{
  "student_guid": "a73e3d91-8f7c-4d8a-bb1e-e96f7212f6c2",
  "name": "John Doe",
  "research_interests": "Topology, Calculus, Mathematical Physics, Geometry, Number Theory, Probability, Applied Mathematics, Statistics, Differential Equations",
  "university_field": "Mathematics"
}