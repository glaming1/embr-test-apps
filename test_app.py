import unittest

from app import app


class GreetingTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_has_working_form_and_local_assets(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('action="/hello"', html)
        self.assertIn('name="name"', html)
        self.assertIn('data-preview-name', html)
        for path in ("/static/studio.css", "/static/studio.js"):
            with self.client.get(path) as asset:
                self.assertEqual(asset.status_code, 200)

    def test_personalized_greeting_preserves_unicode(self):
        response = self.client.post("/hello", data={"name": "Zoë & friends"})
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("Zoë &amp; friends", html)
        self.assertIn("It is nice to meet you!", html)
        self.assertIn('href="/#create"', html)

    def test_name_is_escaped_in_title_and_greeting(self):
        name = '<script>alert("hello")</script>'
        response = self.client.post("/hello", data={"name": name})
        html = response.get_data(as_text=True)
        self.assertNotIn(name, html)
        self.assertEqual(html.count("&lt;script&gt;"), 2)

    def test_missing_and_empty_names_still_redirect_home(self):
        for data in ({}, {"name": ""}):
            with self.subTest(data=data):
                response = self.client.post("/hello", data=data)
                self.assertEqual(response.status_code, 302)
                self.assertEqual(response.headers["Location"], "/")


if __name__ == "__main__":
    unittest.main()
