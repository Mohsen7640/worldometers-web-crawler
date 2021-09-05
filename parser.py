class Parser:

    def __init__(self, row):
        self.row = row
        self.get_td_tag = self.row.find_all('td')

    def parse_data(self, index):
        row = self.get_td_tag[index].text
        row = row.replace(' ', '')
        if row and row != 'N/A':
            return row.replace(',', '')
        return 0

    def parse(self):
        data = {
            'row': int(self.parse_data(0)),
            'country': self.parse_data(1),
            'total_cases': int(self.parse_data(2)),
            'new_cases': int(self.parse_data(3)),
            'total_deaths': int(self.parse_data(4)),
            'new_deaths': int(self.parse_data(5)),
            'total_recovered': int(self.parse_data(6)),
            'new_recovered': int(self.parse_data(7)),
            'active_cases': int(self.parse_data(8)),
            'serious_critical': int(self.parse_data(9)),
            'tot_cases': float(self.parse_data(10)),
            'deaths': float(self.parse_data(11)),
            'total_tests': int(self.parse_data(12)),
            'tests': int(self.parse_data(13)),
            'population': int(self.parse_data(14)),
        }
        return data
