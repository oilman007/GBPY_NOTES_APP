from datetime import datetime


class Notes:
    id = 0
    header = ''
    msg = ''
    change_date = None

    def __init__(self, id, header, msg):
        
        self.id = id
        #self.id = Notes.id + 1
        #Notes.id += 1
        self.header = header
        self.msg = msg
        self.change_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def __str__(self):
        details = ''
        details += f'{self.id} '
        details += f'{self.header}; '
        details += f'{self.msg}; '
        details += f'{self.change_date}'
        return details

    def get_id(self):
        return self.id

    def get_header(self):
        return self.header

    def get_msg(self):
        return self.msg

    def get_change_date(self):
        return self.change_date

    def set_id(self, data):
        self.id = data
        return self.id

    def set_header(self, x):
        self.header = x

    def set_msg(self, x):
        self.msg = x

    def set_change_date(self, x):
        self.change_date = x
