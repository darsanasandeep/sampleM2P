import json
from fastapi import FastAPI, APIRouter
import requests
router = APIRouter()


@router.get("/generateotp")
async def Geberate_OTP_Customer_Registration(phone:str):

    url = f"https://sit-secure.yappay.in/Yappay/otp-manager/generate/+91{phone}"

    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return response.json()



@router.post("/registercustomer")
async def PrepaidCard_register_customer():

    url = "https://sit-secure.yappay.in/Yappay/registration-manager/v3/register"

    payload = json.dumps(
        {
            "entityId": "xpayuser001",
            "entityType": "CUSTOMER",
            "businessType": "BUSINESS",
            "businessId": "+919526621880",
            "countryofIssue": "IND",
            "cardType": "P",
            "kitNo": "50119990007",
            "title": "Mr",
            "firstName": "TEST",
            "lastName": "CUSTOMER",
            "gender": "M",
            "specialDate": "1999-09-29",
            "contactNo": "+919526621880",
            "emailAddress": "darsanadileep98@gmail.com",
            "address": "my address, my street",
            "address2": "my locality",
            "city": "mycity",
            "state": "mystate",
            "country": "India",
            "pincode": "600000",
            "idType": "TEST_AADHAAR",
            "idNumber": "1234500001",
            "idExpiry": "2020-12-12",
            "eKycRefNo": "12345678",
            "kycStatus": "FULL_KYC",
            "countryCode": "12345",
            "programType": " BUSINESS ",
            "otp": "555126",
            "documents": [
                {
                    " docType ": "PAN",
                    " docNo ": "ADOPA89013",
                    "docExpDate": None

                },
                {
                    " docType ": "PASSPORT",
                    " docNo ": "ADOPA89013",
                    " docExpDate ": "2025-12-12"}
            ],
            "addressDto": {
                "contactNo1": "+919677109523",
                "contactNo2": "+919236634491",
                "emailAddress1": "TEst@m2p.in",
                "emailAddress2": "Test.1@gmail.com",
                "notification": "1010",
                "address": [{
                    "title": "PERMANENT",
                    "address1": "Plot 23&23, AG1, Vidhya Apts,",
                    "address2": "Vidhya nagar 2nd St",
                    "address3": "Ullagaram",
                    "city": "Chennai",
                    "state": "TamilNadu",
                    "country": "India",
                    "pinCode": "600091"
                }
                ]
            }
        }

    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()


@router.post('/loadcustomercard')
async def Prepaidcard_load_customer_card():
    url = "https://sit-secure.yappay.in/Yappay/txn-manager/create"

    payload = json.dumps(
        {
            "toEntityId": "New1234",
            "fromEntityId": "LQXPAYBACK01",
            "yapCode": "1234",
            "productId": "GENERAL",
            "description": "transferfunds",
            "amount": 10.00,
            "transactionType": "M2C",
            "business": "LQXPAYBACK",
            "businessEntityId": "LQXPAYBACK",
            "transactionOrigin": "MOBILE",
            "externalTransactionId": "LQXPAYBACK_REVERSE_99"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()

@router.post("/debitfromcustomer")
async def Debit_from_Customer():
    url = "https://sit-secure.yappay.in/Yappay/txn-manager/create/direct"

    payload = json.dumps(
        {
            "toEntityId": "LQXPAYBACK01",
            "fromEntityId": "New1234",
            "productId": "GENERAL",
            "description": "Change",
            "amount": 10,
            "transactionType": "C2M",
            "transactionOrigin": "MOBILE",
            "businessType": " LQXPAYBACK ",
            "businessEntityId": " LQXPAYBACK ",
            "externalTransactionId": " LQXPAYBACK_REVERSE_99"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()

@router.post("/addcard")
async def Prepaidcard_Add_Card():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/addCard"

    payload = json.dumps(
        {
            "entityId": "New1234",
            "kitNo": "552000297",
            "cardType": "V",
            "business" : "LQVEGAPAY"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()

@router.post("/getcvv")
async def Get_CVV():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/generateCVV"

    payload = json.dumps(
        {
            "entityId": " Test123",
            "kitNo": "0000006000591",
            "expiryDate": "1021",
            "dob": "09031993"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()


@router.get('/fetchbalance')
async def fetch_balance():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/fetchbalance/{entityId}"

    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return response.json()

@router.post("/getcarddetails")
async def Get_Card_Details():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/getCardList"

    payload = json.dumps(
        {
            "entityId": "E12345678"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()


@router.get("/transactionstatus")
async def Transactions_Status_by_External_Id(extTrxId:str):
    url = f"https://sit-secure.yappay.in/Yappay/txn-manager/fetch/{extTrxId}"

    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return response.json()

@router.post('/blockunblock')
async def block_unblock_card():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/block"

    payload = json.dumps(
        {
            "entityId": "New1234",
            "flag": "L",
            "kitNo": "0000006000591",
            "reason": "lock for safety"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return response.json()

@router.post("/blockcustomer")
async def Block_Customer():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/updateentity"

    payload = json.dumps(
        {
            "entityId": "6992ef5e-9eef-4374-8245-b8540b9812ce",
            "isBlocked": "true"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


@router.get("/fetchtransaction")
async def Fetch_Transaction(entityId:str):
    url = f"https://sit-secure.yappay.in/Yappay/txn-manager/fetch/success/entity/{entityId}"

    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


@router.post("/updatecustomer")
async def Update_Customer():
    import requests

    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/updateentity"

    payload = json.dumps(
        {

            "entityId": "200990010005",
            "contactNo": "+931111111111",
            "emailAddress": "santhosprabahar@gmail.com",
            "addressDto": {
                "address": [{
                    "title": "RESIDENTIAL_PRIMARY",
                    "address1": "3e,Jai Durgai Nagar,Gobichettipalayam",
                    "address2": "adsda",
                    "city": "Erode",
                    "state": "Balkh",
                    "country": "Afghanistan",
                    "pinCode": "111111"
                }]
            }
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


@router.post("/setpin")
async def Set_Pin():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/setPin"

    payload = json.dumps(
        {
            "entityId": "MyCust001",
            "pin": "JtJqooZOO4AtJsYewMHr+CeRxOcQr59+7A/1AgWTFiQ=",
            "kitNo": "000000000001",
            "expiryDate": "1021",
            "dob": "09031993"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()


@router.post('/updatekyc')
async def update_kyc_status():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/addKycDetails"

    payload = json.dumps(
        {
            "entityId": "cor",
            "idType": "PAN",
            "idNumber": "G13PS6412M",
            "kycType": "FULL",
            "registeredDate": "2019-12-01",
            "description": "full to partial"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()


@router.post("/cardreplace")
async def Card_Replacement():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/replaceCard"

    payload = json.dumps(
        {
            "entityId": "MyCust001",
            "oldKitNo": "000000000001",
            "newKitNo": "000000000002"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()

@router.post("/custpreferences")
async def Customer_Preferences():
    import requests

    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/updatePreferenceExternal"

    payload = json.dumps(
        {
            "entityId": "1110000001",
            "status": "NOTALLOWED",
            "type": "CONTACTLESS"
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()

@router.post("/translimit")
async def Customer_Transaction_Limit():
    url = "https://sit-secure.yappay.in/Yappay/business-entity-manager/setPreferences"

    payload = json.dumps(
        {
            "entityId": "VIJAYSS",
            "limitConfig": {
                "txnType": "ATM",
                "dailyLimitValue": "1000"
            }
        }
    )
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

