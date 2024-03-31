import json
import prompts
import configs
import vertexai
from vertexai.generative_models import GenerativeModel

# Initialize Vertex AI
vertexai.init(
  project='with-comment-418817',
  location='us-central1'
)
# Load the model
model = GenerativeModel("gemini-1.0-pro")


def generate_text(model, prompt, config=None) -> str:
  # Query the model
  response = model.generate_content(prompt, generation_config=config)
  return response


def parse_to_list(s: str) -> dict:
  s = s.replace('\n', '').replace('\\', '')
  i = s.index('[')
  j = s.index(']')
  s = s[i:j + 1]
  try:
    return json.loads(s)
  except Exception as e:
    print(s)
    raise e


def parse_to_dict(s: str) -> dict:
  s = s.replace('\n', '').replace('\\', '')
  i = s.index('{')
  j = s.index('}')
  s = s[i:j + 1]
  try:
    return json.loads(s)
  except Exception as e:
    print(s)
    raise e

def get_charities(
    location: str = 'Alberta',
    category: str = 'Environment'
) -> dict[str, dict]:


  charities = generate_text(
    model,
    prompts.list_charities.format(location, category),
    configs.deterministic
  ).text

  charities = parse_to_list(charities)


  output = dict()
  for charity in charities:
    name = next(iter(charity.values()))
    detail = dict(list(charity.items())[1:])
    spending_breakdown = generate_text(
      model,
      prompts.spending_breakdown.format(charity),
      configs.deterministic
    ).text

    spending_breakdown = parse_to_dict(spending_breakdown)

    output[name] = {'detail': detail, 'spending': spending_breakdown}

  return output


if __name__ == '__main__':
  import pprint

  pprint.pprint(get_charities())
