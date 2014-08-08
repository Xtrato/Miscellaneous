import os
if os.name == 'nt':
    print 'WINDOWS'
if os.name == 'posix':
    shadowFile = open('shad.txt', 'r')
    shadowFileList = shadowFile.readlines()
    shadowFile.close()
    dump = open('dump.txt', 'w')
    for user in shadowFileList:
        if '$' in user:
            print 'The username is: ' + user[0:user.find(':')]
            dump.write('The username is: ' + user[0:user.find(':')] + '\n')
            hashtype = user[user.find(':') + 2]
            count = 0
            for letter in hashtype:
                if letter == '$':
                    count = count + 1
            if hashtype == '1':
                hashtype = 'The hashing algorithm used is: MD5'
                dump.write('The hashing algorithm used is: MD5\n')
            elif hashtype == '2':
                hashtype = 'The hashing algorithm used is: BlowFish'
                dump.write('The hashing algorithm used is: BlowFish\n')
            elif hashtype == '5':
                hashtype = 'The hashing algorithm used is: SHA256'
                dump.write('The hashing algorithm used is: SHA256\n')
            elif hashtype == '6':
                hashtype = 'The hashing algorithm used is: SHA512'
                dump.write('The hashing algorithm used is: SHA512\n')
            else:
                hashtype = 'The hashing algorithm used is Unknown. It has a hash code value of:' + hashtype + '.'
                dump.write('The username is: ' + user[0:user.find(':')] + '\n')
            print hashtype
            delimitercolon = []
            delimiterdolla = []
            count = 0
            for char in user:
                if char == ':':
                    delimitercolon.append(count)
                if char == '$':
                    delimiterdolla.append(count)
                count = count + 1
            print 'The Hash is: ' + user[delimiterdolla[2] + 1:delimitercolon[1]]
            dump.write('The Hash is: ' + user[delimiterdolla[2] + 1:delimitercolon[1]] + '\n')
            print 'The Salt is: ' + user[delimiterdolla[1] + 1:delimiterdolla[2]]
            dump.write('The Salt is: ' + user[delimiterdolla[1] + 1:delimiterdolla[2]] + '\n')
            print 'The password is set to expire in ' + user[delimitercolon[3] + 1:delimitercolon[4]] + ' days.\n\n'
            dump.write('The password is set to expire in ' + user[delimitercolon[3] + 1:delimitercolon[4]] + ' days.\n\n\n')