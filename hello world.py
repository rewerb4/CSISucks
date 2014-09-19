#creating new file for repository
def response(string):
  resp = ''
    if string == 'good':
        resp = 'sweet'
        return resp
    elif string == 'bad':
        resp = 'That sucks hommie'
        return resp
    elif string == 'meh':
        resp = 'time for a drink ;-)'
        return resp
    
    else:
        resp = 'I did ask for that'
        return resp
  
  
print('hello world)
user_input = raw_input('\nHow is your day? Good, Bad, Meh: ').lower()
print (reponse(user_input))
