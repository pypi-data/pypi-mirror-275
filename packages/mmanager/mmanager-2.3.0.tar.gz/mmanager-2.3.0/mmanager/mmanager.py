import os
import json
import requests
import traceback
from .dataresource import *
from .serverequest import *
from .log_keeper import *

class ModelManager:
    def  __init__(self, secret_key, base_url):
        self.base_url = base_url
        self.project_data = {}
        self.secret_key = secret_key
    
    def _get_headers(self, **kwargs):
        '''Returns headers for request
        '''
        headers = {'Authorization': 'secret-key {0}'.format(self.secret_key)}

        return headers
    
class LLMCreds(ModelManager):
    def post(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/llmCreds/" % (self.base_url)
    
        try:
            llm_creds = requests.post(url, data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            llm_creds = e

        if llm_creds.status_code == 201:
            logger.info("Created LLM Creds succeed with status code %s" % llm_creds.status_code)
        else:
            logger.error("Created LLM Creds failed with status code %s" % llm_creds.status_code)
            if llm_creds.json()['name'][0]:
                logger.error(llm_creds.json()['name'][0])
        return llm_creds

class RelatedDatabase(ModelManager):
    def post_related_db(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/related_db/" % (self.base_url)
    
        try:
            related_db = requests.post(url, data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            related_db = e

        if related_db.status_code == 201:
            logger.info("Created Related Database succeed with status code %s" % related_db.status_code)
        else:
            logger.error("Related Database creation failed with status code %s" % related_db.status_code)
            if related_db.json()['name'][0]:
                logger.error(related_db.json()['name'][0])
        return related_db        

class DatabaseLink(ModelManager):
    def post_db_link(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/externaldb_link/" % (self.base_url)
    
        try:
            db_link = requests.post(url, data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            db_link = e

        if db_link.status_code == 201:
            logger.info("Created Database Link succeed with status code %s" % db_link.status_code)
        else:
            logger.error("Database Link creation failed with status code %s" % db_link.status_code)
            if db_link.json()['name'][0]:
                logger.error(db_link.json()['name'][0])
        return db_link

class ReleaseTable(ModelManager):
    def post(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/releaseTable/" % (self.base_url)
    
        try:
            db_link = requests.patch(url, data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            db_link = e

        if db_link.status_code == 201:
            logger.info("Update db_link succeed with status code %s" % db_link.status_code)
        else:
            logger.error("Update db_link failed with status code %s" % db_link.status_code)
            if db_link.json()['name'][0]:
                logger.error(db_link.json()['name'][0])

class Usecase(ModelManager):
  
    def post_usecase(self, usecase_info, forecasting_fields={}, forecasting_feature_tabs={}):
        '''Post Usecase
        '''
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/" % self.base_url
        
        image_p = usecase_info.get('image', None)
        banner_p = usecase_info.get('banner', None)

        #for images
        files = {}
        if image_p:
            files.update({"image":open(image_p, 'rb')})

        if banner_p:
            files.update({"banner":open(banner_p, 'rb')})
        
        #for usecase_info
        data= {}
        files_key_list = ['image', 'banner']
        for key in files_key_list:
            usecase_info.pop(key, None)

        # Add all the usecase data into one
        data.update(usecase_info)

        # For Forecasting
        if usecase_info.get("usecase_type", None)=="Forecasting":
            data.update(forecasting_fields)
            # data.update(forecasting_tables_fields)
            data.update(forecasting_feature_tabs)
    
        try:
            usecase = requests.post(url,
                    data=data, files=files, headers=kwargs['headers'])
            if usecase.status_code == 201:
                logger.info("Post usecase succeed with status code %s" % usecase.status_code)
            else:
                logger.error("Post usecase failed with status code %s" % usecase.status_code)
                if usecase.json()['name'][0]:
                    logger.error(usecase.json()['name'][0])
        except Exception as e:
            logger.error(str(e))
            usecase = e
            
        return usecase

    def patch_usecase(self, usecase_data, usecase_id):
        '''Update Usecase
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)

        #for images
        image_p = usecase_data.get('image', None)
        banner_p = usecase_data.get('banner', None)

        if image_p and banner_p:
            files={
                "image":open(image_p, 'rb'),
                "banner":open(banner_p, 'rb')
            }
        elif image_p:
            files={
                "image":open(image_p, 'rb'),
            }
        elif banner_p:
            files={
                "image":open(banner_p, 'rb'),
            }
        else:
            files = {}
        
        #for usecase_data
        data = usecase_data

        try:
            usecase = requests.patch(url,
                    data=data, files=files, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecase = e

        if usecase.status_code == 200:
            logger.info("Update usecase succeed with status code %s" % usecase.status_code)
        else:
            logger.error("Update usecase failed with status code %s" % usecase.status_code)
            if usecase.json()['name'][0]:
                logger.error(usecase.json()['name'][0])

        return usecase

    def delete_usecase(self, usecase_id):
        '''Delete Usecase
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)
        
        try:
            usecase = requests.delete(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecase = e

        if usecase.status_code == 204:
            logger.info("Delete usecase succeed with status code %s" % usecase.status_code)
        else:
            logger.info("Delete usecase failed with status code %s" % usecase.status_code)
            if usecase.json()['name'][0]:
                logger.error(usecase.json()['name'][0])
            
        return usecase

    def get_usecases(self):

        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/get_usecases/" % self.base_url
        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e
        return usecases
    
    def get_detail(self, usecase_id):

        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)
        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e

        return usecases

    def get_models(self, usecase_id):

        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/getmodels/?usecase_id=%s" % (self.base_url, usecase_id)

        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e
        return usecases
    
    def load_cache(self, usecase_id):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/data_loadcache/?usecase_id=%s" % (self.base_url, usecase_id)
        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e
        return usecases

class Applications(ModelManager):
    
    def post_application(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/applications/" % (self.base_url)

        try:
            application = requests.post(url,
                    data=data, headers=kwargs['headers'])
            
            if application.status_code == 201:
                logger.info("Post application succeed with status code %s" % application.status_code)
            else:
                logger.error("Post application failed with status code %s" % application.status_code)
                if application.json()['name'][0]:
                    logger.error(application.json()['name'][0])
        except Exception as e:
            logger.error(str(e))
            application = e

        return application
    
    def delete_application(self, usecase_id):
        '''Delete application
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/applications/%s/" % (self.base_url, usecase_id)
        
        try:
            application = requests.delete(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            application = e

        if application.status_code == 204:
            logger.info("Delete application succeed with status code %s" % application.status_code)
        else:
            logger.info("Delete application failed with status code %s" % application.status_code)
            if application.json()['name'][0]:
                logger.error(application.json()['name'][0])
            
        return application
    
    def get_applications(self):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/applications/" % (self.base_url)

        try:
            applications = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            applications = e
        return applications

class ExternalDatabase(ModelManager):
    def post_related_db(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/related_db/" % (self.base_url)

        try:
            related_db = requests.post(url,
                    data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            related_db = e
        return related_db
    
    def get_related_db(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/related_db/" % (self.base_url)

        try:
            related_db = requests.get(url,
                    data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            related_db = e
        return related_db

    def link_externaldb(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/externaldb_link/" % (self.base_url)

        try:
            db_link = requests.post(url,
                    data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            db_link = e
        return db_link
    
    def get_externaldb_links(self):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/externaldb_link/" % (self.base_url)

        try:
            db_links = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            db_links = e
        return db_links

class Model(ModelManager):

    def post_model(self, model_data, ml_options={}, data_distribution=True):
        '''Post Model
        '''
        url = "%s/api/models/" % self.base_url

        kwargs = {
            'headers': self._get_headers()
        }

        #for model_data
        model_data.update(ml_options)
        model_data.update({"data_distribution":data_distribution})
        data = get_model_data(model_data)

        #for model_files
        files = get_files(model_data)

        try:
            model = model_request(url, kwargs, data, ml_options, files)

            if model.status_code == 201:
                logger.info("Model creation succeed with status code %s" % model.status_code)
            else:
                logger.error("Model creation failed with status code %s" % (model.status_code))
                if model.json()['name'][0]:
                    logger.error(model.json()['name'][0])

        except Exception as e:
            logger.error(str(e))
            model = e
        
        return model
    
    def delete_model(self, model_id):

        '''Delete Model
        '''

        kwargs = {
            'headers': self._get_headers()
        }
        
        url = "%s/api/models/%s/" % (self.base_url, model_id)
        
        try:
            model = requests.delete(url, headers=kwargs['headers'])

            if model.status_code == 204:
                logger.info("Delete model succeed with status code %s" % model.status_code)
            else:
                logger.error("Delete model failed with status code %s" % model.status_code)
                if model.json()['name'][0]:
                    logger.error(model.json()['name'][0])

        except Exception as e:
            logger.error(str(e))
            model = e
            
        return model

    def patch_model(self, model_data, model_id, create_sweetviz=True):

        '''Update Model
        '''

        url = "%s/api/models/%s/" % (self.base_url, model_id)

        kwargs = {
            'headers': self._get_headers()
        }

        #for model_data
        data = model_data
        data.update({"create_sweetviz":create_sweetviz})      

        #for model_files
        files = get_files(model_data)

        try:
            model = requests.patch(url, data=data, files=files, headers=kwargs['headers'])

            if model.status_code == 200:
                logger.info("Update model succeed with status code %s" % model.status_code)
            else:
                logger.error("Update model failed with status code %s" % model.status_code)
                # if model.json()['name'][0]:
                #     logger.error(model.json()['name'][0])
        except Exception as e:
            logger.error(str(e))
            model = e

        return model

    def generate_report(self, model_id):
        '''Generate Model Report
        '''

        kwargs = {
            'headers': self._get_headers()
        }


        url = "%s/api/govrnreport/%s/generateReport/" % (self.base_url, model_id)

        try:
            model = requests.post(url, headers=kwargs['headers'])

            if model.status_code == 201:
                logger.info("Report Generation succeed with status code %s" % model.status_code)
            else:
                logger.error("Report Generation failed with status code %s" % model.status_code)
                if model.json()['name'][0]:
                    logger.error(model.json()['name'][0])

        except Exception as e:
            logger.error(str(e))
            model = e

        return model

    def get_details(self, model_id):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/models/%s/" % (self.base_url, model_id)
        try:
            model = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            model = e

        return model
    
    def get_latest_metrics(self, model_id, metric_type):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/models/get_latest_metrics/?model_id=%s&&metric_type=%s" % (self.base_url, model_id, metric_type)
        try:
            model = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            model = e

        return model

    def get_all_reports(self, model_id):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/models/get_all_reports/?model_id=%s" % (self.base_url, model_id)
        try:
            model = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            model = e

        return model
    
    def create_insight(self, model_id):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/insight/create_insight/?model_id=%s" % (self.base_url, model_id)
        try:
            model_insight = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            model_insight = e

        if model_insight.status_code == 200:
            logger.info("Model insight creation succeed with status code %s" % model_insight.status_code)
        else:
            logger.error("Model insight creation failed with status code %s" % (model_insight.status_code))

        return model_insight
    
    def create_causalgraph(self, model_id, target_col, algorithm):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/CausalGraph/%s/create_causalgraph/?target_col=%s&&algorithm=%s" % (self.base_url, model_id, target_col, algorithm)
        try:
            causal_graph = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            causal_graph = e

        if causal_graph.status_code == 200:
            logger.info("Causal Graph creation succeed with status code %s" % causal_graph.status_code)
        else:
            logger.error("Causal Graph creation failed with status code %s" % (causal_graph.status_code))

        return causal_graph
   
class TableInfo(ModelManager):
    def post_table_info(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/table_info/" % (self.base_url)
    
        try:
            table_info = requests.post(url, data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            table_info = e

        if table_info.status_code == 201:
            logger.info("Created Table Info Link succeed with status code %s" % table_info.status_code)
        else:
            logger.error("Table Info Link creation failed with status code %s" % table_info.status_code)
            if table_info.json()['name'][0]:
                logger.error(table_info.json()['name'][0])
        return table_info
    
class FieldInfo(ModelManager):
    def post_field_info(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/table_info/" % (self.base_url)
    
        try:
            field_info = requests.post(url, data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            field_info = e

        if field_info.status_code == 201:
            logger.info("Created Field Info Link succeed with status code %s" % field_info.status_code)
        else:
            logger.error("Field Info Link creation failed with status code %s" % field_info.status_code)
            if field_info.json()['name'][0]:
                logger.error(field_info.json()['name'][0])
        return field_info
    
