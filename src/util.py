import json

import numpy as np
import prompts
import configs

import matplotlib.pyplot as plt
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


def graphing(
    charities: dict,
    dir: str = 'images/'
) -> list:
  lst = []
  for agency in charities:
    # Access spending data from the JSON
    data = charities[agency]["spending"]

    # Calculate total spending
    total_spending = sum(data.values())

    # Calculate spending percentages
    spending_percentages = {category: (
      value / total_spending) * 100 for category, value in data.items()}

    # Prepare pie chart data
    pie_chart_data = list(spending_percentages.values())
    pie_chart_labels = list(spending_percentages.keys())

    # Create pie chart
    plt.figure(figsize=(3, 3))
    plt.pie(pie_chart_data, labels=pie_chart_labels, autopct="%1.1f%%")
    plt.title(agency + " Spending Percentages")
    with open(dir + agency.replace(' ', '_') + '.png', 'wb') as f:
      plt.savefig(f)
    lst.append(dir + agency.replace(' ', '_') + '.png')

    agencies = list(charities.keys())
    transparency = np.array([])
    perception = np.array([])
    for i in charities:
      transparency = np.append(
        transparency, charities[i]["detail"]["FinancialTransparency"])
      perception = np.append(
        perception, charities[i]["detail"]["PublicPerception"])

  weight_counts = {
      "Transparency": transparency,
      "Perception": perception
  }
  width = 0.5

  fig, ax = plt.subplots()
  bottom = np.zeros(3)

  for boolean, weight_count in weight_counts.items():
    p = ax.bar(agencies, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

  ax.set_title("Rating of each charity")
  ax.legend(loc="upper right")

  with open('images/' + 'ratings.png', 'wb') as f:
    fig.savefig(f)
  lst.append('images/' + 'ratings.png')

  return lst

if __name__ == '__main__':
  import pprint

  pprint.pprint(get_charities())
