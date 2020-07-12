import pickle

courses = {
    "Python": {"Name": "Python", "Enrolled": 0, "Description": "its an amazing course"},
    "Golang": {"Name": "Golang", "Enrolled": 0, "Description": "its an amazing course"},
    "Rust": {"Name": "Rust", "Enrolled": 0, "Description": "its an amazing course"},
    "Javascript": {"Name": "Javascript", "Enrolled": 0, "Description": "its an amazing course"},
    "Matlab": {"Name": "Matlab", "Enrolled": 0, "Description": "its an amazing course"},
    "Julia": {"Name": "Julia", "Enrolled": 0, "Description": "its an amazing course"},
}
with open("Courses.pkl", 'wb')as f:
    pickle.dump(courses, f)
