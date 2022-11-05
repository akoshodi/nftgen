import csv
import json
import os
import hashlib
import pandas as pd

def make_record(row):
	attributes_dic = dict((a.strip(), (b.strip()))
		for a, b in (element.split(': ')
			for element in row["Attributes"].split('; ')))
	attribute_list = []
	for key, value in attributes_dic.items():
					attribute_list.append({
						"trait_type": key,
						"value": value
					})    
	
	return {
				"format": "CHIP-0007",
				"name": row["Name"],
				"description": row["Description"],
				"minting_tool": row["TEAM NAMES"], 
				"sensitive_content": False,               
				"series_number": row["Series Number"],
				"series_total": 420,
				"gender": row["Gender"],
				"uuid": row["UUID"],
				"attributes": [                    
					attribute_list
				],
				"collection": {
					"name": "Zuri NFT Tickets for Free Lunch",
					"id": "e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57",
					"attributes": [
						{
							"type": "description",
							"value": "Rewards for accomplishments during HNGi9"
						}
					]
				}
			}

def main():
	hashlst = []
	directory = 'jsonfiles'
	with open('hng9.csv', 'r', newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')    
		for row in reader:
			out = json.dumps(make_record(row), indent=4)
			jsonoutput = open('jsonfiles/'+ str(row["Filename"].strip()) + '.json', 'w')
			jsonoutput.write(out)
			jsonoutput.close()
		for item in os.listdir(directory):
			jsonf = os.path.join(directory, item)
			print(jsonf)
			with open(jsonf, "rb") as f:
				bytes = f.read()
				readable_hash = hashlib.sha256(bytes).hexdigest()
				hashlst.append(readable_hash)
				f.close()

	csv_input = pd.read_csv('hng9.csv')
	csv_input['Hash'] = hashlst

	csv_input.to_csv('filename.output.csv', index=False)

if __name__ == "__main__":   
    main()
