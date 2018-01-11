import cs1graphics as cg
paper = cg.Canvas()

#Create a background

paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('My World')

# Create a sun with the correct coordination
sun = cg.Circle()
paper.add(sun)

sun.setFillColor('yellow')
sun.setRadius(50)
sun.moveTo(700, 100)

# Alternative way to create the same sun
sun2 = cg.Circle(50, cg.Point(700, 100))
sun2.setFillColor('Yellow')
paper.add(sun2)

#Create a house
facade = cg.Square(200, cg.Point(400, 350))
facade.setFillColor('white')
# facade.setDepth(60)
paper.add(facade)

chimney = cg.Rectangle(50, 70, cg.Point(450, 215))
chimney.setFillColor('red')
paper.add(chimney)

tree = cg.Polygon(cg.Point(150, 220),
                  cg.Point(120, 380),
                  cg.Point(180, 380))
tree.setFillColor('darkGreen')
paper.add(tree)


#Create sun rays
sunraySW = cg.Path(cg.Point(660, 140), cg.Point(635, 165))
sunraySW.setBorderColor('yellow')
sunraySW.setBorderWidth(6)
paper.add(sunraySW)

sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765, 165))
sunraySE.setBorderColor('yellow')
sunraySE.setBorderWidth(6)
paper.add(sunraySE)

sunrayNE = cg.Path(cg.Point(740, 60), cg.Point(765, 35))
sunrayNE.setBorderColor('yellow')
sunrayNE.setBorderWidth(6)
paper.add(sunrayNE)

sunrayNW = cg.Path(cg.Point(660, 60), cg.Point(635, 35))
sunrayNW.setBorderColor('yellow')
sunrayNW.setBorderWidth(6)
paper.add(sunrayNW)

# Create grass

grass = cg.Rectangle(800, 300, cg.Point(400, 450))
grass.setFillColor('green')
grass.setBorderColor('green')
grass.setDepth(75) # must be behind house and tree
paper.add(grass)

# Create a window
window =  cg.Rectangle(50, 70, cg.Point(345, 300))
window.setFillColor('black')
window.setBorderColor('red')
paper.add(window)
