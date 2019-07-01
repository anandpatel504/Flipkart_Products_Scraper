
# jsondata = json.dumps(data, indent=4, sort_keys=False)
# with open('ngo.json', 'w') as f:
#     f.write(jsondata)
#     f.close()
import json,csv
infile = open('flipkart.json', 'r+')
outfile = open('flipkart.csv', 'w')

writer = csv.writer(outfile)
loading = json.loads(infile.read())

writer.writerow(loading[0].keys())
for row in loading:
    writer.writerow(row.values())