import chardet

#Arg number 
def _Option_filter(option, data, row):
    try:
        if option == '1':
            if chardet.detect(''.join(data['data'][row]['attributes']['names'][0]).encode())['encoding'] == 'utf-8':
                return True
        if option == '2':
            if chardet.detect(''.join(data['data'][row]['attributes']['names'][0]).encode())['encoding'] == 'utf-8' or data['data'][row]['attributes']['type_extension'] == 'eml':
                return True
        if option == '3':
                return True
            
    except Exception as e:
        return False
