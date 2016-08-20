# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bollard"
app_title = "Bollard"
app_publisher = "sagar"
app_description = "Barge & Ships"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "sagarshiragawakar@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bollard/css/bollard.css"
# app_include_js = "/assets/bollard/js/bollard.js"

# include js, css files in header of web template
# web_include_css = "/assets/bollard/css/bollard.css"
# web_include_js = "/assets/bollard/js/bollard.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bollard.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bollard.install.before_install"
# after_install = "bollard.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bollard.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bollard.tasks.all"
# 	],
# 	"daily": [
# 		"bollard.tasks.daily"
# 	],
# 	"hourly": [
# 		"bollard.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bollard.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bollard.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bollard.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bollard.event.get_events"
# }

