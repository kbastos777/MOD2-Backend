from flask import request,jsonify,Flask
from flask.views import MethodView
import json
import os

app = Flask(__name__)

def write_json_file(filename,data):
        try:
            if not os.path.exists(filename):
                with open(filename, "w") as file:
                    json.dump(data, file)
                    file.write("\n")
            else:
                with open(filename, "a") as file:
                        json.dump(data, file)
                        file.write("\n")
        except FileNotFoundError as err:
            return jsonify(message=str(err)), 400


def list_tasks(file_path):
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                tasks_list=[]
                for record in file.readlines():
                    tasks_list.append(json.loads(record))
        except IndexError as ex:
            print(f"An error occurred in list_tasks function due to: {ex}")
        return tasks_list


class TaskAPI(MethodView):


    def get(self):
        try:
            filtered_tasks = list_tasks('json_file.json')
            task_filter = request.args.get("status")
            if task_filter:
                filtered_tasks = list(
                    filter(lambda task: task["status"] == task_filter, filtered_tasks)
                )

            return {"data": filtered_tasks}
        except Exception as err:
            return jsonify(message=str(err)), 400


    def post(self):
        try:
            if os.path.exists('json_file.json'):
                tasks_list = list_tasks('json_file.json')

            identifier = request.form.get("identifier")
            title = request.form.get("title")
            description = request.form.get("description")
            status = request.form.get("status")
            
            if not all([identifier,title,description,status]):
                return jsonify(message="no empty spaces allowed"), 400
            elif status not in (["pending", "in progress", "completed"]):
                raise ValueError("Please enter only the current 3 available status:(pending, in progress or completed)")
            elif os.path.exists('json_file.json') and any(task['identifier'] == identifier for task in tasks_list):
                raise ValueError("Please enter an unique identifier")
            
            
            tasks_dict = {
                'identifier': identifier,
                'title': title,
                'description':description,
                'status':status
            } 


            write_json_file('json_file.json',tasks_dict)
            return jsonify(tasks_dict), 201
        except ValueError as err:
            return jsonify(message=str(err)), 400


    def put(self):
        try:
            if os.path.exists('json_file.json'):
                tasks_list = list_tasks('json_file.json')

            identifier = request.form.get("identifier")
            title = request.form.get("title")
            description = request.form.get("description")
            status = request.form.get("status")
            
            if not all([identifier,title,description,status]):
                return jsonify(message="no empty spaces allowed"), 400
            elif status not in (["pending", "in progress", "completed"]):
                raise ValueError("Please enter only the current 3 available status:(pending, in progress or completed)")
            
            task_index = next((index for index, task in enumerate(tasks_list) if task['identifier'] == identifier), None) #aca next va a tomar el indice de la lista que contenga el identifier y asigna el valor a la variable
            if task_index is None:
                return jsonify(message="Task not found"), 404
            
            # Actualizamos la tarea en la lista
            tasks_list[task_index] = {
                'identifier': identifier,
                'title': title,
                'description': description,
                'status': status
            }

            # Sobrescribe el archivo JSON con la lista actualizada
            with open('json_file.json', 'w', encoding='utf-8') as file:
                for task in tasks_list:
                    json.dump(task, file)
                    file.write("\n")

            return jsonify(message="Task updated successfully")
        except ValueError as err:
            return jsonify(message=str(err)), 400


    def delete(self):
        try:
            if os.path.exists('json_file.json'):
                tasks_list = list_tasks('json_file.json')

            identifier = request.form.get("identifier")
            title = request.form.get("title")
            description = request.form.get("description")
            status = request.form.get("status")
            
            if not all([identifier,title,description,status]): #En caso de que no existan valores para cada una de las variables se debe mostrar un mensaje que diga que los campos son obligatorios
                return jsonify(message="no empty spaces allowed"), 400
            elif status not in (["pending", "in progress", "completed"]):
                raise ValueError("Please enter only the current 3 available status:(pending, in progress or completed)")
            
            task_index = next((index for index, task in enumerate(tasks_list) if task['identifier'] == identifier), None)
            if task_index is None:
                return jsonify(message="Task not found"), 404
            
            # Actualizar la tarea en la lista
            tasks_list.pop(task_index)

            # Sobrescribir el archivo JSON con la lista actualizada
            with open('json_file.json', 'w', encoding='utf-8') as file:
                for task in tasks_list:
                    json.dump(task, file)
                    file.write("\n")  # Escribir cada tarea en una nueva línea

            return jsonify(message="Task removed successfully")
        except ValueError as err:
            return jsonify(message=str(err)), 400



task_view = TaskAPI.as_view('task_api')
app.add_url_rule('/tasks', view_func=task_view, methods=['GET', 'POST'])
app.add_url_rule('/tasks', view_func=task_view, methods=['PUT', 'DELETE'])

if __name__ == "__main__":
    app.run(host="localhost", debug=True)