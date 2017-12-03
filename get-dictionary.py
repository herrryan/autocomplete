import json

def load_dataset(file):
    with open(file) as dataset:
        data = json.load(dataset)
    for entry in data:
	    print entry['name']
	
	
if __name__ == "__main__":
    load_dataset('products.json')