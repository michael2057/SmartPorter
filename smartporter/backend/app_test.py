import unittest
import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        self.client = app.app.test_client()

    def test_chat(self):
        # No JSON data sent
        
        headers = {'Content-Type': 'application/json'}
        response = self.client.post('/api/chat', json={'message': '世界上最长寿的人是谁？活了多大岁数？'}, headers=headers)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
