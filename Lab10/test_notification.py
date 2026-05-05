import unittest
from unittest.mock import Mock
from notification import NotificationService, UserManager

class TestUserManager(unittest.TestCase):

    def test_notify_user(self):
        mock_service = Mock(spec=NotificationService)

        manager = UserManager(mock_service)
        manager.notify_user("Ivan", "Hello!")

        mock_service.send.assert_called_once_with("Ivan", "Hello!")

if __name__ == "__main__":
    unittest.main()