from os import listdir
from os.path import isfile, join

# Get all .rst filenames in API to write to index.md
# In github workflow, script is called outside the doc directory
api_path  = 'doc/API/'
api_files = [f for f in listdir(api_path) if isfile(join(api_path, f))]

api_names = []
for f in api_files:
    f_parts = f.split('.')
    if(len(f_parts) == 3):
        api_names.append(f_parts[0] + '.' + f_parts[1])

# Open API/index.md to modify
f_api = open("API/index.md", "a")
for api_name in api_names:
    # Write api file names
    f_api.write(api_name + '\n')
# Close toctree
f_api.write('```')
f_api.close()
