import re
def solution(new_id):
    answer = ''
    #print(new_id)
    #1
    new_id = new_id.lower()
    #2
    il=''
    # for i in new_id:
    #     #isalnum()
    #     if i.isdigit or i.isalpha or i in ['-','_','.']:
    #         il+=i
    #new_id= il
            
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)

    #3

    new_id = re.sub(r'\.\.+', '.', new_id)
    #4
    new_id=new_id.strip('.')
    print(new_id)
    #5
    if new_id=='':
        new_id='a'
    #6
    if len(new_id)>=16:
        new_id=new_id[:15]
        new_id=new_id.strip('.')
    #7
    while len(new_id)<=2:
        new_id+=new_id[-1]
    
    #print(new_id)

    
    return new_id