#!/usr/bin/python3
"""
module to define a base class
"""
import json
import csv


class Base:
    """
    This is the superclass
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation method for id
        """
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that writes the JSON string representation of
        list_objs to a file
        """
        file_name = cls.__name__ + ".json"
        empty_list = []

        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                empty_list.append(json_dict)

        with open(file_name, mode="w") as f:
            json.dump(empty_list, f)

    @staticmethod
    def from_json_string(json_string):
        """
        method that returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        method that returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy_value = Rectangle(3, 5)
        elif cls.__name__ == "Square":
            dummy_value = Square(4)
        dummy_value.update(**dictionary)
        return dummy_value

    @classmethod
    def load_from_file(cls):
        """
        method that returns a list of instances
        """
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="utf-8") as f:
                data = cls.from_json_string(f.read())

        except FileNotFoundError:
            return []

        instances = []
        for instance in data:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            this is my method
        """
        file_name = cls.__name__ + ".csv"

        with open(file_name, mode="w", newline='', encoding="UTF8") as fd:
            write_this = csv.writer(fd, delimiter=" ")

            if cls.__name__ == "Rectangle":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["width"]) + "," +
                               str(item["height"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

            if cls.__name__ == "Square":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["size"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """
            this is my method
        """
        return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            Opens a window and draws all the squares and rectangles
        """
        import turtle

        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("black")
        turtle.color("teal")
        turtle.hideturtle()
        turtle.goto(-300, 300)
        turtle.speed(0)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)

        turtle.exitonclick()
