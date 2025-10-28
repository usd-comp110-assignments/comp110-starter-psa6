import ast
import turtle
import purple_america

def get_style_selection():
    print("Style Options:")
    print("\t(1) red-blue")
    print("\t(2) purple")
    print("\t(3) black-white\n")

    valid = False
    while not valid:
        selection = input("Enter your selection: ")
        try:
            n = int(selection)
            if 1 <= n <= 3:
                valid = True
            else:
                raise ValueError()

        except:
            print("Invalid selection!")

    if n == 1:
        return "red-blue"
    elif n == 2:
        return "purple"
    else:
        return "black-white"

def test_draw_subregion():
    points = [(5, 3), (1, 6), (-3, 1), (-1, -4)]
    t = turtle.Turtle()
    s = turtle.Screen()

    # set screen to zoom in smaller region
    s.setworldcoordinates(-10, -10, 10, 10)
    purple_america.draw_subregion(t, points)

    # don't close window until user clicks on it
    turtle.exitonclick()


def test_draw_filled_subregion():

    valid = False
    while not valid:
        pen_input = input("Enter the pen color: ")
        try:
            pen = ast.literal_eval(pen_input)
            print(pen)
            if not isinstance(pen, str):
                raise ValueError()
            else:
                valid = True
        except:
            print("FAIL: Invalid pen input.")
    
    valid = False
    while not valid:
        fill_input = input("Enter the fill color: ")
        try:
            fill = ast.literal_eval(fill_input)
            print(fill)
            if not isinstance(fill, tuple):
                raise ValueError()
            if len(fill) != 3:
                # check that the tuple has 3 values
                raise ValueError()
            elif False in [isinstance(v, float) for v in fill]:
                # check that all values are integers
                raise ValueError()
            else:
                valid = True
        except:
            print("FAIL: Invalid fill input.")

    points = [(5, 3), (1, 6), (-3, 1), (-1, -4)]
    t = turtle.Turtle()
    s = turtle.Screen()

    # set screen to zoom in smaller region
    s.setworldcoordinates(-10, -10, 10, 10)

    purple_america.draw_filled_subregion(t, points, pen, fill)

    turtle.exitonclick()

def get_literal(prompt):
    while True:
        user_input = input(prompt)
        try:
            parsed_input = ast.literal_eval(user_input.strip())
            return parsed_input
        except:
            print("Invalid input.")

def test_read_subregion():
    f = open("fake_subregions.txt", 'r')


    try:
        # read and display the first fake subregion
        print("\nReading first subregion (Foo Bar)")

        expected_points = [(5.0, 3.0), (1.0, 6.0), (-3.0, 1.0), (-1.0, -4.0)]
        while True:
            expected_points_user = get_literal("Enter the list of expected points: ")

            if expected_points_user != expected_points:
                print("Incorrect list of points entered.")
            else:
                break

        region_name, points = purple_america.read_subregion(f)
        print("region_name:", repr(region_name))
        assert region_name == 'Foo Bar', "FAIL: region name should be exactly: 'Foo Bar'"

        print("points:", points)
        assert points == expected_points, f"FAIL: Expected points to be {expected_points}"

        # read and display the second fake subregion
        print("\nReading second subregion (Meowtopia)")

        expected_points = [(85.0,-9.3), (91.3,-10.7), (100.41,-14.33)]
        while True:
            expected_points_user = get_literal("Enter the list of expected points: ")

            if expected_points_user != expected_points:
                print("Incorrect list of points entered.")
            else:
                break


        region_name, points = purple_america.read_subregion(f)
        print("region_name:", repr(region_name))
        assert region_name  == 'Meowtopia', "FAIL: region name should be exactly 'Meowtopia'"
        print("points:", points)
        assert points == expected_points, f"FAIL: Expected points to be {expected_points}"

    except AssertionError as e:
        print(e)
    else:
        print("Basic tests passed. Check full test results after uploading.")

def test_calculate_colors():
    
    valid = False
    while not valid:
        vote_input = input("Enter the vote count: ")
        try:
            vote = ast.literal_eval(vote_input)
            print(vote)
            if not isinstance(vote, tuple):
                raise ValueError()
            if len(vote) != 3:
                # check that the tuple has 3 values
                raise ValueError()
            elif False in [isinstance(v, int) for v in vote]:
                # check that all values are integers
                raise ValueError()
            else:
                valid = True
        except:
            print("FAIL: Invalid vote input.")
    
    try:
        # test black-white
        print("\nTesting style black-white")
        expected = ('black',(1.0,1.0,1.0))
        while True:
            expected_input = get_literal("Enter expected output: ")

            if expected_input != expected:
                print("Incorrect tuple of colors entered.")
            else:
                break
        
        pen_color, fill_color = purple_america.calculate_colors("black-white",vote)
        print("pen color:", pen_color)
        assert pen_color  == 'black', "FAIL: region name should be exactly 'black'"
        print("fill color:", fill_color)
        assert fill_color == expected[1], f"FAIL: Expected points to be {expected[1]}"

        # test red-blue
        print("\nTesting style red-blue")
        expected = ('white',(1.0,0.0,0.0))
        while True:
            expected_input = get_literal("Enter expected output: ")

            if expected_input != expected:
                print("Incorrect tuple of colors entered.")
            else:
                break
        
        pen_color, fill_color = purple_america.calculate_colors("red-blue",vote)
        print("pen color:", pen_color)
        assert pen_color  == 'white', "FAIL: region name should be exactly 'white'"
        print("fill color:", fill_color)
        assert fill_color == expected[1], f"FAIL: Expected points to be {expected[1]}"

        # test purple
        print("\nTesting style purple")
        expected = ('white',(.53,.05,.42))
        expected_calc = (0.5263157894736842, 0.05263157894736842, 0.42105263157894735)
        while True:
            expected_input = get_literal("Enter expected output: ")

            if expected_input != expected:
                print("Incorrect tuple of colors entered.")
            else:
                break
        
        pen_color, fill_color = purple_america.calculate_colors("purple",vote)
        print("pen color:", pen_color)
        assert pen_color  == 'white', "FAIL: region name should be exactly 'white'"
        print("fill color:", fill_color)
        assert fill_color == expected_calc, f"FAIL: Expected points to be {expected[1]}"

    except AssertionError as e:
        print(e)
    else:
        print("Basic tests passed. Check full test results after uploading.")

def test_get_election_results():
    try:
        expected_results = {'Narnia': (5000, 3500, 40), 'Candy Land': (800,6300,74)}
        while True:
            expected_results_user = get_literal("Enter the expected return value: ")

            if expected_results_user != expected_results:
                print("Incorrect return value entered.")
            else:
                break

        voting_results = purple_america.get_election_results("fake_votes.txt")
        print("voting_results:", voting_results)
        assert voting_results == expected_results, f"FAIL: Expected results to be {expected_results}"
    except AssertionError as e:
        print(e)
    else:
        print("Basic tests passed. Check full test results after uploading")

def test_draw_map():
    style = get_style_selection()

    voting_data = {"Narnia": (5000, 3500, 40), "Candy Land": (800,6300,74)}
    purple_america.draw_map("fantasy_region.txt", voting_data, style)

    try:
        turtle.exitonclick()
    except turtle.Terminator:
        pass
    else:
        print("FAIL: Forgot to call exitonclick")


def main():
    options = {1: test_draw_subregion, 2: test_draw_filled_subregion, 
                3: test_read_subregion, 4: test_calculate_colors, 5: test_get_election_results, 6: test_draw_map}

    for (k, v) in options.items():
        print(f"({k}) {v.__name__[5:]}")

    selection = input("Enter the number of the function to test: ")
    try:
        n = int(selection)
        if n not in options:
            raise ValueError()

        # call the tester function
        options[n]()

    except ValueError:
        print("ERROR: Invalid selection")


if __name__ == "__main__":
    main()
