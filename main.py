import kivy.app
import kivy.uix.gridlayout
import kivy.uix.boxlayout
import kivy.uix.button
import kivy.uix.textinput
import kivy.uix.label
import kivy.graphics
import numpy
import pygad

import threading

class PygadThread(threading.Thread):
    
    def __init__(self, app, ga_instance):
        super().__init__()
        self.ga_instance = ga_instance
        self.app = app

    def run(self):
        self.ga_instance.run()
        self.ga_instance.plot_result()

class BuzzleApp(kivy.app.App):

    old_best_sol_fitness = -1
    old_best_sol_idx = -1

    def start_ga(self, *args):

        if (not ("pop_created" in vars(self)) or (self.pop_created == 0)):
            print("No Population Created Yet. Create the initial Population by Pressing the \"Initial Population\" Button in Order to Call the initialize_population() Method At First.")
            self.num_attacks_Label.text = "Press \"Initial Population\""
            return

        pygadThread = PygadThread(self, self.ga_instance)
        pygadThread.start()

    def initialize_population(self, *args):
        self.num_solutions = 100
        # print("Number of Solutions within the Population : ", self.num_solutions)

        self.reset_board_text()

        self.population_1D_vector = numpy.zeros(shape=(self.num_solutions, 8)) # Each solution is represented as a row in this array. If there are 5 rows, then there are 5 solutions.

        # Creating the initial population RANDOMLY as a set of 1D vectors.
        for solution_idx in range(self.num_solutions):
            initial_queens_y_indices = numpy.random.rand(8)*8
            initial_queens_y_indices = initial_queens_y_indices.astype(numpy.uint8)
            self.population_1D_vector[solution_idx, :] = initial_queens_y_indices

        self.vector_to_matrix()

        # print("Population 1D Vectors : ", self.population_1D_vector)
        # print("Population 2D Matrices : ", self.population)

        self.pop_created = 1 # indicates that the initial population is created in order to enable drawing solutions on GUI.
        self.num_attacks_Label.text = "Initialized"

        self.ga_instance = pygad.GA(num_generations=200,
                                    num_parents_mating=50,
                                    fitness_func=fitness,
                                    num_genes=8,
                                    initial_population=self.population_1D_vector,
                                    mutation_percent_genes=0.01,
                                    mutation_type="random",
                                    mutation_num_genes=1,
                                    mutation_by_replacement=True,
                                    random_mutation_min_val=0.0,
                                    random_mutation_max_val=8.0,
                                    on_generation=on_gen_callback,
                                    delay_after_gen=0.2)

    def vector_to_matrix(self):
        # Converts the 1D vector solutions into a 2D matrix solutions represrnting the board, where 1 means a queen exists. The matrix form of the solutions makes calculating the fitness value much easier.

        self.population = numpy.zeros(shape=(self.num_solutions, 8, 8))

        solution_idx = 0
        for current_solution in self.population_1D_vector:
            # print(self.population_1D_vector[solution_idx, :])
            current_solution = numpy.uint8(current_solution)
            row_idx = 0
            for col_idx in current_solution:
                self.population[solution_idx, row_idx, col_idx] = 1
                row_idx = row_idx + 1
            # print(self.population[solution_idx, :])
            solution_idx = solution_idx + 1

    def reset_board_text(self):
        # Reset board on GUI.
        for row_idx in range(self.all_widgets.shape[0]):
            for col_idx in range(self.all_widgets.shape[1]):
                self.all_widgets[row_idx, col_idx].text="[color=ffffff]"+str(row_idx)+", "+str(col_idx)+"[/color]"
                with self.all_widgets[row_idx, col_idx].canvas.before:
                    kivy.graphics.Color(0, 0, 0, 1)  # green; colors range from 0-1 not 0-255
                    self.rect = kivy.graphics.Rectangle(size=self.all_widgets[row_idx, col_idx].size, pos=self.all_widgets[row_idx, col_idx].pos)
                    self.all_widgets[row_idx, col_idx].font_size = 20
                    self.all_widgets[row_idx, col_idx].canvas.ask_update()
        self.gridLayout.do_layout()

    def update_board_UI(self, *args):
        if (not ("pop_created" in vars(self)) or (self.pop_created == 0)):
            print("No Population Created Yet. Create the initial Population by Pressing the \"Initial Population\" Button in Order to Call the initialize_population() Method At First.")
            # self.num_attacks_Label.text = "Press \"Initial Population\""
            return

        _, max_fitness, best_sol_idx = self.ga_instance.best_solution()
        best_sol = self.population[best_sol_idx, :].copy()

        # self.num_attacks_Label.text = "Max Fitness = " + str(numpy.round(max_fitness, 4))
        self.num_attacks_Label.text = str(self.ga_instance.generations_completed) + " " + str(numpy.round(max_fitness, 4))

        if abs(BuzzleApp.old_best_sol_fitness - max_fitness) < 0.001:
            return

        self.reset_board_text()

        for row_idx in range(8):
            for col_idx in range(8):
                if (best_sol[row_idx, col_idx] == 1):
                    self.all_widgets[row_idx, col_idx].text = "[color=22ff22]Queen[/color]"
                    with self.all_widgets[row_idx, col_idx].canvas.before:
                        kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
                        self.rect = kivy.graphics.Rectangle(size=self.all_widgets[row_idx, col_idx].size, pos=self.all_widgets[row_idx, col_idx].pos)
                        self.all_widgets[row_idx, col_idx].font_size = 30
                        self.all_widgets[row_idx, col_idx].canvas.ask_update()
        self.gridLayout.do_layout()

        BuzzleApp.old_best_sol_fitness = max_fitness
        BuzzleApp.old_best_sol_idx = best_sol_idx

    def build(self):
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")

        self.gridLayout = kivy.uix.gridlayout.GridLayout(rows=8, size_hint_y=9)
        self.boxLayout_buttons = kivy.uix.boxlayout.BoxLayout(orientation="horizontal")

        self.boxLayout.add_widget(self.gridLayout)
        self.boxLayout.add_widget(self.boxLayout_buttons)

        # Preparing the 8x8 board.
        self.all_widgets = numpy.zeros(shape=(8,8), dtype="O")

        for row_idx in range(self.all_widgets.shape[0]):
            for col_idx in range(self.all_widgets.shape[1]):
                self.all_widgets[row_idx, col_idx] = kivy.uix.button.Button(text=str(row_idx)+", "+str(col_idx), font_size=20)
                self.all_widgets[row_idx, col_idx].markup = True
                self.gridLayout.add_widget(self.all_widgets[row_idx, col_idx])

        # Preparing buttons inside the child BoxLayout.
        initial_button = kivy.uix.button.Button(text="Initial Population", font_size=15, size_hint_x=2)
        initial_button.bind(on_press=self.initialize_population)

        ga_solution_button = kivy.uix.button.Button(text="Show Best Solution", font_size=15, size_hint_x=2)
        ga_solution_button.bind(on_press=self.update_board_UI)

        start_ga_button = kivy.uix.button.Button(text="Start GA", font_size=15, size_hint_x=2)
        start_ga_button.bind(on_press=self.start_ga)

        self.num_attacks_Label = kivy.uix.label.Label(text="Max Fitness", font_size=30, size_hint_x=2)

        self.boxLayout_buttons.add_widget(initial_button)
        self.boxLayout_buttons.add_widget(ga_solution_button)
        self.boxLayout_buttons.add_widget(start_ga_button)
        self.boxLayout_buttons.add_widget(self.num_attacks_Label)

        return self.boxLayout

def fitness(solution_vector, solution_idx):

    if solution_vector.ndim == 2:
        solution = solution_vector
    else:
        solution = numpy.zeros(shape=(8, 8))

        row_idx = 0
        for col_idx in solution_vector:
            solution[row_idx, int(col_idx)] = 1
            row_idx = row_idx + 1

    total_num_attacks_column = attacks_column(solution)

    total_num_attacks_diagonal = attacks_diagonal(solution)

    total_num_attacks = total_num_attacks_column + total_num_attacks_diagonal

    if total_num_attacks == 0:
        total_num_attacks = 1.1 # float("inf")
    else:
        total_num_attacks = 1.0/total_num_attacks

    return total_num_attacks

def attacks_diagonal(ga_solution):
    total_num_attacks = 0 # Number of attacks for the solution (diagonal only).

    # Badding zeros around the solution board for being able to index the boundaries (leftmost/rightmost coumns & top/bottom rows). # This is by adding 2 rows (1 at the top and another at the bottom) and adding 2 columns (1 left and another right).
    temp = numpy.zeros(shape=(10, 10))
    # Copying the solution board inside the badded array.
    temp[1:9, 1:9] = ga_solution
    # print("Solution Board after Badding : ", temp)

    # Returning the indices (rows and columns) of the 8 queeens.
    row_indices, col_indices = numpy.where(ga_solution == 1)
    # Adding 1 to the indices because the badded array is 1 row/column far from the original array.
    row_indices = row_indices + 1
    col_indices = col_indices + 1

    # print("Column indices of the queens : ", col_indices
    total = 0 # total number of attacking pairs diagonally for each solution.

    for element_idx in range(8):
        x = row_indices[element_idx]
        y = col_indices[element_idx]
        # print("ROW index of the current queen : ", x)
        # print("COL index of the current queen : ", y)

        mat_bottom_right = temp[x:, y:]
        total = total + diagonal_attacks(mat_bottom_right)
        # print("Bottom Right : ", total)

        mat_bottom_left = temp[x:, y:0:-1]
        total = total + diagonal_attacks(mat_bottom_left)
        # print("Bottom Left : ", total)

        mat_top_right = temp[x:0:-1, y:]
        total = total + diagonal_attacks(mat_top_right)
        # print("Top Right : ", total)

        mat_top_left = temp[x:0:-1, y:0:-1]
        total = total + diagonal_attacks(mat_top_left)
        # print("Top Left : ", total)

        total_num_attacks = total_num_attacks + total /2

    return total_num_attacks

def diagonal_attacks(mat):
    if (mat.shape[0] < 2 or mat.shape[1] < 2):
        # print("LESS than 2x2.")
        return 0
    num_attacks = mat.diagonal().sum()-1
    return num_attacks

def attacks_column(ga_solution):
    # For a given queen, how many queens sharing the same coulmn? This is how the fitness value is calculated.

    total_num_attacks = 0 # Number of attacks for the solution (column only).
        
    for queen_y_pos in range(8):
        # Vertical
        col_sum = numpy.sum(ga_solution[:, queen_y_pos])
        if (col_sum == 0 or col_sum == 1):
            col_sum = 0
        else:
            col_sum = col_sum - 1 # To avoid regarding a queen attacking itself.
                
        total_num_attacks = total_num_attacks + col_sum

    return total_num_attacks

def on_gen_callback(ga_instance):
    global buzzleApp
    print("Generation = {gen}".format(gen=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))
    
    buzzleApp.population_1D_vector = ga_instance.population
    buzzleApp.vector_to_matrix()

    buzzleApp.update_board_UI()
    # buzzleApp.gridLayout.export_to_png("gen_"+str(ga_instance.generations_completed)+".png")

from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')

buzzleApp = BuzzleApp()
buzzleApp.title = "PyGAD Plays 8 Queen Puzzle"
buzzleApp.run()
