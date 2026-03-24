print(' 🎊🎉Welcome to fruit information🍓🥭🍇🍉 ')
fruit = {
    'apple' : '🍎Apple is a round fruit that can be red, green, or yellow. It is sweet and healthy. People eat apples fresh, in juice, or in desserts',
    'banana' : '🍌Banana is a sweet and soft fruit that is loved by many people. It is yellow when ripe and grows in warm places. Bananas are healthy and give us energy. Many people eat them as a quick and tasty snack.',
    'watermelon' : '🍉Watermelon is a big, green fruit with red, juicy inside. It is sweet and very refreshing, especially in summer. People eat it fresh or in juice.',
    'mango' : '🥭Mango is a sweet and juicy fruit that many people love. It is yellow or orange when ripe and grows in warm countries. Mango is healthy and full of vitamins. People enjoy eating it fresh or in juices.',
    'strawberry' : '🍓Strawberry is a small, red, and sweet fruit. It grows in gardens and farms and is full of vitamins. Many people like to eat strawberries fresh, in desserts, or in juices.',
    'grapes' : '🍇Grapes are small, round fruits that can be green, red, or purple. They are sweet and healthy. People eat them fresh or make juice and jam.',
    'kiwi' : '🥝Kiwi is a small, brown fruit with green inside. It is sour and sweet and full of vitamins. People eat it fresh or in salads and desserts.',
    'pomegranate' : '🤤Pomegranate is a round fruit with many red seeds inside. It is sweet and healthy. People eat the seeds or drink its juice.',
    'orange' : 'Orange is a round, juicy fruit with a bright orange color .It tastes sweet and a little sour ,Oranges are full of vitamin C and are very healthy'
 }
while True:

 print('\nAvailable fruits:')
 for name in fruit:
    print('-',name)

 select = input('Choose a fruit:').lower()
 if select in fruit:
  print(fruit[select])
 else:
   print('❌please choose a fruit form the list') 

 answer = input('do you want to try again(yes/no)').lower()
 if answer == 'no':
   print('Than kyou💫')
   break





































