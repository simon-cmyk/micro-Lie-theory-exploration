# micro-Lie-theory-exploration

Project for TTK4255 Robotic vision

## About

Lie group is said to be

1. Proper: Exact with rigorous calculus on nonlinear spaces.
2. Powerful: In that it can handle uncertainties and be used for complex situations.
3. Abstract: It unifies concepts across implementations. So 2D vs 3D, quaternions and rotation
matrices, and so on.
4. Beautiful :bowtie:

Because of this, it is very useful in robotics applications such as pose state estimation. We therefore
want to delve deeper into the subject to explore some core concepts that help understanding both
concepts from TTK4255 Robotic Vision and later subjects we might encounter during our studies.

![gif example](manim/media/videos/3Dmanifold/480p15/example.gif)

This project delve into the paper by [Sola](http:
//arxiv.org/abs/1812.01537). At the core is the implementation from [manifpy](https://github.com/artivis/manif).

## Structure

We have visualized examples from manifpy (NB. not done the simulation ourselves). These can be found in ́`Localization.ipynb` and `SAM.ipynb`. We also have tried to visualize the mapping between log and exp. Both in the 3d and 2d case. This shows in `exp_and_log_map.ipynb`. Lastly we tried to show a simple use case of lie theory in Interpolating poses, `Interpolation.ipynb`. We also experimented with manim, but it was to difficult and not our main focus. This can be found in the `manim` folder. 



## Setup

I will describe the conda way, you could also use pip. 

```bash
conda create --name lie_theory python=3.9
conda activate lie_theory
```

Now you can activate it. When running the notebooks this is easily done by choosing the kernel in VSCODE.
But first you have to install the packages needed.
In terminal write.

```bash
conda install -c conda-forge manifpy
conda install -c conda-forge ipykernel
conda install -c conda-forge manim
```

This is taken from [this website](https://artivis.github.io/manif/python/index.html). We also based our code from the examples given in [the manif repo](https://github.com/artivis/manif).

In addition you would have to install matplotlib, numpy and transformations3d. This can be done by running the following command in the terminal.

```bash
conda install -c conda-forge matplotlib numpy transformations3d
```

### Working with manim

Here is the link to the [Manim](https://docs.manim.community/en/stable/tutorials/quickstart.html) intro page.

To compile a manim scene

```bash
cd manim
manim -pql scene.py CreateCircle
```

### Credits

| Simon | Emil | Oscar |
| -------- | -------- | -------- |
| [simonlb\@stud.ntnu.no](mailto:simonlb@stud.ntnu.no)  | [emiljohn\@stud.ntnu.no](mailto:emiljohn@stud.ntnu.no)   | [oscarer\@stud.ntnu.no](mailto:oscarer@stud.ntnu.no)   |

We also have used [Bing Copilot](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.microsoft.com/en-us/bing%3Fform%3DMA13FV&ved=2ahUKEwidl6qj_pGFAxWeHBAIHSBwDdcQFnoECAYQAQ&usg=AOvVaw1YqOupLbk8IJ4MfgzJA_wk) and ChatGPT in this project. It has helped in creating some scripts for visualization and also helped us debugging and understand the concepts in the [paper](https://arxiv.org/pdf/1812.01537.pdf) which we based our project on.