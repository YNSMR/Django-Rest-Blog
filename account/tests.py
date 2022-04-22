from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.
# Doğru veriler ile kayıt işlemi yap.
# Şifre invalid olabilir
# Şifre zaten kullannılmış olabilir.
# Üye girşi yaptıysak o sayfa görünmemeli.
# token ile girişte 403 hatası alınmalı

class UserRegistrationTestCase(APITestCase):
    url = reverse("account:register")

    def test_user_registration(self):
        """
            Doğru veriler ile kayıt işlemi
        :return:
        """
        data = {
            "username": "yunustest",
            "password": "deneme123"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_user_invalid_password(self):
        """
            Yanlış password verisi ile Test işlemi
        :return:
        """
        data = {
            "username": "yunustest",
            "password": "1"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_unique_name(self):
        """
            Benzersiz isim Testi
        :return:
        """
        self.test_user_registration()
        data = {
            "username": "yunustest",
            "password": "1dsgsgsddsvsdf"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_user_authenticated_registration(self):
        """
            session ile giriş yapmış kullanıcı sayfayı görememeli.
        :return:
        """
        self.test_user_registration()

        self.client.login(username='yunustest', password='deneme123')
        response = self.client.post(self.url)
        self.assertEqual(403, response.status_code)

    def test_user_authenticated_token_registration(self):
        """
            token ile giriş yapmış kullanıcı sayfayı görememeli.
        :return:
        """
        self.test_user_registration()

        self.client.login(username='yunustest', password='deneme123')
        response = self.client.post(self.url)
        self.assertEqual(403, response.status_code)
