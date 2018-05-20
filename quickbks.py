from quickbooks import Oauth2SessionManager, QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.item import Item
import requests

def find_amount(itemName):

    session_manager = Oauth2SessionManager(
        client_id="Q0f8Ef89cjOuj0u6o5kqcCZJ3QSxQd9XI3OHVBKFZ7PhK8rK3m",
        client_secret="O3MpREDHcJawUKgAzgSXbR8XEgbMf41D8U9dWPDE",
        access_token="eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..4KLzE5BZE9nXa7eJnTqEbA.29yuBbA7WrhoWigxRGYvdciQfLgWv2jO3W2wrpZlSHjMJp-zN4F582HOKSsEwOUG87N1koHGmVsqjG8uRG700xb9-msQanXlzkJW7ijr71XlCFbsDRVbk0WhlS7RNn15ZnSzGzoGa1C2so8WFN4tgAw1b-dpXjsSoJibq0q8R0by3xXLDnYwUizLnMuy8WpGrPWpFqmA5OkMhwiO-Z4Wl470hKd2FtSVxvCaRVfzwxPmrEQ4piZ8EJuVgQq_atHvtGS5dsbMZZKvpGt2aKTN84mfJq4rEKedsgtGjH6ti9jdgR1ox5U0ipcZJsS4Jl-sfMnVL3F6Vz5LcFdfT8JCu5nHXK2t0JFarT4K_AHOyqSpkmrH89r0dHIkctTxDuu878SaKD1hLOeTxI0PnIj46EM04Nd1z14L0r5ri6FkNzYyiufPlSimay-b1CMttl4mbaQa66jZsKMLA-lSo3-As5yzoUHZkxgSwhojU2hnUhrT0Rk9x74tRxvblvF4dOOFX4DWliEHApBkGfajWOx4hrzInccZJoI0Wb6mY_6cJ-DqWQ5JR5AWTm4xhIiptmmDOs2orY56fnU90utyWSqK2SCfjqJZ4eA5fE8KxkdK6tWP9-z6-xh1ywrmLCILwt8F75HV5aGznP6YgSLY1Zowt32sw4ZkjoVeWNWdYx1EGQ40yiP4wSCYkV7bwQDMPSl5BAGsiHX3NMFrppoZNKgQ8Xg5UprVU0MGhSglD6PqwXxY53zq79PCU7CCWAPfrjoZvbW4XR-N3rJ48nwsxDw-bH-sN_MdJqvPMebImX5OKxk.u5qxBaXvf6RTaS-XmLLSWQ",
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
        access_token="eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..4KLzE5BZE9nXa7eJnTqEbA.29yuBbA7WrhoWigxRGYvdciQfLgWv2jO3W2wrpZlSHjMJp-zN4F582HOKSsEwOUG87N1koHGmVsqjG8uRG700xb9-msQanXlzkJW7ijr71XlCFbsDRVbk0WhlS7RNn15ZnSzGzoGa1C2so8WFN4tgAw1b-dpXjsSoJibq0q8R0by3xXLDnYwUizLnMuy8WpGrPWpFqmA5OkMhwiO-Z4Wl470hKd2FtSVxvCaRVfzwxPmrEQ4piZ8EJuVgQq_atHvtGS5dsbMZZKvpGt2aKTN84mfJq4rEKedsgtGjH6ti9jdgR1ox5U0ipcZJsS4Jl-sfMnVL3F6Vz5LcFdfT8JCu5nHXK2t0JFarT4K_AHOyqSpkmrH89r0dHIkctTxDuu878SaKD1hLOeTxI0PnIj46EM04Nd1z14L0r5ri6FkNzYyiufPlSimay-b1CMttl4mbaQa66jZsKMLA-lSo3-As5yzoUHZkxgSwhojU2hnUhrT0Rk9x74tRxvblvF4dOOFX4DWliEHApBkGfajWOx4hrzInccZJoI0Wb6mY_6cJ-DqWQ5JR5AWTm4xhIiptmmDOs2orY56fnU90utyWSqK2SCfjqJZ4eA5fE8KxkdK6tWP9-z6-xh1ywrmLCILwt8F75HV5aGznP6YgSLY1Zowt32sw4ZkjoVeWNWdYx1EGQ40yiP4wSCYkV7bwQDMPSl5BAGsiHX3NMFrppoZNKgQ8Xg5UprVU0MGhSglD6PqwXxY53zq79PCU7CCWAPfrjoZvbW4XR-N3rJ48nwsxDw-bH-sN_MdJqvPMebImX5OKxk.u5qxBaXvf6RTaS-XmLLSWQ",
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


#example of how to update the reorder point integrate this into when datarobot does its update daily
#update_reorder_point("Sun Power E20", 4)


#need to also 


