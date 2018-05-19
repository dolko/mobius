from quickbooks import Oauth2SessionManager, QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.item import Item
import requests

def find_amount(itemName):

    session_manager = Oauth2SessionManager(
        client_id="Q0f8Ef89cjOuj0u6o5kqcCZJ3QSxQd9XI3OHVBKFZ7PhK8rK3m",
        client_secret="O3MpREDHcJawUKgAzgSXbR8XEgbMf41D8U9dWPDE",
        access_token="eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..5LQKgMk0PWF55FbK4M3gWA.UcCV1GQM-qIXq90Spx3wGqHN10Uw1aOUdQ1DePmT1yoN-Wqr9aGyoq3HM8cX2b9SICFiRNGHywWLyYVbTrwDi5tA1uPVvB5AGqMCSBn8JiD0GGrpliXRTqyilL0wvFdCi-9NNjSC3PfjgfZYZsr6w6n_UW36fR8ssG5EtXWUpVmddkJFPFquzdh6rlUWZXHuxjDse2fxjdbHSlWFGhOddoXMMMSWtgd-gEEX3E6CuePMKp_3XaAmO-NjgFcP-wY1gAvNoU9anBgYBMB-EUp9Vq7LBcXQU4ZL08VLfA_E-E52dCq8mh1pXwcxzoh_5vCVjdDu3CCu3BNRdJIPstLuCMYd0qvId5ktxUdacAwnWVuD7jUCwuAxSa8dZAP7hD_QpntrqZB9-FeQXbd87VZZnu8vkuCUHEKyOZ6RdYXmqkG79EQvz7Iw_z7x8xNpfZUBKCxhxKF6W6QSZO2yd2gbOqtO_gGe2uhgmJjMwXSSlKUtZ9UTqunnYyscUEq7ErGdSkoIFwK2tK-mPLVwwBjHszUPxZRsQoktDHYNhqOTX0C22Mvc_biRPix37YqZVnpd7vcRKSPXuEscPP55xktiYej3xWXiqVpEEZ27ER25GlYWVcy6jgUUohshowx_umsVKmRk_jF6LN3uQNZI2gglcsaSBd_5_bl4vDJk8UkJ8-PBKuwG9vi-9LxQI3MjPUX5yna7H1sf8LAwyWe5t9pb6H18bW3MNtEzme_3Rf8gsaQo_RNj1K06ffm2_o6Uh__rxqFLGJagiukrUXUr06A4lwA72pjd38w9EICq8dTit7M.Tpci8WQ5PRrs_Zi4hfj7ng",
    )

    client = QuickBooks(
        sandbox=True,
        session_manager=session_manager,
        company_id="123146067411789"
    )

    items = Item.all(qb=client)

    for item in items:
        if item.Name == itemName:
            if item.QtyOnHand != None:
                return "You currently have " + str(item.QtyOnHand) + " in stock"
            else:
                return "The item you requested does not use a stock count"

    return "Sorry, the item you requested does not have a stock count"

def update_reorder_point(itemName, value):

    session_manager = Oauth2SessionManager(
        client_id="Q0f8Ef89cjOuj0u6o5kqcCZJ3QSxQd9XI3OHVBKFZ7PhK8rK3m",
        client_secret="O3MpREDHcJawUKgAzgSXbR8XEgbMf41D8U9dWPDE",
        access_token="eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..5LQKgMk0PWF55FbK4M3gWA.UcCV1GQM-qIXq90Spx3wGqHN10Uw1aOUdQ1DePmT1yoN-Wqr9aGyoq3HM8cX2b9SICFiRNGHywWLyYVbTrwDi5tA1uPVvB5AGqMCSBn8JiD0GGrpliXRTqyilL0wvFdCi-9NNjSC3PfjgfZYZsr6w6n_UW36fR8ssG5EtXWUpVmddkJFPFquzdh6rlUWZXHuxjDse2fxjdbHSlWFGhOddoXMMMSWtgd-gEEX3E6CuePMKp_3XaAmO-NjgFcP-wY1gAvNoU9anBgYBMB-EUp9Vq7LBcXQU4ZL08VLfA_E-E52dCq8mh1pXwcxzoh_5vCVjdDu3CCu3BNRdJIPstLuCMYd0qvId5ktxUdacAwnWVuD7jUCwuAxSa8dZAP7hD_QpntrqZB9-FeQXbd87VZZnu8vkuCUHEKyOZ6RdYXmqkG79EQvz7Iw_z7x8xNpfZUBKCxhxKF6W6QSZO2yd2gbOqtO_gGe2uhgmJjMwXSSlKUtZ9UTqunnYyscUEq7ErGdSkoIFwK2tK-mPLVwwBjHszUPxZRsQoktDHYNhqOTX0C22Mvc_biRPix37YqZVnpd7vcRKSPXuEscPP55xktiYej3xWXiqVpEEZ27ER25GlYWVcy6jgUUohshowx_umsVKmRk_jF6LN3uQNZI2gglcsaSBd_5_bl4vDJk8UkJ8-PBKuwG9vi-9LxQI3MjPUX5yna7H1sf8LAwyWe5t9pb6H18bW3MNtEzme_3Rf8gsaQo_RNj1K06ffm2_o6Uh__rxqFLGJagiukrUXUr06A4lwA72pjd38w9EICq8dTit7M.Tpci8WQ5PRrs_Zi4hfj7ng",
    )

    client = QuickBooks(
        sandbox=True,
        session_manager=session_manager,
        company_id="123146067411789"
    )

    items = Item.all(qb=client)
    founditem = None
    for item in items:
        print(item.Name)
        if item.Name == itemName:
            founditem = item
            break

    if founditem != None:
        print("found item")
        founditem.ReorderPoint = value
        founditem.save(qb=client)
        return "updated the " + itemName + " to " + str(value)

    return "Sorry, I could not find the item you ask for"

update_reorder_point("Sun Power E20", 4)


