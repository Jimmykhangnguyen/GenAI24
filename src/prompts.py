list_charities = '''
Get the top 3 charities (no duplicates) in {} Canada that is related to {}. For each of the charity, get:

Charity name,
Mission,
PublicPerception (1-10),
Impact,
FundraisingTechnique,
FinancialTransparency.

The output should be in json.

Be professional and use up to date information
'''

impact_prediction = '''
Predict the impact of donating {} dollars to the charity {}.
After overhead costs, what is the portion (in decimal) of the amount of money that are available for programs:
'''

portion = '''
For the charity {} After overhead costs, what is the portion (in decimal) of money that is available for programs:
'''

details = '''
Give the details of the charity organisation {} including the following information:

Mission
Public perceptions on the scale from 1 to 10 (Be harse and strict)
Impact
Fundraising Technique
Financial transparency on the scale from 1 to 10

Be professional and use up to date information and data and produce json where the top-level keys are

Mission
PublicPerception
Impact
FundraisingTechnique
FinalcialTransparency
'''

amount_extraction = '''
Extract the portion (in decimal) and amount of money (without grouping separator)
available after overhead cost. The output should be separated by comma and have no units. 

text: {}
'''
spending_breakdown = '''
Provide a breakdown of the spending of the charity {}.

There should be less than or equal to 5 categories, one of which must be Program Expenses. The output should be in json, the numbers should be in decimal and add up to 1.0.
'''
