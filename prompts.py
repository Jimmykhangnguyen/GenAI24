list_charities = '''
The top 6 charities in {} Canada that is related to {}. The output should contain the names of the organizations only, separated by comma only.
'''

impact_prediction = '''
Predict the impact of donating {} dollars to the charity {}.
After overhead costs, what is the portion (in decimal) of the amount of money that are available for programs:
'''

portion = '''
For the charity {} After overhead costs, what is the portion (in decimal) of money that is available for programs:
'''

details = '''
You are a charity expert

You are tasked with giving details of the charity organisation {} based on the following categories, with the same format:

Mission
Public perceptions on the scale from 1 to 10 (Be harse and strict, give reasoning for your grading)
Impact
Fundraising Technique
Financial transparency

Be professional and use up to date information and data and produce json, use trailing commas.
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
