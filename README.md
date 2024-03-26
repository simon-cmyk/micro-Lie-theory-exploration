# micro-Lie-theory-exploration
Project for TTK4255 Robotic vision

<video src="manim/media/videos/3Dmanifold/480p15/SphereScene.mp4" width="320" height="240" controls autoplay></video>


## Plan

Det hadde vært kult å vise alle eksemplene i paperet. 
Sola og co har allerede laga python kode `manif`, så man kunne laga litt python notebooks, og kanskje
fått det embedda i ei nettside? Litt sann som i ein blogpost. 
Det går ann gratis via github pages. Der kunne man også hatt ein gjennomgang av teorien.
Referanser og linker videre. Trur det kunne vært veldig kult :bowtie:.
Om man fikk interaktive miljø hadde det kanskje vært det beste, sann man fikk endre på ting. 
Kanskje lage oppgaver med løsning også? 

Ser jo selfølgelig at det her er mykje arbeid, som sikkert vil ta mykje tid. Så bare å være ærlig dersom det blir for mykje jobb.
Tenker uansett at hvis vi begynner med python notebooks så kan vi jo legge på ting etter hvert. Rapporten burde jo også bli
skrevet litt i parallell

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

TODO: I want to test if one can create a requirements.txt

```bash
conda create --name lie_theory --file requirements.txt
```

from the list created by

```bash
conda list -e > requirements.txt
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

We also have used [Bing Copilot](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.microsoft.com/en-us/bing%3Fform%3DMA13FV&ved=2ahUKEwidl6qj_pGFAxWeHBAIHSBwDdcQFnoECAYQAQ&usg=AOvVaw1YqOupLbk8IJ4MfgzJA_wk) in this project seeing that this is the preferred LLM based on NTNUs recommendations. It has created some scripts for visualization and also helped us debugging and understand the concepts in the [paper](https://arxiv.org/pdf/1812.01537.pdf) which we based our project on.

### TODO list

* Add some animations showing the concepts from the paper
* Visualize the examples from manifpy
* Create our own examples from the examples in the paper maybe
* Create a blogpost-ish github pages (usikker på om det er nødvendig)
* Outline the report in Overleaf


