#!/bin/bash
# Use the Messaging API-v2 to send an SMS
# Note: only to: and body: are required
AccessToken="P7SSpHslutrWrFb6fPUI4PpuG5Cm"
Dest="0430853885"
curl -X POST -H "Authorization: Bearer $AccessToken" -H "Content-Type: application/json" -d "{ "to":"$Dest", "body":"Test Message", "validity": 5, "scheduledDelivery": 1, "notifyURL": "", "replyRequest": false }" "https://tapi.telstra.com/v2/messages/sms"