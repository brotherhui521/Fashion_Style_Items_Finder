"""
Configuration settings for the Style Finder application.
"""

# Model and API configuration
LLAMA_MODEL_ID = "meta-llama/llama-3-2-90b-vision-instruct"
PROJECT_ID = "ae9c72f8-4367-44b7-a2b4-5c32dce37573"  # Default project ID for lab environment. Now it is the sandbox project id
REGION = "us-south"
api_key="DAy3S0TUlnhb7hOn_0kVtC3QzjbFEEg8UR9la7z6Qfi5"

# Image processing settings
IMAGE_SIZE = (224, 224)
NORMALIZATION_MEAN = [0.485, 0.456, 0.406]
NORMALIZATION_STD = [0.229, 0.224, 0.225]

# Default similarity threshold
SIMILARITY_THRESHOLD = 0.8

# Number of alternatives to return from search
DEFAULT_ALTERNATIVES_COUNT = 5
