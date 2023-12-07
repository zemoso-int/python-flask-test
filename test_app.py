# test_app.py
import unittest
import json
from app import app, tasks

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_tasks(self):
        response = self.app.get('/tasks')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('tasks', data)

    def test_get_task(self):
        response = self.app.get('/tasks/1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('task', data)

    def test_get_task_not_found(self):
        response = self.app.get('/tasks/100')
        self.assertEqual(response.status_code, 404)

    def test_create_task(self):
        task_data = {'title': 'New Task', 'description': 'Description for New Task'}
        response = self.app.post('/tasks', json=task_data)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        self.assertIn('task', data)

    def test_update_task(self):
        task_data = {'title': 'Updated Task', 'done': True}
        response = self.app.put('/tasks/1', json=task_data)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('task', data)

    def test_update_task_not_found(self):
        task_data = {'title': 'Updated Task', 'done': True}
        response = self.app.put('/tasks/100', json=task_data)
        self.assertEqual(response.status_code, 404)

    def test_delete_task(self):
        response = self.app.delete('/tasks/1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'result': True})

    def test_delete_task_not_found(self):
        response = self.app.delete('/tasks/100')
        self.assertEqual(response.status_code, 404)

    # New Test Cases for Introduced Bugs
    def test_bug_index_out_of_range(self):
        response = self.app.get('/index-out-of-range')
        self.assertEqual(response.status_code, 500)  # Expecting an Internal Server Error

    def test_bug_division_by_zero(self):
        response = self.app.get('/division-by-zero')
        self.assertEqual(response.status_code, 500)  # Expecting an Internal Server Error

    def test_bug_null_pointer_exception(self):
        response = self.app.get('/null-pointer-exception')
        self.assertEqual(response.status_code, 500)  # Expecting an Internal Server Error

if __name__ == '__main__':
    unittest.main()
