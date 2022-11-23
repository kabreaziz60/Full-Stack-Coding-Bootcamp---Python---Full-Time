# 🌟 Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.





# Exercice 2 : Travailler Avec JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
#1
sampleJson = json.loads(sampleJson)
print(sampleJson['company']["employee"]['payable']['salary'])
sampleJson['company']['employee'].update({'birth_date':''})
print(sampleJson)

#3
import json
jsonFile = 'fic.json'
with open(jsonFile,'w') as jF:
    json.dump(sampleJson,jF)