# ініціалізація допоміжних бібліотек, для рандомайзера і будування графіку 
import random
import matplotlib.pyplot as plt

# вхідні данні
default_num_of_series = 16  # кількість серій
default_num_of_coins = 32  # 2048 = кількість монет
default_max_num_of_iterations = 8  # максимальна кількість кидків

def get_points(graph=[[],[]],amount_of_coins=default_num_of_coins, heads=0, depth=0):
    # X-и
    graph[0].append(depth)

    # Y-и
    graph[1].append(amount_of_coins)

    # надрукувати точки в консоль
    print("#" + str(depth), "\tInitial(N):", amount_of_coins, "\t\tDecayed(N'):", heads)


    # якщо мало монет, або вже зробили 8 кидків
    # то вийти з функції і почати будувати графік
    if amount_of_coins <= 1 or depth == default_max_num_of_iterations:
        return graph

    # підкинути всі монети
    samples = [random.randint(1, 2) for i in range(amount_of_coins)]

    # герб, або число ядер, що не розпалися
    tails = samples.count(2)

    # оскільки змінюється лише кількість монет, а не сам алгоритм,
    # ми використовуємо ту саму функцію, для наступної ітераціЇ(кидка)
    # але даємо нові вхідні данні
    return get_points(graph=graph, amount_of_coins=tails, heads=samples.count(1), depth=depth + 1)
    

# для кожної серії викликати функцію get_points, яка підкине монетки,
# порахує координати для графіка
series=[(get_points(graph=[[],[]])) for i in range(default_num_of_series)]
print(series)

# для кожної серії побудувати графік на основі порахованих координат
for i in range(len(series)):
    # x axis values 
    x = series[i][0] 
    # corresponding y axis values 
    y = series[i][1]
  
    # plotting the points  
    plt.plot(x, y, label='серія '+str(i+1)) 
  
# naming the x axis 
plt.xlabel('t') 
# naming the y axis 
plt.ylabel('N') 
  
# giving a title to my graph 
plt.title('Radioactive Decay Model by Andrii F.') 

plt.legend() 

# function to show the plot 
plt.show() 
