import pickle
import os
import sys

pickle_in = open('file_path.gsrf', 'r')
path = pickle.load(pickle_in)

try:
    t = open(path, 'r')
    print("________________________________________________________________________")
    print("Compiling " +str(path))
    print("________________________________________________________________________")  
    print ''
except:
    print("Somthing went wrong!")
    print('''It may be this:
1. it has to be a .gs or .txt file!
2. There cant be quotes(") in the path
3. Its not a path''')

try:
    f = open(path +str('.html'), 'w')
    f.write('<html>')
    f.write('\n<head>')
    f.write(' </head>')
    f.write('\n<body>')
except:
    print 'there was an error making ' +str(path+str('.html'))

lines = t.readlines()
line = 0

while True:
    try:
        line_reading = lines[line]
        lineLength = len(line_reading)
    except:
        f.write('\n</body>')
        f.write('\n</html>') 
        os.startfile(path+str('.html'))   
        sys.exit()
    
    if line_reading[0:5] == 'print':
        f.write('\n')
        f.write('<br>'+str(line_reading[6:lineLength]))

    if line_reading[0:5] == 'title':
        f.write('\n')
        f.write('<br>' + '<h1>' +str(line_reading[6:lineLength])+'</h1>')

    if line_reading[0:8] == 'subtitle':
        f.write('\n')
        f.write('<br>' + '<h3>' +str(line_reading[9:lineLength])+'</h3>')

    if line_reading[0:5] == 'image':
        f.write('\n')
        f.write('<img align = "left" src = ' +str(line_reading[6:lineLength])+'>')

    line = line + 1