import yaml

#step 1. open the file
with open('prometheusOperator-clusterRole.yaml','r') as f: 
    data = list(yaml.safe_load_all(f))

#step 2: Extract apiGroups
api_groups= set()
label_count = 0

for doc in data: 
    if not isinstance(doc,dict):
        continue

    rules = doc.get('rules',[])
    #Walk the "rules" section
    for rule in rules:
        groups = rule.get('apiGroups', [])
        api_groups.update(groups)

    

    #Countlabels
    metadata = doc.get('metadaata',{})
    labels = metadata.get('labels',{})
    label_count += len(labels)

#step 3: Output

print("API Groups (deduplicated):", api_groups)
print("Total label Count:", label_count)