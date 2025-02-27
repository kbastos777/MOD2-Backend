from flask import Flask
from flask import request
from flask import jsonify
import json
import os

app = Flask(__name__)


@app.route("/")
def root():
    return "<h1>Hello, World!</h1>"


def write_json_file(filename,data):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump(data, file)
    else:
        with open(filename, "a") as file:
                file.write("\n")
                json.dump(data, file)
                


def list_tasks(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            tasks_list=[]
            for record in file.readlines():
                tasks_list.append(json.loads(record))
    except IndexError as ex:
        print(f"An error occurred in list_tasks function due to: {ex}")
    return tasks_list


@app.route("/tasks", methods=["GET"])
def get_task():
    filtered_tasks = list_tasks('json_file.json')
    task_filter = request.args.get("status")
    if task_filter:
        filtered_tasks = list(
            filter(lambda task: task["status"] == task_filter, filtered_tasks)
        )

    return {"data": filtered_tasks}


@app.route("/tasks",methods=["POST"])
def create_new_task():
    try:
        identifier = request.form.get("identifier")
        title = request.form.get("title")
        description = request.form.get("description")
        status = request.form.get("status")
        tasks_dict = {
            'identifier': identifier,
            'title': title,
            'description':description,
            'status':status
        } 
        if status != "pending" or status != "in progress" or status != "completed":
            raise ValueError("Please enter only the current 3 available status:(pending, in progress or completed)")
        if not all([identifier,title,description,status]):
            return jsonify(message="no empty spaces allowed"), 400
        write_json_file('json_file.json',tasks_dict)
        return tasks_dict
    except ValueError as err:
        return jsonify(message=str(err)), 400
        


@app.route("/tasks",methods=["PUT"])
def edit_json_file():
    identifier = request.form.get("identifier")
    title = request.form.get("title")
    description = request.form.get("description")
    status = request.form.get("status")
    tasks_dict = {
        'identifier': identifier,
        'title': title,
        'description':description,
        'status':status
    } 
    if not identifier or not title or not description or not status:
        return jsonify(message="no empty spaces allowed"), 400
    write_json_file('json_file.json',tasks_dict)
    return tasks_dict


@app.route("/tasks",methods=["DELETE"])
def delete_task():
        return {
            "year": 2024,
            "description": "Esto es un endpoint secundario",
        }


if __name__ == "__main__":
    app.run(host="localhost", debug=True)