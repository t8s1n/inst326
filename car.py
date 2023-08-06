class Car:
    """
    A 'Car' class, instances of the class will be able to turn left or right and drive forward.

    Attributes:
          x: references the x coordinate
          y: references the y coordinate
          heading: references the north/south/east/west
    """

    def __init__(self):
        """
        Initializes a new Car object.

        side effects: sets x coordinate, y coordinate, and headings
        """
        self.x = 0
        self.y = 0
        self.heading = "n"  # for north

    def turn(self, direction):
        """
        Changes the direction of the Car

        side effects: changes the value of the heading as the value of direction is declared.
        """
        if direction == 'r':  # to turn right
            if self.heading == 'n':
                self.heading = 'e'
            elif self.heading == 'e':
                self.heading = 's'
            elif self.heading == 's':
                self.heading = 'w'
            elif self.heading == 'w':
                self.heading = 'n'
        elif direction == 'l':  # to turn left
            if self.heading == 'n':
                self.heading = 'w'
            elif self.heading == 'w':
                self.heading = 's'
            elif self.heading == 's':
                self.heading = 'e'
            elif self.heading == 'e':
                self.heading = 'n'
        else:
            print("Wrong Direction")

    def drive(self, distance=1):
        """
        Drive the car

        side effect: the car will drive a distance depending on the distance parameter value.
        """
        if self.heading == 'n':
            self.y += distance
        elif self.heading == 's':
            self.y -= distance
        elif self.heading == 'e':
            self.x += distance
        elif self.heading == 'w':
            self.x -= distance

    def status(self):
        """
        Updates the status of the car

        side effect: prints out the coordinate and heading of the current Car
        """
        print(f"Coordinates: ({self.x}, {self.y})")
        print(f"Heading: {self.heading}")
