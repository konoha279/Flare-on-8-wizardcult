from os import pardir
from re import I
import socket, time

############################ Configuration ############################
HOST = '127.0.0.1' #irc server
PORT = 6667 #port
NICK = 'dung3onm4st3r13'
USERNAME = 'dung3onm4st3r13'
REALNAME = 'dung3onm4st3r13'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
############################ RAW DATA ############################
data_temp1 = ' what is your quest?'
data_temp2 = ' welcome to the party.'

potion_temp1=' you have learned how to create the Potion of Acid Resistance. To brew it you must combine magnifying glass, kernels of grain, silver spoon, fish tail, undead eyeball, undead eyeball, coal, ash, silver rod, gold-inlaid vial, rose petals, silver rod, honeycomb, phosphorus, undead eyeball, kernels of grain, tarts, bone, undead eyeball, coal, undead eyeball, tentacle of giant octopus or giant s'
potion_temp2= 'quid, glass sliver, honeycomb, rose petals, pearl, snaketongue, undead eyeball, adamantine, bone, undead eyeball, tentacle of giant octopus or giant squid, focus, polished marble stone, gum arabic, an item distasteful to the target, mistletoe sprig, undead eyeball, kernels of grain, reed, bone, undead eyeball, ice, crystal bead, an item distasteful to the target, mistletoe sprig, gum arabic, an it'
potion_temp3= 'em distasteful to the target, mistletoe sprig, undead eyeball, kernels of grain, caterpillar cocoon, bone, undead eyeball, adamantine, silk square, gum arabic, an item distasteful to the target, fur of bat, undead eyeball, kernels of grain, sulfur, bone, undead eyeball, adamantine, feather of owl, crystal bead, glass sliver, fur of bat, undead eyeball, kernels of grain, spheres of glass, bone, und'
potion_temp4= 'ead eyeball, adamantine, feather of owl, chalks and inks infused with precious gems, glass sliver, fur of bat, undead eyeball, kernels of grain, cork, bone, undead eyeball, tentacle of giant octopus or giant squid, fur, pearl, polished marble stone, sweet oil, fur of bat, undead eyeball, kernels of grain, silver cage, bone, bone, bone, sponge, kernels of grain, adder\'s stomach, fish tail, undead e'
potion_temp5= 'yeball, undead eyeball, jade dust, focus, polished marble stone, gum arabic, an item distasteful to the target, mistletoe sprig, earth, herbs, moonseeds, pearl, snaketongue, herbs, undead eyeball, kernels of grain, reed, bone, undead eyeball, undead eyeball, undead eyeball, adamantine, ivory portal (miniature), honeycomb, phosphorus, herbs, undead eyeball, rotten egg, bone, bone, bone, rope, kerne'
potion_temp6= 'ls of grain, jewel-encrusted dagger, fish tail, undead eyeball, undead eyeball, rotten egg, crystal bead, an item distasteful to the target, mistletoe sprig, gum arabic, an item distasteful to the target, mistletoe sprig, earth, herbs, moonseeds, pearl, snaketongue, herbs, undead eyeball, kernels of grain, caterpillar cocoon, bone, undead eyeball, undead eyeball, undead eyeball, adamantine, ivory '
potion_temp7= 'portal (miniature), honeycomb, phosphorus, herbs, undead eyeball, rotten egg, bone, bone, bone, tears, kernels of grain, clay and water, spider, undead eyeball, undead eyeball, food morsel, quiver, butter, moonseeds, phosphorus, niter, silk square, gum arabic, an item distasteful to the target, undead eyeball, kernels of grain, sulfur, bone, undead eyeball, kernels of grain, gem as powder, bone, b'
potion_temp8= 'one, silk square, kernels of grain, clay pot of grave dirt, fish tail, undead eyeball, undead eyeball, fish tail, silk square, gum arabic, an item distasteful to the target, undead eyeball, kernels of grain, gem as powder, bone, undead eyeball, tentacle of giant octopus or giant squid, undead eyeball, fish tail, chalks and inks infused with precious gems, snaketongue, snaketongue, undead eyeball, '
potion_temp9= 'adamantine, bone, undead eyeball, fish tail, earth, honeycomb, mistletoe sprig, undead eyeball, adamantine, bone, undead eyeball, spider, ash, snaketongue, undead eyeball, adamantine, bone, undead eyeball, adamantine, silk square, gold-inlaid vial, polished marble stone, humanoid blood, undead eyeball, adamantine, bone, undead eyeball, rotten egg, focus, polished marble stone, fur of bat, mistleto'
potion_temp10='e sprig, silver rod, an item distasteful to the target, snaketongue, mistletoe sprig, pearl, gold-inlaid vial, polished marble stone, fur of bat, undead eyeball, kernels of grain, ammunition, bone, bone, bone, dust, kernels of grain, tiny piece of target matter, spider, undead eyeball, undead eyeball, soil mixture in a small bag, quiver, butter, moonseeds, phosphorus, niter, focus, polished marble'
potion_temp11= ' stone, fur of bat, mistletoe sprig, silver rod, an item distasteful to the target, snaketongue, mistletoe sprig, pearl, gold-inlaid vial, polished marble stone, undead eyeball, kernels of grain, ammunition, bone, undead eyeball, kernels of grain, flesh, bone, bone, focus, kernels of grain, iron filings or powder, fish tail, undead eyeball, undead eyeball, jade dust, focus, polished marble stone, '
potion_temp12='fur of bat, mistletoe sprig, silver rod, an item distasteful to the target, snaketongue, mistletoe sprig, pearl, gold-inlaid vial, polished marble stone, undead eyeball, kernels of grain, flesh, bone, undead eyeball, ice, undead eyeball, ice, crystal bead, gum arabic, snaketongue, gold-inlaid vial, humanoid blood, herbs, undead eyeball, adamantine, bone, undead eyeball, spider, chalks and inks inf'
potion_temp13='used with precious gems, hot pepper, undead eyeball, adamantine, bone, undead eyeball, spider, chalks and inks infused with precious gems, pebble, undead eyeball, adamantine, bone, undead eyeball, spider, chalks and inks infused with precious gems, stone, undead eyeball, adamantine, bone, undead eyeball, spider, tallow, phosphorus, undead eyeball, adamantine, bone, undead eyeball, adamantine, silk'
potion_temp14=' square, gold-inlaid vial, polished marble stone, humanoid blood, undead eyeball, adamantine, bone, bone, bone, tears, kernels of grain, cloak, spider, undead eyeball, undead eyeball, food morsel, quiver, butter, moonseeds, phosphorus, niter, feather of owl, crystal bead, glass sliver, undead eyeball, kernels of grain, spheres of glass, bone, undead eyeball, kernels of grain, ruby (as dust), bone,'
potion_temp15=' bone, distilled spirits, kernels of grain, black pearl (as crushed powder), fish tail, undead eyeball, undead eyeball, fish tail, feather of owl, crystal bead, glass sliver, undead eyeball, kernels of grain, ruby (as dust), bone, undead eyeball, fish tail, undead eyeball, spider, chalks and inks infused with precious gems, hot pepper, undead eyeball, adamantine, bone, undead eyeball, spider, chal'
potion_temp16='ks and inks infused with precious gems, pebble, undead eyeball, adamantine, bone, undead eyeball, adamantine, earth, honeycomb, mistletoe sprig, honeycomb, undead eyeball, kernels of grain, leather loop, bone, bone, bone, makeup, kernels of grain, gilded acorn, spider, undead eyeball, undead eyeball, tentacle of giant octopus or giant squid, quiver, butter, pearl, polished marble stone, mistletoe '
potion_temp17='sprig, undead eyeball, kernels of grain, leather loop, bone, undead eyeball, adamantine, bone, bone, tears, kernels of grain, alum soaked in vinegar, spider, undead eyeball, undead eyeball, food morsel, quiver, butter, moonseeds, phosphorus, niter, feather of owl, chalks and inks infused with precious gems, glass sliver, undead eyeball, kernels of grain, cork, bone, undead eyeball, kernels of grai'
potion_temp18='n, snakeskin glove, bone, bone, distilled spirits, kernels of grain, cured leather, fish tail, undead eyeball, undead eyeball, fish tail, feather of owl, chalks and inks infused with precious gems, glass sliver, undead eyeball, kernels of grain, snakeskin glove, bone, undead eyeball, fish tail, undead eyeball, spider, chalks and inks infused with precious gems, hot pepper, undead eyeball, adamanti'
potion_temp19='ne, bone, undead eyeball, spider, chalks and inks infused with precious gems, pebble, undead eyeball, adamantine, bone, undead eyeball, adamantine, earth, honeycomb, mistletoe sprig, honeycomb, undead eyeball, kernels of grain, leather loop, bone, bone, bone, salt, kernels of grain, eggshells, spider, undead eyeball, undead eyeball, bitumen (a drop), quiver, butter, moonseeds, phosphorus, niter, f'
potion_temp20='ur, pearl, polished marble stone, sweet oil, undead eyeball, kernels of grain, silver cage, bone, undead eyeball, kernels of grain, flame, bone, bone, pitch, kernels of grain, crystal sphere, fish tail, undead eyeball, undead eyeball, adamantine, fur, pearl, polished marble stone, sweet oil, undead eyeball, kernels of grain, flame, bone, undead eyeball, adamantine, undead eyeball, food morsel, fur'
potion_temp21=', mandrake root, earth, herbs, moonseeds, pearl, snaketongue, herbs, undead eyeball, adamantine, bone, undead eyeball, tentacle of giant octopus or giant squid, fur, mandrake root, feather of owl, herbs, rose petals, undead eyeball, adamantine, bone, undead eyeball, food morsel, feather of owl, mandrake root, earth, herbs, moonseeds, pearl, snaketongue, herbs, undead eyeball, adamantine, bone, und'
potion_temp22='ead eyeball, tentacle of giant octopus or giant squid, feather of owl, mandrake root, feather of owl, herbs, rose petals, undead eyeball, adamantine, bone, bone, bone, fleece, kernels of grain, tarts, undead eyeball, ruby vial, iron, polished marble stone, undead eyeball, bone, undead eyeball, bone, undead eyeball, spider, tentacle of giant octopus or giant squid, coal, undead eyeball, spider, spi'
potion_temp23='der, food morsel, spider, ice, bone, undead eyeball, giant slug bile, undead eyeball, food morsel, undead eyeball, undead eyeball, spider, spider, bone, undead eyeball, spider, undead eyeball, undead eyeball, undead eyeball, spider, spider, adamantine, undead eyeball, spider, bone, undead eyeball, spider, spider, food morsel, spider, ice, undead eyeball, spider, bone, undead eyeball, spider, undea'
potion_temp24='d eyeball, food morsel, undead eyeball, adamantine, spider, ice, bone, undead eyeball, spider, undead eyeball, adamantine, undead eyeball, food morsel, spider, ice, bone, undead eyeball, spider, undead eyeball, food morsel, undead eyeball, spider, spider, ice, bone, bone, tentacle of giant octopus or giant squid, fish tail, undead eyeball, spider, spider, food morsel, spider, ice, bone, undead eye'
potion_temp25='ball, shamrock, undead eyeball, ruby vial, undead eyeball, earth, bone, undead eyeball, spider, undead eyeball, food morsel, fish tail, ice, bone, bone, fish tail, fish tail, fish tail, adamantine, bone, undead eyeball, adamantine, undead eyeball, spider, undead eyeball, spider, bone, undead eyeball, adamantine, undead eyeball, adamantine, undead eyeball, ice, bone, and bone.'

ingredients = potion_temp1 + potion_temp2 + potion_temp3 + potion_temp4 + potion_temp5 + potion_temp6 + potion_temp7 + potion_temp8 + potion_temp9 + potion_temp10 + potion_temp11 + potion_temp12 + potion_temp13 + potion_temp14 + potion_temp15 + potion_temp16 + potion_temp17 + potion_temp18 + potion_temp19 + potion_temp20 + potion_temp21 + potion_temp22 + potion_temp23 + potion_temp24 + potion_temp25
# print(len(ingredients))
############################ Connect IRC Server ############################

print('[+] Socket created |', s)
remote_ip = socket.gethostbyname(HOST)
print('[+] IP address of irc server is:', remote_ip)
s.connect((HOST, PORT))
print('[+] Connected to: ', HOST, PORT)

############################ Register User & Join Dungeon ############################

nick_cr = ('NICK ' + NICK + '\x0d\n').encode()
s.send(nick_cr)
usernam_cr= ('USER user user user :xx2 xx \x0d\n').encode()
s.send(usernam_cr)
while 1:
    data = s.recv(4096).decode('utf-8')
    print(data)
    if data.find('PING') != -1:
        s.send(str('PONG ' + data.split(':')[1] + '\x0d\n').encode())
        print('[!] PONG sent \n')
        break
print("[!] Escaped Ping-Pong check")
s.send('JOIN #dungeon \x0d\n'.encode()) #chanel

############################ Replay Packets ############################
def stage_1():
    dungeon1_1 = ' you enter the dungeon Graf\'s Infernal Disco. It is frightening, virtual, danish, flimsy, gruesome great, dark oppressive, bad, average, virtual, last, more strange, inhospitable, slimy, average, and few dismal..'
    dungeon1_2 =' you encounter a Goblin in the distance. It stares at you imposingly. The beast smells quite foul. What do you do?'
    
    ingredients = potion_temp1 + potion_temp2 + potion_temp3 + potion_temp4 + potion_temp5 + potion_temp6 + potion_temp7 + potion_temp8 + potion_temp9 + potion_temp10 + potion_temp11 + potion_temp12 + potion_temp13 + potion_temp14 + potion_temp15 + potion_temp16 + potion_temp17 + potion_temp18 + potion_temp19 + potion_temp20 + potion_temp21 + potion_temp22 + potion_temp23 + potion_temp24 + potion_temp25

    xuser =''
    index = 0
    bytes_to_send = 398
    dbcheck = ''
    while 1:
        data = s.recv(4096).decode('utf-8')
        print(data)
        if data.find('PING') != -1:
            s.send(str('PONG ' + data.split(':')[1] + '\x0d\n').encode())
            print('[!] PONG sent \n')
        if data.find('I am') != -1:
            xuser= data.split(' ')[6]
            ingredients = xuser + ingredients
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + xuser +data_temp1+'\x0d\n').encode())      
        if data.find('Fossil') != -1:
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + xuser +data_temp2+'\x0d\n').encode()) # welcome to the party
            while(index+bytes_to_send <= len(ingredients)):
                s.send((str('PRIVMSG ' + data.split()[2])+' :' + ingredients[index:index+bytes_to_send] +'\x0d\n').encode())
                dbcheck += ingredients[index:index+bytes_to_send]
                time.sleep(1)
                index += bytes_to_send
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + ingredients[index:len(ingredients)] +'\x0d\n').encode())
            dbcheck += ingredients[index:len(ingredients)]
            if (dbcheck == ingredients):
                print("[+] Done")
            else:
                print("[-] Failed somewhere!!")
        if data.find('Acid Resistance') != -1:
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + xuser +dungeon1_1+'\x0d\n').encode())
            time.sleep(1)
        if data.find('Infernal Disco') != -1:
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + xuser +dungeon1_2+'\x0d\n').encode())
            time.sleep(1)
    s.close()

def stage_2():
    dungeon2_1 = ' you enter the dungeon The Sunken Crypt. It is flimsy, gruesome great, dark oppressive, bad, average, virtual, last, more strange, inhospitable, slimy, average, few dismal, flimsy, dark and gruesome, inhospitable, inhospitable, frightening, last, slimy, nicest, solid, dark oppressive, few dismal, deep subterranean, last, gruesome great, average, gruesome great, average, cruel, damned, common, and bad..'
    dungeon2_2 = ' you encounter a Wyvern in the distance. It stares at you imposingly. The beast sits in the water, waiting for you to approach it. What do you do?'

    ingre2_file = open('ingre2.txt','r')
    ingredients = ingre2_file.read()
    soceror_name = ''
    bytes_to_send = 398
    index = 0
    while 1:
        data = s.recv(4096).decode('utf-8')
        print(data)
        if data.find('PING') != -1:
            s.send(str('PONG ' + data.split(':')[1] + '\x0d\n').encode())
            print('[!] PONG sent \n')

        if data.find('I am') != -1:
            soceror_name = data.split(' ')[6]
            ingredients = soceror_name + ingredients
            print(soceror_name)
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + soceror_name +data_temp1+'\x0d\n').encode()) 

        if data.find('Fossil') != -1:
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + soceror_name +data_temp2+'\x0d\n').encode()) # welcome to the party
            while(index+bytes_to_send <= len(ingredients)):
                s.send((str('PRIVMSG ' + data.split()[2])+' :' + ingredients[index:index+bytes_to_send] +'\x0d\n').encode())
                time.sleep(2)
                index += bytes_to_send
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + ingredients[index:len(ingredients)] +'\x0d\n').encode())
            print("[+] Done")

        if data.find('Potion of Water Breathing') != -1:
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + soceror_name +dungeon2_1+'\x0d\n').encode())
            time.sleep(1)
        
        if data.find('The Sunken Crypt') != -1:
            s.send((str('PRIVMSG ' + data.split()[2])+' :' + soceror_name +dungeon2_2+'\x0d\n').encode())
            time.sleep(1)

#stage_1()

stage_2()

