name = 'eduardo'
colors = {'clean':'\033[m', 
          'blue':'\033[34m', 
          'yellow':'\033[33m', 
          'blackandwhite':'\033[7:30m'}
print('Hello {}{}{}'.format(colors['yellow'] ,name,colors['clean']))