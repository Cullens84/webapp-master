from flask_table import Table, Col, LinkCol

class Books(Table):
    BookID = Col('BookID', show=False)
    Title = Col('Title')
    Author = Col('Author')
    credId = Col('credId', show=False)
