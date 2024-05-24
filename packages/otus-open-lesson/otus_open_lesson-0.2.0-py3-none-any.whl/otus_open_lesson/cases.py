from rest_framework.test import APITestCase


class OtusOpenLessonTestCase(APITestCase):

    def assertStatusCode(self, response, code):
        self.assertEqual(response.status_code, code)

    def assertResponse(self, response, **kwargs):
        for k,v in kwargs.items():
            result = getattr(response, k)
            expected = v
            self.assertEqual(result, expected)