from flask_table import Table, Col, LinkCol

class Books1(Table):
    Title = Col('Title')
    Author = Col('Author')
    BookID = Col('BookID', show=False)
    
