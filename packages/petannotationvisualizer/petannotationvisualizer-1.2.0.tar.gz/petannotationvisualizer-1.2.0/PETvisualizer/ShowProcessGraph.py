import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import networkx as nx
import ast
from utility import readjson
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
from petreader.labels import *
import mplcursors
from Labels import *

COLORS = {
        ACTIVITY:                       'green',
        AND_GATEWAY:                    'orange',
        XOR_GATEWAY:                    'red',
        ACTIVITY_DATA:                  'salmon',
        ACTOR:                          'blue',
        CONDITION_SPECIFICATION:        'gold',
        FURTHER_SPECIFICATION:          'orchid',

        FLOW:                           'green',
        USES:                           'salmon',
        ACTOR_PERFORMER:                'dodgerblue',
        ACTOR_RECIPIENT:                'navy',
        FURTHER_SPECIFICATION_RELATION: 'orchid',
        SAME_GATEWAY:                   'red',
}

class ShowGraphGUI(tk.Frame):

    def __init__(self, parent, graph_data):
        tk.Frame.__init__(self, parent)
        self._init_variables_()

        self.parent = parent
        self.parent.geometry('1150x800')
        self._graph = graph_data
        graph_name = graph_data.name
        self.window_title = '{}'.format(graph_name)
        self.parent.title(self.window_title)
        # self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='./icons/wolficon.png'))
        # # self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='./icons/wolfgold.png'))
        self._create_gui()

        self._show_graph()

    # def _load_data(self):
    #     filename = filedialog.askopenfilename(initialdir=os.path.abspath(os.path.curdir),
    #                                           defaultextension='.dot')
    #     print(os.path.abspath(filename))
    #     self._graph = nx.nx_agraph.read_dot(os.path.abspath(filename))
    #
    #     #  fix attrs
    #     for node in self._graph.nodes:
    #         self._graph.nodes[node]['attrs'] = ast.literal_eval(self._graph.nodes[node]['attrs'])
    #     for edge in self._graph.edges:
    #         self._graph.edges[edge]['attrs'] = ast.literal_eval(self._graph.edges[edge]['attrs'])

        # self._show_graph()

    def _init_variables_(self):
        self._graph = None

        self.font_size = tk.IntVar()
        self.font_size.set(15)
        self.node_size = tk.IntVar()
        self.node_size.set(25)
        self.padding = 5

    def _create_gui(self):
        self.frmCommands = tk.Frame(self.parent)
        self.frmCommands.pack(side='top', expand=False, fill='x')

        # tk.Button(self.frmCommands,
        #           text='load graph',
        #           command=self._load_data).pack(side='left',
        #                                         fill='y')

        self.sclMarkingThick = tk.Scale(self.frmCommands,
                                        label='Node Size',
                                        length=200,
                                        variable=self.node_size,
                                        orient='horizontal',
                                        from_=1,
                                        to=125,
                                        command=self._show_graph
                                        )
        self.sclMarkingThick.pack(side='left')

        self.sclMarkingThick = tk.Scale(self.frmCommands,
                                        label='Font Size',
                                        length=200,
                                        variable=self.font_size,
                                        orient='horizontal',
                                        from_=1,
                                        to=25,
                                        command=self._show_graph
                                        )
        self.sclMarkingThick.pack(side='left')

        # tk.Label(self.parent,
        #          text=self.window_title,
        #          background='black',
        #          foreground='white').pack(side='top', fill='x')
        self._fig_ = Figure(frameon=False, dpi=100)
        self._ax_ = self._fig_.subplots(1, 1)

        self._canvas_ = tk.Canvas(self.parent)
        self._canvas_.pack(side='top',
                           fill='both',
                           expand=True)
        self._canvas_plot = FigureCanvasTkAgg(self._fig_,
                                              master=self._canvas_)
        self._canvas_plot.get_tk_widget().pack(fill='both',
                                               expand=True)
        # self._fig_.canvas.mpl_connect('motion_notify_event', self.on_plot_hover)
        self._fig_.canvas.mpl_connect('button_press_event', self.on_click)
        toolbar = NavigationToolbar2Tk(self._canvas_plot,
                                       self.parent)

        toolbar.update()
        # ##
        self.node_size.set(15)
        self.font_size.set(10)
        # self.Expand()

    # def on_plot_hover(self, event):
    def on_click(self, event):
        if event.inaxes:
            print(f'data coords {event.xdata} {event.ydata},',
                  f'pixel coords {event.x} {event.y}')
        # if self._fig_.contains(event)[0]:
        #     print("over %s" % self._fig_.get_gid())
        for ele in self._ax_.get_children():
            if ele.contains(event)[0]:
                if type(ele) == matplotlib.collections.PathCollection:
                    # node

                    print("win", ele, type(ele))
                # print(ele.get_label(), ele._label)

                if type(ele) == matplotlib.patches.FancyArrowPatch:
                    #  edge
                    print('this is an edge')

        #         if type(ele) == matplotlib.collections.PathCollection:
        #             ek = ele
        # self._ax_
        #
        #
        # return
        # # Iterating over each data member plotted
        # for curve in self._graph.nodes:
        #     # Searching which data member corresponds to current mouse position
        #     if self._fig_.contains(event)[0]:
        #         print("over %s" % curve.get_gid())
        # for curve in self._graph.edges:
        #     # Searching which data member corresponds to current mouse position
        #     if curve.contains(event)[0]:
        #         print("over %s" % curve.get_gid())

    #  this one
    def _show_graph(self, *event):
        """
                it create a plot of the graph
                if a filename is passed, the figure is saved but not shown
        Parameters
        ----------
        filename

        Returns
        -------

        """
        self._fig_.clear()
        self._ax_ = self._fig_.add_subplot(111)

        # if not font_size:
        font_size = self.font_size
        # if not node_size:
        node_size = self.node_size

        color_map = list()
        labels = dict()
        label_pos = dict()
        node_pos = dict()
        edges_labels = dict()
        edges_color = list()

        #############################################
        # use pydot to get node position
        node_pos = nx.nx_agraph.graphviz_layout(self._graph, prog='dot')
        # self.wm_node_pos = node_pos

        #  retrieve graph attributes to display
        for node in self._graph.nodes:
            #  transform attrs into dict
            # color_map.append(COLORS[self._graph.nodes[node]['attrs']['type']])
            color_map.append(matplotlib.colors.to_rgb(COLORS[self._graph.nodes[node]['attrs'][TYPE]]))
            labels[node] = self._graph.nodes[node]['attrs'][LABEL]
            # set label pos below the node
            label_pos[node] = node_pos[node][0], node_pos[node][1] - self.padding

        # Edges
        for edge in self._graph.edges(data=True):
            source, target, attrs = edge
            attrs = attrs['attrs']
            edges_labels[source, target] = attrs['label']
            # edges_color[source, target] = matplotlib.colors.to_rgb(self.wm.edges[edge]['attr']['color'])
            edges_color.append(matplotlib.colors.to_rgb(COLORS[attrs['type']]))

        nodes = nx.draw(self._graph,
                        # with_labels=True,
                        node_color=color_map,
                        edge_color=edges_color,
                        pos=node_pos,
                        # labels=labels,
                        font_size=font_size.get(),
                        node_size=node_size.get(),
                        font_color='black',
                        ax=self._ax_,
                        )
        self.mh_nodes = nx.draw_networkx_nodes(self._graph,
                                               # with_labels=True,
                                               node_color=color_map,
                                               # edge_color=edges_color,
                                               pos=node_pos,
                                               # labels=labels,
                                               # font_size=font_size.get(),
                                               node_size=node_size.get(),
                                               # font_color='black',
                                               ax=self._ax_,
                                               )

        nx.draw_networkx_labels(self._graph,
                                label_pos,
                                font_size=font_size.get(),
                                labels=labels,
                                ax=self._ax_)

        nx.draw_networkx_edge_labels(self._graph,
                                     font_size=int(font_size.get()/2),
                                     edge_labels=edges_labels,
                                     label_pos=0.5,
                                     pos=node_pos,  # edges_pos,
                                     ax=self._ax_)
        self.mh_edges = nx.draw_networkx_edges(self._graph,
                                               # with_labels=True,
                                               # node_color=color_map,
                                               edge_color=edges_color,
                                               pos=node_pos,
                                               # labels=labels,
                                               # font_size=font_size.get(),
                                               node_size=node_size.get(),
                                               # font_color='black',
                                               ax=self._ax_,
                                               )
        self._fig_.subplots_adjust(left=0,
                                   bottom=0,
                                   right=1,
                                   top=1,
                                   wspace=0,
                                   hspace=0)

        self._canvas_plot.draw()
        self._canvas_plot.draw_idle()

        cursor = mplcursors.cursor(self.mh_nodes, hover=True)
        cursor.connect('add', self.update_annot_node)

    def update_annot_node(self, sel):
        node_index = sel.target.index
        node_name = list(self._graph.nodes)[node_index]
        node_attr = self._graph.nodes[node_name]['attrs']
        # text = node_name + ' ' + '\n'.join(f'{k}: {v}' for k, v in node_attr.items())
        text = f"{node_attr['label']} | {node_attr['type']}"
        sel.annotation.set_text(text)

    def update_annot_edge(self, sel):
        node_index = sel.target.index
        node_name = list(self._graph.nodes)[node_index]
        node_attr = self._graph.nodes[node_name]['attrs']
        # text = node_name + ' ' + '\n'.join(f'{k}: {v}' for k, v in node_attr.items())
        text = f"{node_attr['label']} | {node_attr['type']}"
        sel.annotation.set_text(text)
    # def DrawFigure(self, *event):
    #     # clear previous fig
    #     self.fig_annotator1.clear()
    #     self.ax_annotator1 = self.fig_annotator1.add_subplot(111)
    #
    #     self.fa2wm.DrawWorldModelOnAx(self.ax_annotator1,
    #                              self.behavioral_only,
    #                              font_size=self.font_size.get(),
    #                              node_size=self.node_size.get())
    #     self.fig_annotator1.subplots_adjust(left=0,
    #                                         bottom=0,
    #                                         right=1,
    #                                         top=1,
    #                                         wspace=0,
    #                                         hspace=0)
    #
    #     self.canvas_annotator1_plot.draw()
    #     self.canvas_annotator1_plot.draw_idle()
    #
    #     self.Close()
    #
    # def OpenClose(self):
    #     if self.btnOpenCloseStatus.get():
    #         self.Close()
    #     else:
    #         self.Expand()
    #
    # def Close(self):
    #     self.frmCommands.config(height=self.width_closed)
    #     self.btnOpenCloseText.set('Open')
    #     self.btnOpenCloseStatus.set(False)
    #
    # def Expand(self):
    #     self.frmCommands.config(height=self.width_expanded)
    #     self.btnOpenCloseText.set('Close')
    #     self.btnOpenCloseStatus.set(True)


class ShowGraphGUIwithData(tk.Frame):

    def __init__(self, parent,  graph_data, dfg_list):
        tk.Frame.__init__(self, parent)
        self._init_variables_()

        self.parent = parent
        self.parent.geometry('1150x800')
        self._graph = graph_data
        graph_name = graph_data.name
        self.window_title = '{}'.format(graph_name)
        self.parent.title(self.window_title)

        self.dfg_list = dfg_list

        # self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='./icons/wolficon.png'))
        # # self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='./icons/wolfgold.png'))
        self._create_gui()

        self._show_graph()


    def _init_variables_(self):
        self._graph = None

        self.font_size = tk.IntVar()
        self.font_size.set(15)
        self.node_size = tk.IntVar()
        self.node_size.set(25)
        self.padding = 5

    def _create_gui(self):
        self.frmCommands = tk.Frame(self.parent)
        self.frmCommands.pack(side='top', expand=False, fill='x')

        # tk.Button(self.frmCommands,
        #           text='load graph',
        #           command=self._load_data).pack(side='left',
        #                                         fill='y')

        self.sclMarkingThick = tk.Scale(self.frmCommands,
                                        label='Node Size',
                                        length=200,
                                        variable=self.node_size,
                                        orient='horizontal',
                                        from_=1,
                                        to=125,
                                        command=self._show_graph
                                        )
        self.sclMarkingThick.pack(side='left')

        self.sclMarkingThick = tk.Scale(self.frmCommands,
                                        label='Font Size',
                                        length=200,
                                        variable=self.font_size,
                                        orient='horizontal',
                                        from_=1,
                                        to=25,
                                        command=self._show_graph
                                        )
        self.sclMarkingThick.pack(side='left')

        self.lateral_width_closed = 20
        self.lateral_width_expanded = 500
        self.opencloselateral = tk.StringVar()
        self.opencloselateral_status = tk.BooleanVar()

        self.lateral_frame = tk.Frame(self.parent)
        self.lateral_frame.pack(side='left', fill='y')
        self.lateral_frame.pack_propagate(0)

        tk.Button(self.lateral_frame,
                  textvariable=self.opencloselateral,
                  command=self.OpenCloseLateral).pack(side='top', fill='x')
        self.ExpandLateral()
        tk.Label(self.lateral_frame, text=f"{len(self.dfg_list)}").pack(side='top')

        self.lst_dfg = tk.Listbox(self.lateral_frame, width=65)
        self.lst_dfg.pack(side='left', fill='y')
        self.lst_dfg.bind('<<ListboxSelect>>', self.lst_dfg_selected)


        for dfg_rel in self.dfg_list:
            self.lst_dfg.insert('end', dfg_rel)
        # tk.Label(self.parent,
        #          text=self.window_title,
        #          background='black',
        #          foreground='white').pack(side='top', fill='x')
        self._fig_ = Figure(frameon=False, dpi=100)
        self._ax_ = self._fig_.subplots(1, 1)

        self._canvas_ = tk.Canvas(self.parent)
        self._canvas_.pack(side='top',
                           fill='both',
                           expand=True)
        self._canvas_plot = FigureCanvasTkAgg(self._fig_,
                                              master=self._canvas_)
        self._canvas_plot.get_tk_widget().pack(fill='both',
                                               expand=True)
        # self._fig_.canvas.mpl_connect('motion_notify_event', self.on_plot_hover)
        self._fig_.canvas.mpl_connect('button_press_event', self.on_click)
        toolbar = NavigationToolbar2Tk(self._canvas_plot,
                                       self.parent)

        toolbar.update()
        # ##
        self.node_size.set(15)
        self.font_size.set(10)
        # self.Expand()

    def OpenCloseLateral(self):
        if self.opencloselateral_status.get():
            self.CloseLateral()
        else:
            self.ExpandLateral()

    def CloseLateral(self):
        self.lateral_frame.config(width=self.lateral_width_closed)
        self.opencloselateral.set('>>')
        self.opencloselateral_status.set(False)

    def ExpandLateral(self):
        self.lateral_frame.config(width=self.lateral_width_expanded)
        self.opencloselateral.set('Close <<')
        self.opencloselateral_status.set(True)

    # def on_plot_hover(self, event):
    def on_click(self, event):
        if event.inaxes:
            print(f'data coords {event.xdata} {event.ydata},',
                  f'pixel coords {event.x} {event.y}')
        # if self._fig_.contains(event)[0]:
        #     print("over %s" % self._fig_.get_gid())
        for ele in self._ax_.get_children():
            if ele.contains(event)[0]:
                if type(ele) == matplotlib.collections.PathCollection:
                    # node

                    print("win", ele, type(ele))
                # print(ele.get_label(), ele._label)

                if type(ele) == matplotlib.patches.FancyArrowPatch:
                    #  edge
                    print('this is an edge')

        #         if type(ele) == matplotlib.collections.PathCollection:
        #             ek = ele
        # self._ax_
        #
        #
        # return
        # # Iterating over each data member plotted
        # for curve in self._graph.nodes:
        #     # Searching which data member corresponds to current mouse position
        #     if self._fig_.contains(event)[0]:
        #         print("over %s" % curve.get_gid())
        # for curve in self._graph.edges:
        #     # Searching which data member corresponds to current mouse position
        #     if curve.contains(event)[0]:
        #         print("over %s" % curve.get_gid())

    #  this one
    def lst_dfg_selected(self, *event):
        relation =self.lst_dfg.get(self.lst_dfg.curselection()[0])

        source, target = relation.split(' -> ')
        for (node, attrs) in self._graph.nodes(data=True):
            if attrs['attrs']['label'] == source:
                source_node = node
            elif attrs['attrs']['label'] == target:
                target_node = node

        self._show_graph(nodes_to_highlight=[source_node, target_node])


    def _show_graph(self, nodes_to_highlight=list(),*event):
        """
                it create a plot of the graph
                if a filename is passed, the figure is saved but not shown
        Parameters
        ----------
        filename

        Returns
        -------

        """
        self._fig_.clear()
        self._ax_ = self._fig_.add_subplot(111)

        # if not font_size:
        font_size = self.font_size
        # if not node_size:
        node_size = self.node_size

        color_map = list()
        labels = dict()
        label_pos = dict()
        node_sizes = list()
        edges_labels = dict()
        edges_color = list()

        #############################################
        # use pydot to get node position
        self.node_pos = nx.nx_agraph.graphviz_layout(self._graph, prog='dot')
        # self.wm_node_pos = node_pos

        #  retrieve graph attributes to display
        for node in self._graph.nodes:
            #  transform attrs into dict
            # color_map.append(COLORS[self._graph.nodes[node]['attrs']['type']])
            if node in nodes_to_highlight:
                color_map.append('yellow')
                node_sizes.append(self.node_size.get()*5)
            else:
                color_map.append(matplotlib.colors.to_rgb(COLORS[self._graph.nodes[node]['attrs'][TYPE]]))
                node_sizes.append(self.node_size.get())
            labels[node] = self._graph.nodes[node]['attrs'][LABEL]
            # set label pos below the node
            label_pos[node] = self.node_pos[node][0], self.node_pos[node][1] - self.padding

        # Edges
        for edge in self._graph.edges(data=True):
            source, target, attrs = edge
            attrs = attrs['attrs']
            edges_labels[source, target] = attrs['label']
            # edges_color[source, target] = matplotlib.colors.to_rgb(self.wm.edges[edge]['attr']['color'])
            edges_color.append(matplotlib.colors.to_rgb(COLORS[attrs['type']]))

        nodes = nx.draw(self._graph,
                        # with_labels=True,
                        node_color=color_map,
                        edge_color=edges_color,
                        pos=self.node_pos,
                        # labels=labels,
                        font_size=font_size.get(),
                        node_size=node_size.get(),
                        font_color='black',
                        ax=self._ax_,
                        )
        self.mh_nodes = nx.draw_networkx_nodes(self._graph,
                                               # with_labels=True,
                                               node_color=color_map,
                                               # edge_color=edges_color,
                                               pos=self.node_pos,
                                               # labels=labels,
                                               # font_size=font_size.get(),
                                               node_size=node_sizes,
                                               # font_color='black',
                                               ax=self._ax_,
                                               )

        nx.draw_networkx_labels(self._graph,
                                label_pos,
                                font_size=font_size.get(),
                                labels=labels,
                                ax=self._ax_)

        nx.draw_networkx_edge_labels(self._graph,
                                     font_size=int(font_size.get()/2),
                                     edge_labels=edges_labels,
                                     label_pos=0.5,
                                     pos=self.node_pos,  # edges_pos,
                                     ax=self._ax_)
        self.mh_edges = nx.draw_networkx_edges(self._graph,
                                               # with_labels=True,
                                               # node_color=color_map,
                                               edge_color=edges_color,
                                               pos=self.node_pos,
                                               # labels=labels,
                                               # font_size=font_size.get(),
                                               node_size=node_size.get(),
                                               # font_color='black',
                                               ax=self._ax_,
                                               )
        self._fig_.subplots_adjust(left=0,
                                   bottom=0,
                                   right=1,
                                   top=1,
                                   wspace=0,
                                   hspace=0)

        self._canvas_plot.draw()
        self._canvas_plot.draw_idle()

        cursor = mplcursors.cursor(self.mh_nodes, hover=True)
        cursor.connect('add', self.update_annot_node)

    def update_annot_node(self, sel):
        node_index = sel.target.index
        node_name = list(self._graph.nodes)[node_index]
        node_attr = self._graph.nodes[node_name]['attrs']
        # text = node_name + ' ' + '\n'.join(f'{k}: {v}' for k, v in node_attr.items())
        text = f"{node_attr['label']} | {node_attr['type']}"
        sel.annotation.set_text(text)

    def update_annot_edge(self, sel):
        node_index = sel.target.index
        node_name = list(self._graph.nodes)[node_index]
        node_attr = self._graph.nodes[node_name]['attrs']
        # text = node_name + ' ' + '\n'.join(f'{k}: {v}' for k, v in node_attr.items())
        text = f"{node_attr['label']} | {node_attr['type']}"
        sel.annotation.set_text(text)
    # def DrawFigure(self, *event):
    #     # clear previous fig
    #     self.fig_annotator1.clear()
    #     self.ax_annotator1 = self.fig_annotator1.add_subplot(111)
    #
    #     self.fa2wm.DrawWorldModelOnAx(self.ax_annotator1,
    #                              self.behavioral_only,
    #                              font_size=self.font_size.get(),
    #                              node_size=self.node_size.get())
    #     self.fig_annotator1.subplots_adjust(left=0,
    #                                         bottom=0,
    #                                         right=1,
    #                                         top=1,
    #                                         wspace=0,
    #                                         hspace=0)
    #
    #     self.canvas_annotator1_plot.draw()
    #     self.canvas_annotator1_plot.draw_idle()
    #
    #     self.Close()
    #
    # def OpenClose(self):
    #     if self.btnOpenCloseStatus.get():
    #         self.Close()
    #     else:
    #         self.Expand()
    #
    # def Close(self):
    #     self.frmCommands.config(height=self.width_closed)
    #     self.btnOpenCloseText.set('Open')
    #     self.btnOpenCloseStatus.set(False)
    #
    # def Expand(self):
    #     self.frmCommands.config(height=self.width_expanded)
    #     self.btnOpenCloseText.set('Close')
    #     self.btnOpenCloseStatus.set(True)


if __name__ == '__main__':
    window = tk.Tk()
    # window.geometry('950x600')
    program = ShowGraphGUI(window, )
    # Start the GUI event loop
    program.mainloop()
