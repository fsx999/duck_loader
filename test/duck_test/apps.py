# coding=utf-8
from django.apps import AppConfig


class DuckTestApp(AppConfig):
    name = "duck_loader.test.duck_test"
    label = 'test.duck_test'
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

    collapse_settings = [{
        "group_label": "auth",
        "icon": 'fa-fw fa fa-group',
        "entries": [{
            "label": 'Groupes',
            "icon": 'fa-fw fa fa-group',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }, {
            "label": 'Permissions',
            "icon": 'fa-fw fa fa-lock',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }, {
            "label": 'Utilisateurs',
            "icon": 'fa-fw fa fa-user',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    }, {
        "group_label": "Django_Apogee",
        "icon": 'fa-fw fa fa-circle-o',
        "entries": [{
            "label": 'Settings année universitaire',
            "icon": 'fa-fw fa fa-circle-o',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    },]


    dashboard_settings = [{
        "group_label": "Scolarité",
        "icon": 'fa fa-caret-square-o-right',
        "entries": [{
            "label": 'Pré-Inscription',
            "icon": 'fa fa-rocket',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        },
        {
            "label": 'Consultation dossier inscription etudiant apogée',
            "icon": 'fa fa-rocket',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        },
        {
            "label": 'Extraction',
            "icon": 'fa fa-rocket',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    }, {
        "group_label": "Informations",
        "icon": 'fa fa-caret-square-o-right',
        "entries": [{
            "label": 'Statistique',
            "icon": 'fa fa-rocket',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        },
        {
            "label": 'Dates et tarifs',
            "icon": 'fa fa-rocket',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        },{
            "label": 'Annuaire',
            "icon": 'fa fa-rocket',
            "url": 'mon_url',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    }]

    search = [
        {
            "labal": 'toto',
            "url": "mon_url",
            'post_param': 'search',
        }
    ]
