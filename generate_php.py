import os



def generate_php(url,code):
    f = open(code + '.php', "w+")
    f.write('<?php \n header(\'Location: '+url+'\'); \n ?>')
    f.close()


