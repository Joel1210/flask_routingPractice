# flask_routingPractice
run in localhost 5000/play/&lt;num>/&lt;color> 


Simple app to play around with routing.
Run app in virtual environment with flask. 
In project folder, run: python server.py

http://localhost:5000/play/ --> displays 3 boxes in default color.

http://localhost:5000/play/<number> --> displays <number> amount of boxes in default color.

http://localhost:5000/play/<number>/<color> --> displays <number> amount of <color> boxes. (assuming <color> is valid CSS)
