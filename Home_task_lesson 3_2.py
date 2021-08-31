def private_info(name, surname, birthday, place_of_birthday, email, phone_number):
    return f'Name - {name}, Surname - {surname}, Birthday - {birthday}, Place_of_birthday - {place_of_birthday} ;' \
           f' email - {email}, phone_number - {phone_number}'


print(private_info(name='Kate', surname='Smith', birthday='12.05.2001', place_of_birthday='New York',
                   email='KateSmith@gmail.com', phone_number='439-125-65-98'))
