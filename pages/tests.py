from django.test import SimpleTestCase

# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_portfolio_page_status_code(self):
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_socials_page_status_code(self):
        response = self.client.get('/socials/')
        self.assertEqual(response.status_code, 200)

    def test_bootstrapless_page_status_code(self):
        response = self.client.get('/socials/bootstrapless/')
        self.assertEqual(response.status_code, 200)
