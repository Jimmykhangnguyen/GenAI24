list_charities = '''
The top 6 charities in {} Canada that is related to {}. The output should contain the names of the organizations only, separated by newline.
'''

impact_prediction = '''
Predict the impact of donating {} dollars to the charity {}.
After overhead costs, what is the portion (in decimal) of the amount of money that are available for programs:
Amount of people impacted in 2017: 
Amount of people impacted in 2018: 
Amount of people impacted in 2019: 
Amount of people impacted in 2020: 
Amount of people impacted in 2021: 
'''

amount_extraction = '''
Extract the portion (in decimal) and amount of money (without grouping separator)
available after overhead cost. The output should be separated by comma and have no units. 

text: {}
'''
spending_breakdown = '''
Provide a breakdown of the spending of the charity {} in the format of 
Category: portion in decimal

There should be less than or equal to 5 categories. The output should be a plain string.
'''
