import os
os.getcwd()
os.chdir('C:/Python27/Doc/HeadFirstPython/chapter3')
os.getcwd()


if os.path.exists('sketch.text'):
    data = open('sketch.txt')
    for each_line in data:
       if ":" in each_line:
           (role, line_spoken) = each_line.split(':', 1)
           print role,
           print  'said;',
           print line_spoken,
       else:
           pass
else:
    print 'the file is missing'