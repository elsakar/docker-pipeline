# Container Pipeline

A modern container pipeline with GitLab CI/CD for building, scanning, and deploying Docker images with security checks.

## Features

- **Environment-based deployments** (dev, staging, production)
- **Vulnerability scanning** with Trivy
- **Manual pipeline triggering** with environment selection
- **Security gates** to prevent deployment of vulnerable images
- **Multi-stage Docker builds** for optimized images
- **Basic Flask application** as an example

## Prerequisites

- Docker
- GitLab account with Container Registry access
- GitLab Runner with Docker executor

## Project Structure

```
.
├── .gitlab-ci.yml    # CI/CD pipeline configuration
├── Dockerfile         # Multi-stage Docker configuration
├── README.md          # This file
├── app/               # Application code
│   └── __init__.py   # Flask application
├── requirements.txt   # Python dependencies
└── tests/             # Test files
    └── test_app.py   # Unit tests
```

## How to Use

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd container-pipeline
   ```

2. **Build the Docker image locally**
   ```bash
   docker build -t myapp:latest --build-arg ENV=dev .
   ```

3. **Run the application locally**
   ```bash
   docker run -p 5000:5000 myapp:latest
   ```
   Then visit `http://localhost:5000` in your browser.

4. **Run tests**
   ```bash
   python -m pytest tests/
   ```

## GitLab CI/CD Pipeline

The pipeline consists of the following stages:

1. **validate**: Checks if an environment was selected
2. **build**: Builds the Docker image
3. **scan**: Scans the image for vulnerabilities
4. **deploy**: Deploys the image to the selected environment

### Triggering the Pipeline

1. Go to CI/CD > Pipelines in your GitLab project
2. Click "Run pipeline"
3. Select your branch
4. Add a variable:
   - Key: `ENVIRONMENT`
   - Value: `dev`, `staging`, or `production`
5. Click "Run pipeline"

### Environment Variables

- `ENVIRONMENT`: Required. The target environment (dev/staging/production)
- `CI_REGISTRY_IMAGE`: Automatically set by GitLab
- `CI_COMMIT_SHORT_SHA`: Automatically set by GitLab

## Security

- Images are scanned for critical vulnerabilities before deployment
- Deployment is blocked if critical vulnerabilities are found
- Sensitive data should be stored in GitLab CI/CD variables

## License

MIT
