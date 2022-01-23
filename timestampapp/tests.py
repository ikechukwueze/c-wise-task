from django.test import TestCase, Client
from .models import UuidTimeStamp
from django.http.response import JsonResponse
import uuid
import json
import datetime

# Create your tests here.


class TestUuidTimestampModel(TestCase):

    def setUp(self):
        self.model_obj = UuidTimeStamp.objects.create(uuid_code=uuid.uuid4())
        self.model_obj.save()

    def test_model_str(self):
        self.assertEqual(str(self.model_obj), str(self.model_obj.uuid_code))


class TestUuidTimestampView(TestCase):

    def setUp(self):
        self.client = Client()
        self.response = self.client.get("/")
        self.post_data = {
            "uuid_code":uuid.uuid4(),
            "timestamp":datetime.datetime.now()
        }
    
    def test_successful_get_request(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_response_is_json(self):
        self.assertEqual(type(self.response), JsonResponse)
    
    def test_failed_post_request(self):
        post_response = self.client.post("/", data=self.post_data)
        self.assertEqual(post_response.status_code, 405)
        
    def test_json_response_data_size(self):
        # this tests if the response length is same as database obj length
        resp = self.response.content
        response_length = len(json.loads(resp))
        self.assertEqual(UuidTimeStamp.objects.count(), response_length)
        
