
import json

def convert_dataset_to_productname_dict(inputfile, outputfile):
    with open(inputfile) as dataset:
        data = json.load(dataset)
    for entry in data:
	    print entry['name']
	    with open(outputfile, 'a') as output:
	        output.write(entry['name'])
			
			
if __name__ == "__main__":
    convert_dataset_to_productname_dict('products.json', 'product_name_dict.txt')