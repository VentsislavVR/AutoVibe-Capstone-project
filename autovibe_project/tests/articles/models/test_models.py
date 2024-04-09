from django.contrib.auth.models import Permission
from django.test import TestCase
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class ArticleModelTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email='testuser@example.com', password='12345')

    def test_permissions(self):
        change_permission = Permission.objects.get(codename='can_change_article')
        add_permission = Permission.objects.get(codename='can_add_article')

        self.user.user_permissions.add(change_permission, add_permission)

        self.assertTrue(self.user.has_perm("articles.can_change_article"))
        self.assertTrue(self.user.has_perm("articles.can_add_article"))
        self.assertFalse(self.user.has_perm("articles.can_delete_article"))