#!/bin/bash
# Obtain these keys from the Telstra Developer Portal
CONSUMER_KEY="Agl2rsjQ0fbLC1xqPGDNve2Oianci7wK"
CONSUMER_SECRET="eWJoCzsYcTk2ITRl"
curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "grant_type=client_credentials&client_id=$CONSUMER_KEY&client_secret=$CONSUMER_SECRET&scope=NSMS" \
  'https://tapi.telstra.com/v2/oauth/token'