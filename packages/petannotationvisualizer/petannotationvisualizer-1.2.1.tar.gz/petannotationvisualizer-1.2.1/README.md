PET Visualizer 
==============
PET Visualizer is a tool for visualizing the [PET Dataset](https://huggingface.co/datasets/patriziobellan/PET)
It is based on tkinter, pygraphviz, and matplotlib packages.

---

This readme file will be updated soon.

---
To install requirements, run the following command in a terminal:

    pip install -r requirements.txt

To run the program, run the following command in a terminal:

        python main.py

*Abstract*
========
The extraction of process models from natural language text is an essential task for process discovery. Several approaches have been developed in recent years to address this task. Still, one of the main limitations is the impossibility of visualizing the extracted process model and comparing it with gold standard data to assess similarity. 
In this paper, we present PET Visualizer, a visualization tool developed to graphically represent the process models of the document annotated in the PET dataset, the unique gold-standard dataset developed for process information extraction tasks.
The main goal of PET Visualizer is to provide a way to visualize the dataset, making it easier to analyze and understand the process models. 
The tool supports several visualization options and can be easily integrated into existing workflows or extend the function implemented. During the system presentation, we demonstrate the effectiveness of the tool and its potential impact in improving process extraction from text tas

---
![PET Visualizers GUI](figures/PETVisualizerscreenshot1.jpg)
*Fig.1 A screenshot of the PET Visualizer GUI.*

We present PET Visualizer, a tool developed to graphically visualize process model document annotations and the representation of the process model in the form of labeled graphs. For this first version of the tool, we concentrate on providing a graphical representation of the annotations of the [PET dataset](https://huggingface.co/datasets/patriziobellan/PET), the unique gold-standard dataset freely available specifically for process information extraction tasks.  The PET dataset is a corpus of human-annotated process model descriptions. It consists of a collection of 45 descriptions annotated with process model elements and relations at the textual level. 

The GUI, shown in *Fig.1*, is composed of three main parts: ***Command Bar***, ***Annotation Menu***, and ***Text Area***.

On the top left side of the GUI, there is the *Command Bar*.
Starting from the left end side, the first button allows the hiding of the command bar for showing a more significant portion of text annotated in *Text Area*.
Along with this, a list box shows the names of the documents annotated in the PET dataset. Here, selecting a document to visualize the gold standard annotations is possible. Next, there is a list of the main commands of the tool that allow a user to:
- *Load PETv1.1* Loads the original PET dataset from the HuggingFace repository.
- Export Data* Exports the dataset in a JSON format after manipulation.
- Export for HuggingFace* Exports the manipulated dataset in the same format and following the original schema of the PET dataset on HuggingFace. This important feature allows the extension of the PET dataset with new data while keeping compatibility with other PET-related tools (e.g., [PET Dataset Reader](https://pypi.org/project/petdatasetreader/)).
- Show Process Graph* Shows the process model graph of the annotations of a document. When you choose to visualize the process graph of a document, a new window displays the graph representation where the nodes represent the entities and the edges represent the relations.
		At the top of this window, we implemented the two accessibility controls to increase the size of nodes and edges and the font size of the text.
		At the bottom side, there are the common *matplotlib* commands to navigate and export the graph image.
		An example of graph visualization is shown in *Fig.2*.
- *Load Json Data* Loads a local dataset. The local dataset is split into two JSON files: an *entities* annotation file and a *relations* annotation file. This command is straightforward but makes the dataset loading operation faster than loading from the HuggingFace repository every time.
![PET Visualizers GUI - process graph](figures/PETVisualizerscreenshootgraph.jpg)
*Fig.2 A screenshot of the PET Visualizer - Process Graph visualization.*

Finally, in the last part of the command bar, we implemented two scroll controls that allow users to set the size of the annotation lines and the font size of the text. These two controls would increase *accessibility* of our tool.

On the right-hand side of the GUI, the *Annotation Menu* allows users to create, delete, or edit annotations. The menu is divided into two cards, one for process model elements (as shown in Figure \ref{fig:menuentities*) and the other for process model element relations (as shown in Figure \ref{fig:menurelations*). Each schedule consists of a list box that displays all the annotations (either elements or relations) of the document. When an item is selected in the list box, the corresponding annotation is highlighted in the *Text Area*.


 
*Entities Menu*
---
![PET Visualizers GUI - Entities Menu](figures/PETVisualizermenuentities.jpg)
*Fig.3 Entities menu.*

The Entities Menu card, shown in *Fig.3*, lists all the process model element annotations of the selected document.
This menu consists of a list box containing all the process model annotations for a document. Each item represents a single annotation. The list box reports the annotation ID, the type of process model element annotated (such as *PET activity*), and the words annotated (e.g., *a company*) for each annotation.
Below the list box, a process element type combo box reports the type of process model element, while the *n sent* text field shows the index of the sentence of the words annotated. The *Begin* and *End* text fields represent the index of the first and last words of the span of words that the annotation covers\footnote{It is essential to note that all the indexes (sentence, begin, end) start from 0.*.
When an entity is selected, its information fills these text fields.
When creating a new annotation, these fields must be filled with the annotation data.
At the bottom part of the card, there are the annotation commands:
- *Create New Annotation* This command starts the creation of a new entity annotation. This operation reset the text fields and the combo box to allow the user to select the type of PET element to annotate
- *Show temp Annotation* This command displays the annotation being edited.
- *Add Annotation* This command adds a newly created annotation to the document.
- *Delete Annotation*This command deletes the selected annotation.


*Relations Menu*
---
![PET Visualizers GUI - Relations Menu](figures/PETVisualizermenurelations.jpg)
*Fig.4 Relations menu.*
 

The Relations Menu card, shown in *Fig.4*, contains all the process model relation annotations of a document. This menu comprises a list box where each item represents a single annotation and includes the annotation ID, the type of relation annotated (e.g., *PET uses relation*), and the source and target elements of the relation.

Below the list of relations, three combo boxes report the source, the relation type, and the target element.
When a relation is selected, the relation data fills the combo boxes.
When creating a new relation, the combo boxes allow users to select the elements of the relation. 

The process of creating a new relation starts with selecting the source element of the relation.
The source element type (e.g., *PET activity*) determines the type of relations it can make with other PET elements, as specified in the [PET annotation schema](https://pdi.fbk.eu/pet/annotation-guidelines-for-process-description.pdf). The element type also determines the type of relations that can be selected. When the relation type is chosen, the target items are filtered accordingly. We have implemented a filtering mechanism that completely prevents the error of assigning an invalid relation type (e.g., linking a *PET activity* with a *PET XOR Gateway* via *PET uses relation*).
When the three combo boxes are filled, the tool shows the relation with dashed lines. To be created, the relation must be added to the list of relations via *Add Annotation* command.
At this point, the tool will render the fresh annotation in the *Text Area*. 

At the bottom part of the card, there are three annotation commands:
- *Create New Annotation* This command starts the creation of a new annotation.	
- *Add Annotation* This command adds a newly created annotation to the document.
- *Delete Annotation* This command deletes the selected annotation.

***Text Area*** part lies in the central part of the GUI. It shows the text of a document and its annotations. PET elements are highlighted in boxes, while PET relations connect PET elements using labeled arrows. Boxes and relation arrows follow the color schema reported in *Fig.5*.

![Color Schema](https://github.com/patriziobellan86/PETvisualizer/blob/master/img/colorschema.jpg)
*Fig.5 Relations menu.*


Dependencies installation notes
===============================
If the installation of requirements fails, you need to downgrade the setuptool and wheel packages.
run the following command in a terminal:

    pip install setuptools==65.5.0 "wheel<0.40.0"

An explanation of this behavior with pip program can be found [here*(://stackoverflow.com/questions/76129688/why-is-pip-install-gym-failing-with-python-setup-py-egg-info-did-not-run-succ)


Visualization notes
===================
We raccomand to run the program with a ***light mode*** theme on your machine, to avoid visualization problems.

