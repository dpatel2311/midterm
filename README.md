# midterm
# CI Pipeline

This is to test CI pipeline for build and test of an py app with workflow.


### Structure of application
- ".github/workflows/ci-pipeline.yml" CI pipeline  file.
- "app.py" test file.
- "Dockerfile" Dockerfile for building the Docker image.
- "requirement.txt" File listing the dependencies.
- "README.md" This file.
- 
### Prerequisites

- Python 3.x
- Docker

### Instructions on how to build and run your application.

- docker pull dhavalpatel2311/midterm:latest
- docker run -p 5000:5000 dhavalpatel2311/midterm:latest

### Steps to test your CI pipeline.
- to test the pipe line any commits can trigger pipeline, dummy commit on README.md is sufficient.

### test application
- pytest is used to test few usecases stored in file test_app.py file.

