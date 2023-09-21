
import requests
import json

class GetPrograms:

    def get_programs(self):
        url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        programs_list = []

        response = requests.get(url)
        if response.status_code == 200:
            programs = json.loads(response.text)
            for program in programs:
                programs_list.append(program["agency"])
        
        return programs_list

if __name__ == "__main__":
    programs = GetPrograms()
    programs_schools = programs.get_programs()

    for school in set(programs_schools):
        print(school)
