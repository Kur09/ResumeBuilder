import pymongo
from pymongo import collection


class Mongopy:

    def connect(self, collec):
        print("Welcome......")
        client = pymongo.MongoClient("mongodb://127.0.0.1/27017")
        db = client['ResumeBuilder']
        col = db[collec]
        print("Connected...")
        return col

    def save_to_db(self, fm, col):
        data = {
            "name": fm['name'],
            "email": fm['email'],
            "objective": fm['objective'],
            "prof": fm['prof'],
            "college": fm['college'],
            "college_location": fm['college_location'],
            "college_join": fm['college_join'],
            "college_leave": fm['college_leave'],
            "college_field": fm['college_field'],
            "college_per": fm['college_per'],
            "school_12": fm['school_12'],
            "school_12_location": fm['school_12_location'],
            "school_12_join": fm['school_12_join'],
            "school_12_leave": fm['school_12_leave'],
            "school_12_field": fm['school_12_field'],
            "school_12_per": fm['school_12_per'],
            "school_10": fm['school_10'],
            "school_10_location": fm['school_10_location'],
            "school_10_join": fm['school_10_join'],
            "school_10_leave": fm['school_10_leave'],
            "school_10_per": fm['school_10_per'],
            "skill_name_1": fm['skill_name_1'],
            "skill_1": fm['skill_1'],
            "skill_name_2": fm['skill_name_2'],
            "skill_2": fm['skill_2'],
            "skill_name_3": fm['skill_name_3'],
            "skill_3": fm['skill_3'],
            "project": fm['project'],
            "project_obj": fm['project_obj'],
            "project_tech": fm['project_tech']
        }
        col.insert_one(data)

    def drop_dbs(self, dbs, collection):
        print("Welcome......")
        client = pymongo.MongoClient("mongodb://127.0.0.1/27017")
        client.drop_database(dbs)

        print("Connected...")

    def getAll(self, collection):
        alldoc = collection.find()
        for item in alldoc:
            print(f"Name :: {item['name']}  Age :: {item['age']}  Minor :: {item['minor']}")
