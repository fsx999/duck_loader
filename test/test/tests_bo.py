# coding=utf-8
from django.test import TestCase
from duck_loader.templatetags.duck_loader import config_navbar
from mock.mock import MagicMock, patch

def config():
    class Config:
        url = {"regex": "^duck_test/", "module_url": "urls"}

        navbar_settings = [
            {
                "type": "link",
                "icon": 'fa fa-key',  # facultatif
                "url": 'mon_ur',  # name or url
                "class": 'left',  # name or url
                "label": "link",
                "groups_permissions": [],  # facultatif
                "permissions": [],  # facultatif
            },

            {
                "type": "dropdown",
                "dropdown_label": "toto",
                'class': 'right',
                'groups_permissions': ['recrutrement'],  # facultatif
                'permissions': [],  # facultatif
                'entries': [{
                    "label": 'my entry',
                    "icon": 'fa fa-key',
                    "url": 'mon_url',  # name or url
                    "groups_permissions": [],   # facultatif
                    "permissions": [],  # facultatif
                },
                {
                    "label": 'my entry',
                    "icon": 'fa fa-key',
                    "url": 'mon_url',  # name or url
                    "groups_permissions": [],   # facultatif
                    "permissions": [],  # facultatif
                },
                {
                    "label": 'toto',
                    "icon": 'fa fa-key',
                    "url": 'mon_url',  # name or url
                    "groups_permissions": [],   # facultatif
                    "permissions": [],  # facultatif
                },
                 {
                    "label": 'totos',
                    "icon": 'fa fa-key',
                    "url": 'mon_url',  # name or url
                    "groups_permissions": [],   # facultatif
                    "permissions": [],  # facultatif
                }],
            }
        ]

    config = Config()
    config.module = MagicMock()
    config.module.__name__ = "duck_loader.test.duck_test"
    return [config]


class MenuTagLoader(TestCase):

    @patch('duck_loader.templatetags.duck_loader.apps.get_app_configs', new=config)
    def test_navbar(self):
        config = config_navbar()
        self.assertEqual(len(config), 2)


