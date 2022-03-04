class Syracuse:

    def __init__(self):

        self.nombre = 0
        

    def suite(self):
       
        l = [self.nombre]

        while (l.count(1) != 4) :

            if self.nombre % 2 == 0:
                self.nombre = self.nombre // 2
                l.append(self.nombre)

            else:
                self.nombre = (self.nombre * 3) + 1
                l.append(self.nombre)

        fichier = open("syracuse.txt", "w")
        fichier.write(str(l))
        fichier.close()

    def lecture(self):
        
        fichier = open("syracuse.txt", "r")
        print(fichier.read())
        fichier.close()

    

    
