from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_background_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
