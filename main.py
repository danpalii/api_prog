import requests

# urls = [
#     "http://localhost:8000/api/turn_point/1",
#     "http://localhost:8000/api/photo_point/1/"
# ]

# start_while_point = True

# while start_while_point:
#     print("Hello")


def print_function():
    print("Start Make Photo")
    print("3")
    print("2")
    print("1")
    print("Finishing!!")

# http://localhost:8000/api/photo_point/  ---> GET, POST   URL
# http://localhost:8000/api/photo_point/1/ ---> GET , PUT, DELETE   URL
urls = [
    # "https://apidrone.herokuapp.com/api/turn_point/1",
    "http://localhost:8000/api/turn_point/1",
    "http://localhost:8000/api/photo_point/1/"
]

# for n in range(0, 100000000):
#     response = requests.get(urls[0])
#     print(response.json())


while True:
    responseVal = requests.get(urls[0])
    response_var = responseVal.json()
    
    if response_var['turn_point'] == 1:
        print('Start!!!')
        requests.put('http://localhost:8000/api/turn_point/1', data = {'turn_point': 0})
        print_function()
        break  
    print(responseVal.json())




# response.content() # Return the raw bytes of the data payload
# response.text() # Return a string representation of the data payload
# response.json() # This method is convenient when the API returns JSON