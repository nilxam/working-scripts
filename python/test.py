#!/usr/bin/env python

username = 'yclin7442@gmail.com'
passwd   = 's96639111'
doc_name = 'Conference registration'

import gdata.docs
import gdata.docs.service
import gdata.spreadsheet.service
import re, os

# Connect to Google
gd_client = gdata.spreadsheet.service.SpreadsheetsService()
gd_client.email = username
gd_client.password = passwd
gd_client.source = 'maxlin.example-1'
gd_client.ProgrammaticLogin()

q = gdata.spreadsheet.service.DocumentQuery()
q['title'] = doc_name
q['title-exact'] = 'true'
feed = gd_client.GetSpreadsheetsFeed(query=q)
spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]
feed = gd_client.GetWorksheetsFeed(spreadsheet_id)
worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

rows = gd_client.GetListFeed(spreadsheet_id, worksheet_id).entry
confirm = 'Yes, I want to be on that mailing list'

for row in rows:
    for key in row.custom:
#        if (row.custom[key].text == confirm):
            print " %s: %s" % (key, row.custom[key].text)
    print
