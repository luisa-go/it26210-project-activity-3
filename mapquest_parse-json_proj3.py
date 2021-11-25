import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ci3HmNJSBN1I6UYPtHDrp3Nhog2fHoVF"
#Notifies the user that they have entered or started the MapQuest
print("Greetings! Welcome to MapQuest. Where do you want to go?")

while True:
    orig = input("Starting Location: ")

    if orig == "quit" or orig == "q":
        #In order to notify the user that they have exitted the MapQuest
        print("Thank you for using MapQuest!")
        break
    dest = input("Destination: ")

    if dest == "quit" or dest == "q":
        #In order to notify the user that they have exitted the MapQuest
        print("Thank you for using MapQuest!")
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.")
        print("\n=============================================")
        print("TRIP DETAILS")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Miles: " + str(json_data["route"]["distance"]))
        print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("\n=============================================")

        print("TRIP DISTANCE")
        print("Kilometers: " +
        str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " +
        str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("\n=============================================")

        print("TRIP NOTES")
        print("Has bridge: ", str(json_data["route"]["legs"][0]["hasBridge"]))
        print("Has Highway: ", str(json_data["route"]["legs"][0]["hasHighway"]))
        print("Has Toll Road: ", str(json_data["route"]["legs"][0]["hasTollRoad"]))
        print("\n=============================================")

        print("DIRECTIONS FOR YOUR DESTINATION")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

            #Displays the time needed until you have reached your destination
            #When the destination has been reached, it will notify you in terminal
            if each["formattedTime"] == "00:00:00":
                print("You have arrived at your destination!")
            else:
                for each2 in json_data["route"]["legs"]:
                    print("Estimated Time of Arrival: ", each["formattedTime"])
                    print('\n')
        
        print("=============================================\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

#Washington, D.C.
#Baltimore, MD