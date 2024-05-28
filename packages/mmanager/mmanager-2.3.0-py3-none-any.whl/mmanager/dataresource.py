import json
import requests
import datetime


def get_model_data(model_data):

    data = model_data
    registryOption = model_data.get('registryOption', None) 
    if registryOption:
        registryOption = json.dumps(registryOption)
        data.update({"registryOption": registryOption})

    fetchOption = model_data.get('fetchOption', None)
    if fetchOption:
        fetchOption = json.dumps(fetchOption)
        data.update({"fetchOption": fetchOption})
    
    return data

def get_files(model_data):
        training_dataset = model_data.get('training_dataset', None)
        pred_dataset = model_data.get('pred_dataset', None)
        actual_dataset = model_data.get('actual_dataset', None)
        test_dataset = model_data.get('test_dataset', None)
        model_image_path = model_data.get('model_image_path', None)
        model_summary_path = model_data.get('model_summary_path', None)
        model_file_path = model_data.get('model_file_path', None)

        files = {}

        if training_dataset:
            training_dataset = open(training_dataset, 'rb')
            files.update({"training_dataset": training_dataset})

        if pred_dataset:
            pred_dataset = open(pred_dataset, 'rb')
            files.update({"pred_dataset": pred_dataset})

        if actual_dataset:
            actual_dataset = open(actual_dataset, 'rb')
            files.update({"actual_dataset": actual_dataset})

        if test_dataset:
            test_dataset = open(test_dataset, 'rb')
            files.update({"test_dataset": test_dataset})

        if model_image_path:
            model_image_path = open(model_image_path, 'rb')
            files.update({"model_image_path": model_image_path})

        if model_summary_path:
            model_summary_path = open(model_summary_path, 'rb')
            files.update({"model_summary_path": model_summary_path})

        if model_file_path:
            model_file_path = open(model_file_path, 'rb')
            files.update({"model_file_path": model_file_path})
    

        return files
