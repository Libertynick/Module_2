password = []
def get_password (n):

    for i in range(1,n):
        #print(i)

        for j in range(1,n):
            if i < j:
                if n % (i + j) == 0:
                    password.append(i)
                    password.append(j)
n = int(input('Введите любое число в первую каменную вставку от 3 до 20: '))
get_password(n)
print ('')
print('Инди,получилось! Мы нашли пароль! Введи его во вторую каменную вставку', password)
