from pymongo import MongoClient

client = MongoClient("mongodb+srv://cmunoz-admin:Seti2019*@cluster0-ghkjh.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('student_db')
records = db.student_records
print(records.count_documents({}))
new_student = {'name':'otro', 
               'roll_on':456,
               'branch':'ere'}
#records.insert_one(new_student)
new_students = [{'name':'pedro', 
               'roll_on':457,
               'branch':'ere'},
               {'name':'pablo', 
               'roll_on':458,
               'branch':'csi'}
               ]
#records.insert_many(new_students)
print(records.count_documents({}))
print('LISTA: ',list(records.find()))
print('UN REGISTRO: ',records.find_one({'roll_on': 456}))


student_updates = {'name': 'el otro'}
results = records.update_one(
        {'roll_on': 456}, 
        {'$set' : {'name': 'el otro'}
        })
print(results.modified_count)        
print('UN REGISTRO: ',records.find_one({'roll_on':456}))