import vertexai
from vertexai.generative_models import GenerativeModel, Part


def init_api(project_id: str) -> str:
  vertexai.init(project=project_id)

def generate_text(project_id: str, location: str) -> str:
  # Initialize Vertex AI
  vertexai.init(project=project_id, location=location)
  # Load the model
  model = GenerativeModel("gemini-1.0-pro")
  # Query the model
  response = model.generate_content(
    [
      # Add an example image
      Part.from_uri(
          "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
      ),
      # Add an example query
      "what is shown in this image?",
    ]
  )
  print(response)
  return response.text
