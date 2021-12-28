import json  #built-int package 
# Converting Json file to Python
# data
x = '{"Name":"Laxman", "Age":25, "City":"Brisbane"}'

# Parse x
y = json.loads(x)

#result comes in dictionary 
print(y['Name'])


# Converting Python to Json
#
# a python object (dict):
x={
    "Name":"Laxman",
    "Age":25,
    "City":"Brisbane"
}

# Convert into JSON
y = json.dumps(x) #Serialize obj to a JSON formatted str.

# writing into file
file = open('File.txt','w')
file.write(y)
file.close()

# the result is a JSON string
print("This data is from Json:\n",y)

# read from file
fileR = open('File.txt','r')
dataFromFile = fileR.read()
fileR.close()

print("This data is from File:\n",dataFromFile)
usr = json.loads(dataFromFile)
print(usr["Name"])