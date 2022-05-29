import time

print('SILLY ICON SWAPPER!')
print('Version: 0.0.1')

iconlist = ['player', 'ship', 'player_ball', 'bird', 'dart', 'robot', 'spider', 'swing']

nk = [3, 3, 3, 4, 3, 13, 13]

icon = str()

for i in enumerate(iconlist):
    mk = str(i)
    mk = mk.replace(", '", ": ")
    mk = mk.strip("')")
    mk = mk.strip("(")
    print(mk)
##dawg i KNOW theres a better way to do this but i wrote this part at like 1am im to lazy
    
iconchoice = int(input("Icon Type: "))

icon = iconlist[iconchoice]

repl = nk[iconchoice]

print('Icon Type Chosen: ' + icon)

if iconchoice == 7:
    print('ERROR: v1.0.0 will include the swing swapper.')
    time.sleep(5)
    quit()

bput = input('1: HD\n2: Regular\n')

if bput == '1':
    b = 9
    ext = '-hd.plist'
if bput == '2':
    b = 6
    ext = '.plist'
if bput > '2':
    print('ERROR: Invalid Choice!')
    time.sleep(5)
    quit()

thing = int(input('Which icon do you want?: '))
otherthing = (input('Which icon do you want to swap it with?: '))

if len(otherthing) < 2:
    otherthing = '0'+ otherthing


##oh hell nah please dont kill me im too lazy to find a better way
if thing > 96 and iconchoice == 0:
    repl = 4
if thing > 25 and iconchoice == 1:
    repl = 4
if thing > 21 and iconchoice == 2:
    repl = 4
if thing > 19 and iconchoice == 3:
    repl = 5
if thing > 28 and iconchoice == 4:
    repl = 4
if thing > 26 and iconchoice == 5:
    repl = 13
if thing == 12 and iconchoice == 6:
    repl = 12
if thing == 14 and iconchoice == 6:
    repl = 12
if thing == 23 and iconchoice == 6:
    repl = 12

file = str(icon) + '_' + str(thing) + ext
output_file = str(icon) + '_' + str(otherthing) + ext

lsdjak = ('icons/' + file + '.bak')

ship = file[:-b]

with open('icons/' + file) as f:
    k = f.read()

with open(lsdjak, 'w') as fbackup:
    fbackup.write(k)

k = k.replace(ship, icon + '_' + otherthing, repl)

with open(output_file, 'w') as f:
    f.write(k)

print(ship + ' has been swapped with ' + 'ship_' + otherthing + '.')
