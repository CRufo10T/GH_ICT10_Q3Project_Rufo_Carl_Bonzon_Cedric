from pyscript import display, document

def Play1(e):



    Players = {
     'Jalaine Abdullah',
     'Leona Abeleda',
     'Caleb Arias', 
    'Renzo Arce',
     ' Martina Cajucom',
     'Sean Cotioco',
      'Sang Heon Choi',
     'Phoebe Catimbang',
     'Alejandro Enriquez', 
     'Skyler Escobar',
     'Khloe Espina',
     'Prince Akishino Gano',
      'Calvin Garcia',
     'Simrandip Kaur',
     'Sebastian Chilli Ong', 
     'Carl Joseph Rufo',
     ' Miguel Joaquin Sanchez',
     'Ramon Santos',
      'Allen Daradal',
     'Beatrix Vilale',
     'Deryck Tan', 
     'Harmony Gail Yao',
       'Ivy Zosa',
     'Cedric Bonzon',
    
    }
    document.getElementById("output").innerHTML = ""
    

    

    for num in Players:
        display (num, target='output')

