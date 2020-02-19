import ticketpy
def main():
    location_input = input("Please enter the state code for which you want to search (e.g. GA for Georgia): ")
    month_input = input("Which month do you want to go to a concert? (e.g. 05 May): ")
    day_input = input("Which date do you want to go to a concert? (e.g. 19 for the 19th): ")
tm_client = ticketpy.ApiClient('75HmUlvv8QYL5XJNsvH6b0qDxAU10uwS')
pages = tm_client.events.find(
    classification_name='Hip-Hop',
    state_code='NY',
    #state_code=location_input,
    start_date_time='2020-01-01T01:00:00Z',
    end_date_time='2020-03-02T01:00:00Z'
    #start_date_time='2020-',month_input,'-',day_input,'T01:00:00Z',
    #end_date_time='2020-',month_input,'-',day_input,'T24:00:00Z'
).limit(10)
for event in pages:
    print(event)
    limit(1)