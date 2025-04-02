height_req = 137
cost_req = 10

input_height = int(input("What is your height?: "))
input_cost = int(input("What is your cost?: "))

if input_height >= height_req and input_cost >= cost_req:
    print("Enjoy the ride!")
elif input_height <= height_req and input_cost >= cost_req:
    print("You are not tall enough to ride")
elif input_height >= height_req and input_cost <= cost_req:
    print("You dont have enough credits")
else:
    print("You have not met either requirement")