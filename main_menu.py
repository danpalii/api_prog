import requests

''' Functii definite importate '''
import functions.url_functions as url_f


urls = [
    'https://apidrone.herokuapp.com/api/status_point_detail/1',
    'https://apidrone.herokuapp.com/api/turn_point/1',
    'https://apidrone.herokuapp.com/api/image_list/'
]

first_true_point = True
second_true_point = True




print("Start Drone Program ------------------->")
print('________________________________________________________')
requests.put(urls[0], {"id": 1, "status_point": 1})
print('Status Point ===> 1')
requests.put(urls[1], {"id": 1, "turn_point": 0})
print('Turn Point ===> 0')

print('Execute Menu')

while first_true_point:

    status_point_response = url_f.get_request(urls[0])

    print(status_point_response['status_point'])
    while True:
        turn_point_response = url_f.get_request(urls[1])

        if turn_point_response['turn_point'] == 1:
            print("1 Photo")
        elif turn_point_response['turn_point'] == 2:
            print("2 Sound")
        elif turn_point_response['turn_point'] == 3:
            print("3 Exit")
            break
    break        

requests.put(urls[0], {"id": 1, "status_point": 0})
print('Status Point ===> 0')
requests.put(urls[1], {"id": 1, "turn_point": 0})
print('Turn Point ===> 0')
print('________________________________________________________')
print('Finish Frone Program')
