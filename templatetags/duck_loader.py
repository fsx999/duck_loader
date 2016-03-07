# coding=utf-8
from __future__ import unicode_literals

from collections import OrderedDict
from copy import copy, deepcopy

from django import template
from django.apps import apps
from django.core.urlresolvers import reverse, NoReverseMatch
from django.shortcuts import render
from django.template import Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()


class NavbarErrorLabel(Exception):
    pass


def config_navbar():
    config = []
    result = OrderedDict()
    for x in apps.get_app_configs():
        if getattr(x, 'navbar_settings', None):
            config.append(getattr(x, 'navbar_settings'))
    for x in config:
        for item in x:
            if item['type'] == 'link':
                link(item, result)
            else:
                dropdown(item, result)
    return result


def reverse_url(url):
    try:
        return reverse(url)
    except NoReverseMatch:
        return url


def link(item, result):
    if item['label'] not in result:
        result[item['label']] = item
        item['url'] = reverse_url(item['url'])
    else:
        raise NavbarErrorLabel("L'entrée existe déjà")


def dropdown(item, result):
    entries = deepcopy(item['entries'])
    if item['dropdown_label'] not in result:

        result[item['dropdown_label']] = deepcopy(item)
        result[item['dropdown_label']]['entries'] = OrderedDict()
    for entry in entries:
        entry['url'] = reverse_url(entry['url'])
        result[item['dropdown_label']]['entries'][entry['label']] = entry


def collapse_item(item, result):
    entries = deepcopy(item['entries'])
    if item['group_label'] not in result:

        result[item['group_label']] = deepcopy(item)
        result[item['group_label']]['entries'] = OrderedDict()
    for entry in entries:
        entry['url'] = reverse_url(entry['url'])
        result[item['group_label']]['entries'][entry['label']] = entry

def dashboard_item(item, result):
    entries = deepcopy(item['entries'])
    if item['group_label'] not in result:

        result[item['group_label']] = deepcopy(item)
        result[item['group_label']]['entries'] = OrderedDict()
    for entry in entries:
        entry['url'] = reverse_url(entry['url'])
        result[item['group_label']]['entries'][entry['label']] = entry

def config_colapse():
    config = []
    result = OrderedDict()
    for x in apps.get_app_configs():
        if getattr(x, 'collapse_settings', None):
            config.append(getattr(x, 'collapse_settings'))
    for x in config:
        for item in x:
            collapse_item(item, result)
    return result

def config_dashboard():
    config = []
    result = OrderedDict()
    for x in apps.get_app_configs():
        if getattr(x, 'dashboard_settings', None):
            config.append(getattr(x, 'dashboard_settings'))
    for x in config:
        for item in x:
            dashboard_item(item, result)
    return result


@register.simple_tag(takes_context=True)
def navbar(context):
    request = context['request']
    config = config_navbar()
    return mark_safe(render_to_string('duck_admin/menu.html', context={'config': config}, request=request))


@register.simple_tag(takes_context=True)
def collapse(context):
    request = context['request']
    config = config_colapse()
    return mark_safe(render_to_string('duck_admin/colapse.html', context={'config': config}, request=request))


@register.simple_tag(takes_context=True)
def dashboard(context):
    request = context['request']
    config = config_dashboard()
    return mark_safe(render_to_string('duck_admin/dashboard.html', context={'config': config}, request=request))