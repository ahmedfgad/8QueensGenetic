# 8QueensGenetic
A Python project for optimizing the 8 Queens Puzzle using the Genetic Algorithm implemented in PyGAD.

The project uses the [Kivy cross-platform Python framework](https://github.com/kivy/kivy) for building the GUI of the 8 queens puzzle. The GUI helps to visualize the solutions reached while the genetic algorithm (GA) is optimizing the problem to find the best solution.

For implementing the genetic algorithm, the `PyGAD` library is used. Check its documentation here: https://pygad.readthedocs.io

**IMPORTANT** *If you are coming for the code of the tutorial [8 Queen Puzzle Optimization Using a Genetic Algorithm in Python](https://heartbeat.fritz.ai/8-queen-puzzle-optimization-using-a-genetic-algorithm-in-python-1d9ca769ede8), then it has been moved to the [TutorialProject](https://github.com/ahmedfgad/8QueensGenetic/tree/master/TutorialProject) directory on 17 June 2020.*

# PyGAD Installation

To install [PyGAD](https://pypi.org/project/pygad), simply use pip to download and install the library from [PyPI](https://pypi.org/project/pygad) (Python Package Index). The library lives a PyPI at this page https://pypi.org/project/pygad.

For Windows, issue the following command:

```python
pip install pygad
```

For Linux and Mac, replace `pip` by use `pip3` because the library only supports Python 3.

```python
pip3 install pygad
```

PyGAD is developed in Python 3.7.3 and depends on NumPy for creating and manipulating arrays and Matplotlib for creating figures. The exact NumPy version used in developing PyGAD is 1.16.4. For Matplotlib, the version is 3.1.0.

## Project GUI

The project comes with a GUI built in Kivy, a cross-platform Python framework for building natural user interfaces. Before using the project, install Kivy:

```python
pip install kivy
```

Because the project is built using Python 3, use `pip3` instead of `pip` for Mac/Linux:

```python
pip3 install kivy
```

Check this [Stackoverflow answer](https://stackoverflow.com/a/44220712) to install other libraries that are essential to run Kivy: https://stackoverflow.com/a/44220712

The main file for this project is called `main.py` which holds the code for building the GUI and instantiating PyGAD for running the genetic algorithm. 

After running the `main.py` file successfully, the window will appear as given in the figure below. The GUI uses a GridLayout for creating an 8x8 grid. This grid represents the board of the 8 queen puzzle.

![main](https://user-images.githubusercontent.com/16560492/58335124-2f1e4e00-7e41-11e9-9328-fc3b5cd95f41.jpg)

The objective of the GA is to find the best locations for the 8 queens so that no queen is attacking another horizontally, vertically, or diagonally. This project assumes that no 2 queens are in the same row. As a result, we are sure that no 2 queens will attack each other horizontally. This leaves us to the 2 other types of attacks (vertically and diagonally).

The bottom part of the window has 3 Button widgets and 1 Label widget. From left to right, the description of the 3 Button widgets is as follows:

* The **Initial Population** button creates the initial population of the GA.
* The **Show Best Solution** button shows the best solution in the last generation the GA stopped at.
* The **Start GA** button starts the GA iterations/generations.

The Label widget just prints some informational messages to the user. For example, it prints the fitness value of the best solution when the user presses the **Show Best Solution** button.

## Steps to Use the Project

Follow these steps to use the project:

1. Run the **main.py** file.
2. Press the **Initial Population** Button.
3. Press the **Start GA** Button.

After pressing the **Start GA** button, the GA uses the initial population and evolves its solutions until reaching the best possible solution. 

Behind the scenes, some important stuff was built that includes building the Kivy GUI, instantiating PyGAD, preparing the the fitness function, preparing the callback function, and more. For more information, please check the tutorial titled [8 Queen Puzzle Optimization Using a Genetic Algorithm in Python](https://heartbeat.fritz.ai/8-queen-puzzle-optimization-using-a-genetic-algorithm-in-python-1d9ca769ede8).

## 6 Attacks

After running the `main.py` file and pressing the **Initial Population** button, the next figure shows one possible initial population in which 6 out of 8 queens are attacking each other. 

![1  6 attacks](https://user-images.githubusercontent.com/16560492/58335727-840e9400-7e42-11e9-830d-6d6b9bdad67a.jpg)

In the Label, the fitness value is calculated as `1.0/number of attacks`. In this case, the fitness value is equal to 1.0/6.0 which is 0.1667.

The next figures shows how the GA evolves the solutions until reaching the best solution in which 0 attacks exists.

## 5 Attacks
![2  5 attacks](https://user-images.githubusercontent.com/16560492/58336029-321a3e00-7e43-11e9-860e-99aaf16a1d67.jpg)

## 4 Attacks
![3  4 attacks](https://user-images.githubusercontent.com/16560492/58336030-321a3e00-7e43-11e9-972d-1e948fbd62ee.jpg)

## 3 Attacks
![4  3 attacks](https://user-images.githubusercontent.com/16560492/58336031-321a3e00-7e43-11e9-9b6b-83b9de252186.jpg)

## 2 Attacks
![5  2 attacks](https://user-images.githubusercontent.com/16560492/58336032-32b2d480-7e43-11e9-87d1-48dfdd305cc6.jpg)

## 1 Attack
![6  1 attack](https://user-images.githubusercontent.com/16560492/58336033-32b2d480-7e43-11e9-9626-080f5e922825.jpg)

## 0 Attacks (Optimal Solution)
![7  0 attack](https://user-images.githubusercontent.com/16560492/58336034-32b2d480-7e43-11e9-801d-38bf028c7359.jpg)

## IMPORTANT
It is very important to note that the GA does not guarantee reaching the optimal solution each time it works. You can make changes in the number of solutions per population, the number of generations, or the number of mutations. Other than doing that, the initial population might also be another factor for not reaching the optimal solution for a given trial.

# For More Information

There are different resources that can be used to get started with the building CNN and its Python implementation. 

## Tutorial: 8 Queen Puzzle Optimization Using a Genetic Algorithm in Python

In 1 May 2019, I wrote a tutorial discussing this project. The tutorial is titled [**8 Queen Puzzle Optimization Using a Genetic Algorithm in Python**](https://heartbeat.fritz.ai/8-queen-puzzle-optimization-using-a-genetic-algorithm-in-python-1d9ca769ede8) which is published at Heartbeat. Check it at these links:

- [Heartbeat](https://heartbeat.fritz.ai/8-queen-puzzle-optimization-using-a-genetic-algorithm-in-python-1d9ca769ede8): https://heartbeat.fritz.ai/8-queen-puzzle-optimization-using-a-genetic-algorithm-in-python-1d9ca769ede8

[![Tutorial Cover Image](https://miro.medium.com/max/3240/1*4tHGUbApzoB5rKHIJi9zmg.jpeg)](https://heartbeat.fritz.ai/8-queen-puzzle-optimization-using-a-genetic-algorithm-in-python-1d9ca769ede8)

## Book: Practical Computer Vision Applications Using Deep Learning with CNNs

You can also check my book cited as [**Ahmed Fawzy Gad 'Practical Computer Vision Applications Using Deep Learning with CNNs'. Dec. 2018, Apress, 978-1-4842-4167-7**](https://www.amazon.com/Practical-Computer-Vision-Applications-Learning/dp/1484241665) which discusses neural networks, convolutional neural networks, deep learning, genetic algorithm, and more.

Find the book at these links:

- [Amazon](https://www.amazon.com/Practical-Computer-Vision-Applications-Learning/dp/1484241665)
- [Springer](https://link.springer.com/book/10.1007/978-1-4842-4167-7)
- [Apress](https://www.apress.com/gp/book/9781484241660)
- [O'Reilly](https://www.oreilly.com/library/view/practical-computer-vision/9781484241677)
- [Google Books](https://books.google.com.eg/books?id=xLd9DwAAQBAJ)

![Fig04](https://user-images.githubusercontent.com/16560492/78830077-ae7c2800-79e7-11ea-980b-53b6bd879eeb.jpg)

# Citing PyGAD - Bibtex Formatted Citation

If you used PyGAD, please consider adding a citation to the following paper about PyGAD:

```
@misc{gad2021pygad,
      title={PyGAD: An Intuitive Genetic Algorithm Python Library}, 
      author={Ahmed Fawzy Gad},
      year={2021},
      eprint={2106.06158},
      archivePrefix={arXiv},
      primaryClass={cs.NE}
}
```

# Contact Us

* E-mail: ahmed.f.gad@gmail.com
* [LinkedIn](https://www.linkedin.com/in/ahmedfgad)
* [Amazon Author Page](https://amazon.com/author/ahmedgad)
* [Heartbeat](https://heartbeat.fritz.ai/@ahmedfgad)
* [Paperspace](https://blog.paperspace.com/author/ahmed)
* [KDnuggets](https://kdnuggets.com/author/ahmed-gad)
* [TowardsDataScience](https://towardsdatascience.com/@ahmedfgad)
* [GitHub](https://github.com/ahmedfgad)
