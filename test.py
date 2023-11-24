import unittest
from flask import Flask
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_video_details_no_url(self):
        response = self.app.get('/')
        data = response.get_json()
        self.assertEqual(data['error'], 'Please provide a video URL or id')

    def test_video_details_with_url(self):
        # replace 'test_url' with a valid youtube video url or id for the test
        response = self.app.get('/?video=https://www.youtube.com/watch?v=xiRC_by_7eY&ab_channel=5secondfilms')
        data = response.get_json()
        # assert the expected response here
        self.assertEqual(data, {
            'channel': '5secondfilms',
            'title': 'Eating in Bed',
            'transcript': 'I hate it when you eat in bed.\nAnd for our next course, you...',
            'url': 'https://www.youtube.com/watch?v=xiRC_by_7eY'
        })

    def test_video_details_with_id(self):
        # replace 'test_url' with a valid youtube video url or id for the test
        response = self.app.get('/?video=xiRC_by_7eY')
        data = response.get_json()
        # assert the expected response here
        self.assertEqual(data, {
            'channel': '5secondfilms',
            'title': 'Eating in Bed',
            'transcript': 'I hate it when you eat in bed.\nAnd for our next course, you...',
            'url': 'https://www.youtube.com/watch?v=xiRC_by_7eY'
        })

    def test_video_details_with_long_id(self):
        # replace 'test_url' with a valid youtube video url or id for the test
        response = self.app.get('/?video=xB6oRi9TIkyQ')
        data = response.get_json()
        # assert the expected response here
        self.assertEqual(data, {
            'error': '"xB6oRi9TIkyQ" is not a valid video id'
        })

    def test_video_details_with_bad_id(self):
        # replace 'test_url' with a valid youtube video url or id for the test
        response = self.app.get('/?video=x')
        data = response.get_json()
        # assert the expected response here
        self.assertEqual(data, {
            'error': '"x" is not a valid video id'
        })

if __name__ == '__main__':
    unittest.main()