import json

from fastapi import FastAPI

import requests

import PrepaidCard

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/generateotp')
async def Min_KYC_generate_OTP(entityId:str,mobileNumber:str):
    url = "https://kycuat.yappay.in/kyc/customer/generate/otp"

    payload = json.dumps({ "entityId" : entityId,
                "mobileNumber" : mobileNumber
                })
    headers = {
        'partnerid': "LQXPAYBACK",
        'tenant': "LQXPAYBACK",
        'partnertoken': "Basic TFFYUEFZQkFDSw==",
        'content-type': "application/json",

    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    return response.json()


@app.post("/minkycregister")
async def Min_KYC_Register():
    url = "https://kycuat.yappay.in/kyc/v2/register"

    payload = json.dumps({
     "entityId": "xpayuser01",
     "otp": "383053",
     "channelName": "MIN_KYC",
     "entityType": "CUSTOMER",
     "businessType": "LQFINAJIT",
     "businessId": "xpayuser01",
     "title": "Mr",
     "firstName": "Darsana",
     "middleName": "K",
     "lastName": "Sandeep",
     "gender": "FEMALE",
     "isNRICustomer" : False,
     "isMinor": False,
     "isDependant": False,
     'maritalStatus': "SINGLE",
     "countryCode": "91",
     "employmentIndustry": "INFORMATION_TECHNOLOGY",
     "employmentType": "EMPLOYED",
     "plasticCode": "TYPE1",
     "kitInfo": [
     {
     "kitNo": "100000000589",
     "cardType": "VIRTUAL",
     "cardCategory": "DEBIT",
     "cardRegStatus": "ACTIVE",
     "aliasName": "Darsana Sandeep",
     "fourthLine": "10001"
     }
     ],
     "addressInfo": [
     {
     "addressCategory": "PERMANENT",
     "address1": "F2 AMPA FLATS",
     "address2": "NSK ROAD 2ND STREET",
     "address3": "TNAGAR",
     "city": "CHENNAI",
     "state": "TAMILNADU",
     "country": "INDIA",
     "pinCode": "600028"
     },
     {
     "addressCategory": "COMMUNICATION",
     "address1": "F2 AMPA FLATS",
     "address2": "NSK ROAD 2ND STREET",
     "address3": "TNAGAR",
     "city": "CHENNAI",
     "state": "TAMILNADU",
     "country": "INDIA",
     "pinCode": "600028"
     }
     ],
     "communicationInfo": [
     {
     "contactNo": "+919526621880",
     "emailId": "darsanadileep98@gmail.com"
     }
     ],
     "kycInfo": [
     {
     "documentType": "PAN",
     "documentNo": "AQOPN1118C",
     "documentExpiry": "2099-03-01"
     }
     ],
     "dateInfo": [
     {
     "dateType": "DOB",
     "date": "1998-12-07"
     }
     ]
    }

    )
    headers = {
        'partnerid': "LQXPAYBACK",
        'tenant': "LQXPAYBACK",
        'partnertoken': "Basic TFFYUEFZQkFDSw==",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return response.json()


@app.post("/generatetoken")
async def Min_to_Full_KYC_Flow(entityId:str):

    url = "https://kycuat.yappay.in/kyc/customer/generate/token"

    payload = json.dumps({"entityId": entityId})
    headers = {
        'partnerid': "LQXPAYBACK",
        'tenant': "LQXPAYBACK",
        'partnertoken': "Basic TFFYUEFZQkFDSw==",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return response.json()


@app.post("/fullkyc")
async def Fill_KYC_Register_customer():
    import requests

    url = "https://kycuat.yappay.in/kyc/v3/register"

    payload = json.dumps({"customerKycStatus": "FULL_KYC",
                "entityId": "xpaydar01",
                "entityType": "CUSTOMER",
                "businessId": "xpaydar01",
                "businessType": "BUSINESS",
                "title": "Mrs",
                "firstName": "Darsana",
                "lastName": "Sandeep",
                "isMinor": False,
                "isNRICustomer": False,
                "isDependant": False,
                "countryCode": "91",
                "maritalStatus": "SINGLE",
                "middleName": "K",
                "gender": "FEMALE",
                "parentEntityId": "testparent01",
                "plasticCode": "TYPE1",
                "kitInfo": [ {
                    "kitNo": "100000000589",
                    "cardType": "VIRTUAL",
                    "cardCategory": "DEBIT",
                    "cardRegStatus":"ACTIVE",
                    "aliasName": "Naren Viswanath",
                    "fourthLine": "10001"
                        }],
               "kycInfo": [ {
                   "documentType": "PAN",
                   "documentNo": "AQOPN11111",
                   "documentExpiry": "2099-03-01"
                        } ],
               "dateInfo": [{
                   "dateType": "DOB",
                   "date": "1994-02-05"
                        }],
               "communicationInfo": [{
                   "contactNo": "+919526621880",
                   "emailId": "darsanadileep98@gmail.com"
                              }],
               "addressInfo": [{
                   "addressCategory": "PERMANENT",
                   "address1": "F2 AMPA FLATS",
                   "address2": "NSK ROAD 2ND STREET",
                   "address3": "TNAGAR",
                   "city": "CHENNAI",
                   "state": "TAMILNADU",
                   "country": "INDIA",
                   "pinCode": "600028"
                               },
                   {"addressCategory": "COMMUNICATION",
                    "address1": "F2 AMPA FLATS",
                    "address2": "NSK ROAD 2ND STREET",
                    "address3": "TNAGAR",
                    "city": "CHENNAI",
                    "state": "TAMILNADU",
                    "country":"INDIA",
                    "pinCode": "600028" }],
               "employmentType": "EMPLOYED",
               "employmentIndustry": "INFORMATION_TECHNOLOGY"})
    headers = {
        'tenant': "LQXPAYBACK",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return response.json()




x = {"entityId": "New1234",
     "channelName": "MIN_KYC",
     "entityType": "CUSTOMER",
     "businessType": "LQXPAYBACK",
     "businessId": "New1234",
     "title": "Mr",
     "otp": "185769",
     "firstName": "Kalyani",
     "middleName": "V",
     "lastName": "J",
     "gender": "MALE",
     "isNRICustomer": False,
     "isMinor": False,
     "isDependant": False,
     "maritalStatus": "SINGLE",
     "countryCode": "91",
     "employmentIndustry": "INFORMATION_TECHNOLOGY",
     "employmentType": "EMPLOYED",
     "plasticCode": "TYPE1",
     "addressInfo": [ {
         "addressCategory": "PERMANENT",
         "address1": "F2 AMPA FLATS",
         "address2": "NSK ROAD 2ND STREET",
         "address3": "TNAGAR",
         "city": "CHENNAI",
         "state": "TAMILNADU",
         "country": "INDIA",
         "pinCode": "600028"       },
         {"addressCategory": "COMMUNICATION",
          "address1": "F2 AMPA FLATS",
          "address2": "NSK ROAD 2ND STREET",
          "address3": "TNAGAR",
          "city": "CHENNAI",
          "state": "TAMILNADU",
          "country": "INDIA",
          "pinCode": "600028"
          } ],
     "communicationInfo": [ {
         "contactNo": "+919566699940",
         "notification": True,
         "emailId": "kesavvel@gmail.com"
     }    ],

     "kitInfo": [{
         "cardType": "PHYSICAL",
         "cardCategory": "PREPAID",
         "cardRegStatus": "ACTIVE",
         "aliasName": "Naren Viswanath"
     }],
     "kycInfo": [{
         "documentType": "PAN",
         "documentNo": "DBZPS3456D",
         "documentExpiry": "2099-03-01"
     }],
     "dateInfo": [{
         "dateType": "DOB",
         "date": "1984-02-05"
     }]
     }



app.include_router( PrepaidCard.router,
                    prefix = "/PrepaidCard",
                    tags = ["Prepaid Card"],
                   )