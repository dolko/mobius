#!/bin/bash
curl -X POST \
  https://tapi.telstra.com/v2/messages/provisioning/subscriptions \
  -H 'authorization: Bearer P8V90YQTGP5SFAKItQ3UXSeNoth3' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "activeDays":30,
  "notifyURL":"http://example.com/callback",
  "callbackData":
  {
    "anything":"some data"
  }
}'