import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import os

matplotlib.use('Agg')

def save_graph(path, df, x_name="", y_name=""):
	# Step 2: Set the plot style
	# sns.set_theme(style="darkgrid")

	# Step 3: Create the bar plot
	plt.figure(figsize=(10, 6))
	sns.barplot(x=x_name, y=y_name, data=df)

	# Step 4: Customize the plot
	plt.title('Revenue by Fiscal Quarter')
	plt.xlabel(x_name)
	plt.ylabel(y_name)
	plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

	# Step 4: Save the plot as a PNG file
	os.makedirs(os.path.dirname(path), exist_ok=True) 
	plt.savefig(path, dpi=300, bbox_inches='tight')  # Save with high resolution

	
xl = pd.ExcelFile('output/Companies Reports.xlsx')

symbols = xl.sheet_names  # see all sheet names

x_name = 'Fiscal Quarter'
metrics = ['Revenue', 'Operating Income', 'Operating Margin', 'Free Cash Flow']
for company in symbols:
	df = xl.parse(company)  # read a specific sheet to DataFrame
	columns = df.columns

	# df = df.set_index(x_name).T
	df = df.set_index(x_name).T
	df = df.reset_index()

	# Step 4: Rename columns
	df.columns.name = None  # Remove the name of the columns
	df.columns = [x_name] + list(df.columns[1:])  # Set new column names
	
	for metric in metrics:
		save_graph(f"graphs/{metric}/{company}_{metric}.png", df, x_name, metric)

	

