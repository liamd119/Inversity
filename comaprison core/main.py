from objects import Battery

if __name__ == '__main__':
    type_ = input("Enter path to battery type: ")
    num_of_batteries = int(input("Enter number of batteries: "))
    profit_per_hour = int(input("Enter average profit per hour per battery (the money that the battery will make,"
                                " while the system is in use, excluding charging time.): "))

    batteries = [Battery(type_) for i in range(num_of_batteries)]
    current_cost_per_day = (sum([_.cost_per_day() + _.charge_time * profit_per_hour for _ in batteries]))
    old_outlay = sum([_.purchase_cost for _ in batteries])

    type_ = "our_bat.json"
    batteries = [Battery(type_) for i in range(num_of_batteries)]
    new_cost_per_day = sum([_.cost_per_day() + _.charge_time * profit_per_hour for _ in batteries])
    outlay = sum([_.purchase_cost for _ in batteries])
    print(f"Savings per day: {(current_cost_per_day - new_cost_per_day)}")
    print(f"Time to pay off cost: "
          f"{(outlay / (current_cost_per_day - new_cost_per_day) - old_outlay / (current_cost_per_day - new_cost_per_day))}")
