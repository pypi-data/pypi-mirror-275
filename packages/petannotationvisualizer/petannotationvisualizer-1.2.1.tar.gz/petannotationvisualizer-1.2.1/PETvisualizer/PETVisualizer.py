#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrizio Bellan
@email: patrizio.bellan@gmail.com


"""
import os
from copy import deepcopy
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import tkinter.font as tkFont
from collections import defaultdict
from pathlib import Path
from tkinter import filedialog as fd
from Labels import * # from PET_TEST.ExperimentLabels import *
from utility import readjson
import networkx as nx
import json
import sys 

seed = 23
import random
from CreateProcessGraph import CreateGraph
from ShowProcessGraph import ShowGraphGUI, ShowGraphGUIwithData
from utility import savejson, readjson

from petreader.TokenClassification import TokenClassification
from petreader.RelationsExtraction import RelationsExtraction
from petreader.labels import *
from tqdm import tqdm
from itertools import combinations
import json
import random

random.seed(23)

MARK_COLORS = {
        ACTIVITY:                       'dark green',
        AND_GATEWAY:                    'orange',
        XOR_GATEWAY:                    'red',
        ACTIVITY_DATA:                  'dark salmon',
        ACTOR:                          'royal blue',
        CONDITION_SPECIFICATION:        'gold4',
        FURTHER_SPECIFICATION:          'medium orchid',

        FLOW:                           'green',
        USES:                           'dark salmon',
        ACTOR_PERFORMER:                'blue',
        ACTOR_RECIPIENT:                'blue',
        FURTHER_SPECIFICATION_RELATION: 'orchid',
        SAME_GATEWAY:                   'red',
}
RE_LABELS_ACTIVITY = [USES, FURTHER_SPECIFICATION, ACTOR_PERFORMER, ACTOR_RECIPIENT, FLOW]
BEHAVIORAL_ELEMENTS = [ACTIVITY, CONDITION_SPECIFICATION, XOR_GATEWAY, AND_GATEWAY]

GATEWAYS = ['XOR Gateway', 'AND Gateway']
RE_LABELS_DICT_ALLOWED_TYPES = {FLOW:                  BEHAVIORAL_ELEMENTS,
                                USES:                  ['Activity Data'],
                                ACTOR_PERFORMER:       [ACTOR],
                                ACTOR_RECIPIENT:       [ACTOR],
                                FURTHER_SPECIFICATION: [FURTHER_SPECIFICATION],
                                SAME_GATEWAY:          GATEWAYS,
                                }
PE_LABELS = [ACTIVITY, ACTIVITY_DATA, ACTOR, FURTHER_SPECIFICATION, XOR_GATEWAY, AND_GATEWAY,
             CONDITION_SPECIFICATION]
RE_LABELS = [USES, FURTHER_SPECIFICATION, ACTOR_PERFORMER, ACTOR_RECIPIENT, FLOW, SAME_GATEWAY]
RE_LABELS_BEHAVIORAL = [FLOW]
RE_LABELS_GATEWAY = [FLOW, SAME_GATEWAY]


def simplify_graph_with_predicate(G: nx.Graph, node_removal_predicate: callable):
    '''
    Loop over the graph until all nodes that match the supplied predicate
    have been removed and their incident edges fused.
    '''
    g = G.copy()
    while any(node_removal_predicate(node) for node in g.nodes):

        g0 = g.copy()

        for node in g.nodes:
            if node_removal_predicate(node):

                if g.is_directed():
                    in_edges_containing_node = list(g0.in_edges(node))
                    out_edges_containing_node = list(g0.out_edges(node))

                    for in_src, _ in in_edges_containing_node:
                        for _, out_dst in out_edges_containing_node:
                            g0.add_edge(in_src, out_dst, attrs={'type': FLOW, 'label': FLOW})

                else:
                    edges_containing_node = g.edges(node, data=True)
                    dst_to_link = [e[1] for e in edges_containing_node]
                    dst_pairs_to_link = list(combinations(dst_to_link, r=2))
                    for pair in dst_pairs_to_link:
                        g0.add_edge(pair[0], pair[1], attrs={'type': FLOW, 'label': FLOW})

                g0.remove_node(node)
                break
        g = g0
    return g


class PETVisualizerGUI(tk.Frame):
    pe_labels_dict_plot = {k: k for k in PE_LABELS}
    SENTENCE_OFFSET = 60
    WORD_OFFSET = 20

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry('1450x1100')
        self.parent.title('PET Visualizer')
        self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='./wolfgold.png'))

        # init variables
        self.__init__varialbles__()

        # create interface
        self.__create_GUI()

    def LoadPET(self):
        self._load_pet_dataset()
        self._load_document_names()

    def __init__varialbles__(self):
        self.re = RelationsExtraction()

        #  dataset data
        self.pet_relations = dict()
        self.pet_entities = dict()
        # load the
        # self._load_pet_dataset()

        #  document data
        self.document_relations = list()  # keep relation data. the index identify the row
        self.document_entities = list()  # as relations

        self.is_create_new_annotation = False
        self.is_create_new_relation = False

        # self.entities_dict = dict()  # {(n_sent, start, end): pe_type}

        self._font_size = tk.IntVar()
        self._font_size.set(15)
        self._box_border_size = tk.IntVar()
        self._box_border_size.set(1)

        self.selection_lst_documents = 0
        self.selection_lst_entities_annotations = 0
        self.selection_lst_relations_annotations = 0

        self.document_is_changed = tk.BooleanVar()
        self.document_is_changed.set(False)
        # self.previous_document_index = tk.IntVar()

        self.pe_type = tk.StringVar()
        self.pe_n_sent_val = tk.IntVar()
        self.pe_begin_val = tk.IntVar()
        self.pe_end_val = tk.IntVar()
        self.re_source = tk.StringVar()
        self.re_type = tk.StringVar()
        self.re_target = tk.StringVar()

        ###
        self.width_closed = 15
        self.width_expanded = 150
        self.btnOpenCloseText = tk.StringVar()
        self.btnOpenCloseStatus = tk.BooleanVar()

        self.lateral_width_closed = 20
        self.lateral_width_expanded = 500
        self.opencloselateral = tk.StringVar()
        self.opencloselateral_status = tk.BooleanVar()

        self.canvas_height_start = self.SENTENCE_OFFSET * 2
        self.canvas_width_start = 50
        self.canvas_height = 50
        self.canvas_width = 50

    def __document_list_changed(self, *events):
        if self.lst_documents.curselection():
            self.selection_lst_documents = self.lst_documents.curselection()[0]
            self.current_doc_name = self.lst_documents.get(self.lst_documents.curselection())
            self._load_document_annotation()  # self.current_doc_name)

            # save current state
            if self.document_entities and self.document_relations:
                self.pet_entities[self.current_doc_name] = self.document_entities
                self.pet_relations[self.current_doc_name] = self.document_relations

    def _load_pet_dataset(self):
        # for doc_name in tqdm([
        #                              'doc-1.1']):  # , 'doc-1.2', 'doc-1.3']): #self.re.GetDocumentNames(), desc='loading pet dataset', dynamic_ncols=True):
        #
        #
        #     print(doc_name)
        for doc_name in tqdm(self.re.GetDocumentNames(), desc='loading pet dataset', dynamic_ncols=True):
            doc_id = self.re.GetDocumentNumber(doc_name)
            # get data
            doc_data = self.re.GetRelations(doc_id)
            #  order data
            #  translate into a easy sortable dict
            relations_to_order = list()
            entities_to_order = list()

            for rel_type in doc_data.keys():
                for relation in doc_data[rel_type]:
                    relations_to_order.append((deepcopy(relation), rel_type))

                    source_text = f"{relation[SOURCE_ENTITY_TYPE]} | {' '.join(relation[SOURCE_ENTITY])}"
                    source = {SOURCE_SENTENCE_ID:   relation[SOURCE_SENTENCE_ID],
                              SOURCE_HEAD_TOKEN_ID: relation[SOURCE_HEAD_TOKEN_ID],
                              SOURCE_ENTITY:        relation[SOURCE_ENTITY]}
                    source = (relation[SOURCE_ENTITY_TYPE], source)
                    if source not in entities_to_order:
                        entities_to_order.append(source)

                    target = {SOURCE_SENTENCE_ID:   relation[TARGET_SENTENCE_ID],
                              SOURCE_HEAD_TOKEN_ID: relation[TARGET_HEAD_TOKEN_ID],
                              SOURCE_ENTITY:        relation[TARGET_ENTITY]}
                    target = (relation[TARGET_ENTITY_TYPE], target)
                    target_text = f"{relation[TARGET_ENTITY_TYPE]}| {' '.join(relation[TARGET_ENTITY])}"
                    if target not in entities_to_order:
                        entities_to_order.append(target)

            sorted_relations = sorted(relations_to_order,
                                      key=lambda x: (
                                              x[0][SOURCE_SENTENCE_ID], x[0][SOURCE_HEAD_TOKEN_ID],
                                              x[0][TARGET_SENTENCE_ID],
                                              x[0][TARGET_HEAD_TOKEN_ID]))
            sorted_entities = sorted(entities_to_order,
                                     key=lambda x: (
                                             x[1][SOURCE_SENTENCE_ID], x[1][SOURCE_HEAD_TOKEN_ID]))

            #  put back relations into original format
            # sorted_relations_original_format = defaultdict(list)
            # for rel in sorted_relations:
            #     sorted_relations_original_format[rel[1]].append(rel[0])
            #  memorize
            self.pet_relations[doc_name] = sorted_relations  # dict(sorted_relations_original_format)
            self.pet_entities[doc_name] = sorted_entities
            # self.pet_entities[doc_name]=
            # if dev == 3:
            #     break
            # dev += 1

    def _load_document_annotation(self):
        # self.is_create_new_relation = False
        # self.relation_is_changed = False
        #  load annotation
        self.document_entities = self.pet_entities[self.current_doc_name]
        self.document_relations = self.pet_relations[self.current_doc_name]
        self.__fill_relation_list(self.document_relations)
        self.__fill_entities_list(self.document_entities)
        self.__draw_annotation()

    def re_source_Changed(self, *event):
        self._fill_cmb_rel_type()

    def __draw_annotation(self, *event):
        #  draws
        self._draw_document_text()
        # self.__draw_document_relations()

        self.__draw_document_entities()
        self.__draw_document_relations()

        self.document_is_changed.set(False)

    def __load_document_relation_list(self, relations):
        self.lst_relations.delete(0, 'end')
        for rel_type in relations.keys():
            for rel in relations[rel_type]:
                source_entity = ' '.join(rel[SOURCE_ENTITY])
                target_entity = ' '.join(rel[TARGET_ENTITY])
                rel_text = f"{rel_type}| {source_entity} -> {target_entity}"
                self.lst_relations.insert('end', rel_text)
                self.document_relations.append((rel_type, rel))

    def __load_document_entities_list(self, relations):
        #  use relation to get entities
        self.lst_entities.delete(0, 'end')
        for rel_type in relations.keys():
            for rel in relations[rel_type]:
                source_text = f"{rel[SOURCE_ENTITY_TYPE]} | {' '.join(rel[SOURCE_ENTITY])}"
                source = {SOURCE_SENTENCE_ID:   rel[SOURCE_SENTENCE_ID],
                          SOURCE_HEAD_TOKEN_ID: rel[SOURCE_HEAD_TOKEN_ID],
                          SOURCE_ENTITY:        rel[SOURCE_ENTITY]}
                source = (rel[SOURCE_ENTITY_TYPE], source)
                if source not in self.document_entities:
                    self.document_entities.append(source)
                    self.lst_entities.insert('end', source_text)

                target = {SOURCE_SENTENCE_ID:   rel[TARGET_SENTENCE_ID],
                          SOURCE_HEAD_TOKEN_ID: rel[TARGET_HEAD_TOKEN_ID],
                          SOURCE_ENTITY:        rel[TARGET_ENTITY]}
                target = (rel[TARGET_ENTITY_TYPE], target)
                target_text = f"{rel[TARGET_ENTITY_TYPE]}| {' '.join(rel[TARGET_ENTITY])}"
                if target not in self.document_entities:
                    self.document_entities.append(target)
                    self.lst_entities.insert('end', target_text)
        # update combo box
        self._fill_cmb_re_source_list()

    def __fill_relation_list(self, relations):
        self.lst_relations.delete(0, 'end')
        for n_rel, rel in enumerate(relations):
            # for rel in relations[rel_type]:
            rel_type = rel[1]
            rel = rel[0]
            source_entity = ' '.join(rel[SOURCE_ENTITY])
            target_entity = ' '.join(rel[TARGET_ENTITY])
            rel_text = f"{n_rel}| {rel_type}| {source_entity} -> {target_entity}"
            self.lst_relations.insert('end', rel_text)

    def __fill_entities_list(self, entities):
        #  use relation to get entities
        self.lst_entities.delete(0, 'end')
        for n_entity, entity in enumerate(entities):
            self.lst_entities.insert('end', f"{n_entity}| {entity[0]}| {' '.join(entity[1][SOURCE_ENTITY])}")
        # update combo box
        self._fill_cmb_re_source_list()

    def _fill_cmb_re_source_list(self):
        vals = [item.split('|') for item in self.lst_entities.get(0, 'end')
                if item.split('|')[1].strip() in BEHAVIORAL_ELEMENTS]
        vals = sorted(vals, key=lambda x: x[0].strip())
        self.cmb_re_source['values'] = [' | '.join(item) for item in vals]

    def _load_document_names(self):
        #  ok - fixed
        self.lst_documents.delete(0, 'end')
        for doc_name in sorted(self.pet_relations.keys()):
            self.lst_documents.insert(tk.END, doc_name)
            # if self.gold_standard_annotator_name in self.dataset.dataset['documents'][doc_name].keys():
            self.lst_documents.itemconfig('end', bg='green')
            self.lst_documents.itemconfig('end', foreground="white")
        self.__document_list_changed()

    def __create_GUI(self):
        # frame
        self.Frame = tk.Frame(self.parent)
        self.Frame.pack(fill='both',
                        expand=True)

        self.frmCommands = tk.Frame(self.Frame)
        self.frmCommands.pack(fill='x')
        self.frmCommands.pack_propagate(0)

        self.btnOpenClose = tk.Button(self.frmCommands,
                                      textvariable=self.btnOpenCloseText,
                                      command=self.OpenClose)
        self.btnOpenClose.pack(side='left',
                               fill='y')

        frmlbl_doc = tk.LabelFrame(self.frmCommands, text='Documents')
        frmlbl_doc.pack(
                side='left',
                fill='y',
                # expand=True
        )
        frmlbl_ = tk.Frame(frmlbl_doc)
        frmlbl_.pack(side='left', fill='x', expand=True)

        self.lst_documents = tk.Listbox(frmlbl_,
                                        selectmode='single',
                                        exportselection=False,
                                        height=7,
                                        width=13)
        self.lst_documents.pack(side='left', fill='x')
        self.lst_documents.bind("<Down>", self.OnEntryDown_lst_documents)
        self.lst_documents.bind("<Up>", self.OnEntryUp_lst_documents)
        self.lst_documents.bind('<<ListboxSelect>>', self.__document_list_changed)
        scrollbar_doc = tk.Scrollbar(frmlbl_)
        scrollbar_doc.pack(side=tk.RIGHT, fill='y')
        self.lst_documents.config(yscrollcommand=scrollbar_doc.set)
        scrollbar_doc.config(command=self.lst_documents.yview)

        frmlbl_doc_op = tk.Frame(frmlbl_doc)
        frmlbl_doc_op.pack(side='left')

        tk.Button(frmlbl_doc_op,
                  text='Load PETv11',
                  anchor='w',
                  command=self.LoadPET).pack(side='top', fill='x')

        tk.Button(frmlbl_doc_op,
                  text='Export Data',
                  anchor='w',
                  command=self.ExportData).pack(side='top', fill='x')

        tk.Button(frmlbl_doc_op,
                  text='Export for Hugging Face',
                  anchor='w',
                  command=self.ExportDataHG).pack(side='top', fill='x')

        tk.Button(frmlbl_doc_op,
                  text='Show Process Graph',
                  command=self._show_process_graph).pack(side='top', fill='x')

        tk.Button(frmlbl_doc_op,
                  text='LoadJsonData',
                  command=self.LoadJsonData).pack(side='top', fill='x')
        frmlbl_ls = tk.Frame(self.frmCommands)
        frmlbl_ls.pack(side='left', fill='x')
        self.sclMarkingThick = tk.Scale(frmlbl_ls,
                                        label='Line Size',
                                        length=100,
                                        variable=self._box_border_size,
                                        orient='horizontal',
                                        from_=1,
                                        to=7,
                                        command=self.__draw_annotation
                                        )
        self.sclMarkingThick.pack(side='top')

        self.sclTextFont = tk.Scale(frmlbl_ls,
                                    label='Text Size',
                                    length=100,
                                    variable=self._font_size,
                                    orient='horizontal',
                                    from_=11,
                                    to=32,
                                    command=self.__draw_annotation
                                    )
        self.sclTextFont.pack(side='top')
        # frmlbl_graph = tk.Frame(self.frmCommands)
        # frmlbl_graph.pack(side='left', fill='x')
        # tk.Button(frmlbl_graph,
        #           text='Save JSON DFG for In-context Exp.',
        #           command=self._save_json_dfg_relations).pack(side='top', fill='x')
        # 
        # tk.Button(frmlbl_graph,
        #           text='Show DFG for In-context Exp.',
        #           command=self._show_dfg_graph_for_experiments).pack(side='top', fill='x')
        # 
        # tk.Button(frmlbl_graph, text='generate graphs', command=self._generate_all_graphs_nx).pack()
        # tk.Button(frmlbl_graph, text='generate fine-tune-data', command=self._generate_all_graphs_nxELEREL).pack()
        # tk.Button(frmlbl_graph, text='generate fine-tune-dfg-data', command=self._generate_fine_tune_dfg_data).pack()
        # 
        # frmlbl_graph_f = tk.LabelFrame(self.frmCommands, text='fine tuning')
        # frmlbl_graph_f.pack(side='left', fill='x')
        # tk.Button(frmlbl_graph_f, text='CRF IOB2 data', command=self._generate_crf_iob2_data).pack()
        # 
        # tk.Button(frmlbl_graph_f, text='generate activity element',
        #           command=self._generate_finetune_activity_element).pack()
        # tk.Button(frmlbl_graph_f, text='fine-tune-data', command=self._generate_all_graphs_nxELEREL).pack()

        ####### lateral frame #####
        self.lateral_frame = tk.Frame(self.Frame)
        self.lateral_frame.pack(side='left', fill='both')
        self.lateral_frame.pack_propagate(0)

        tk.Button(self.lateral_frame,
                  textvariable=self.opencloselateral,
                  command=self.OpenCloseLateral).pack(side='top', fill='x')

        #  ttk notebook
        notebooklateral = ttk.Notebook(self.lateral_frame)
        notebooklateral.pack(side='top',
                             # expand=True,
                             fill='both')

        #  ENTITIES
        frm_ents = tk.Frame(notebooklateral)
        frm_ents.pack(side='top', fill='both')

        notebookEntities = ttk.Notebook(frm_ents)
        notebookEntities.pack(side='top', fill='both')

        frm_entities = tk.Frame(notebookEntities)  # self.lateral_frame)
        frm_entities.pack(side='top', expand=True, fill='both')

        self.lst_entities = tk.Listbox(frm_entities,
                                       selectmode='single',
                                       exportselection=False,
                                       width=75)
        self.lst_entities.pack()
        self.lst_entities.bind("<Down>", self.OnEntryDown_lst_entities_annotations)
        self.lst_entities.bind("<Up>", self.OnEntryUp_lst_entities_annotations)
        self.lst_entities.bind('<<ListboxSelect>>', self.EntitiesListChanged)

        frm_pe_type = tk.Frame(frm_entities)  # self.lateral_frame)
        frm_pe_type.pack(side='top', fill='x')
        tk.Label(frm_pe_type, text='Process Element Type').pack(side='top')
        self.pe_cmb_type = ttk.Combobox(frm_pe_type,
                                        textvariable=self.pe_type,
                                        values=RE_LABELS,
                                        state='readonly')
        self.pe_cmb_type.pack(side='top', fill='x')

        frm_n_sent = tk.Frame(frm_entities)  # self.lateral_frame)
        frm_n_sent.pack(side='top')
        tk.Label(frm_n_sent, text='n sent.').pack(side='left')
        tk.Entry(frm_n_sent, textvariable=self.pe_n_sent_val).pack(side='left')

        frm_begin = tk.Frame(frm_entities)  # self.lateral_frame)
        frm_begin.pack(side='top')
        tk.Label(frm_begin, text='Begin').pack(side='left')
        tk.Entry(frm_begin, textvariable=self.pe_begin_val).pack()

        frm_end = tk.Frame(frm_entities)  # self.lateral_frame)
        frm_end.pack(side='top')
        tk.Label(frm_end, text='end').pack(side='left')
        tk.Entry(frm_end, textvariable=self.pe_end_val).pack(side='left')

        ttk.Separator(frm_entities, orient='horizontal').pack(fill='x', pady=(10, 5))
        tk.Button(frm_entities,  # self.lateral_frame,
                  text='Create New Annotation',
                  command=self.CreateNewAnnotation).pack(side='top', fill='x', expand=True)
        tk.Button(frm_entities,  # self.lateral_frame,
                  text='Show temp Annotation',
                  command=self.ShowTempAnnotation).pack(side='top', fill='x', expand=True)

        tk.Button(frm_entities,  # self.lateral_frame,
                  text='Add Annotation',
                  command=self.AddEntityAnnotation).pack(side='top', fill='x', expand=True)

        ttk.Separator(frm_entities, orient='horizontal').pack(fill='x', pady=(10, 5))
        tk.Button(frm_entities,  # self.lateral_frame,
                  text='Delete Annotation',
                  command=self.DeleteEntityAnnotation).pack(side='top', fill='x', expand=True)

        # RELATIONS ##
        frm_rels = tk.Frame(notebooklateral)
        frm_rels.pack(side='top', expand=True, fill='both')

        # notebookRelations = ttk.Notebook(frm_rels)
        # notebookRelations.pack(side='top', fill='both')

        frm_relations = tk.Frame(frm_rels)  # self.lateral_frame)
        frm_relations.pack(side='top', expand=True, fill='both')

        frm_relations_lst = tk.Frame(frm_relations)
        frm_relations_lst.pack(side='top', expand=True, fill='both')
        self.lst_relations = tk.Listbox(frm_relations_lst,
                                        selectmode='single',
                                        exportselection=False,
                                        width=65)
        self.lst_relations.pack(side='left')
        self._scrollbar_ = tk.Scrollbar(frm_relations_lst, orient=tk.VERTICAL)
        self._scrollbar_.pack(side='right', fill='y')
        self.lst_relations.config(yscrollcommand=self._scrollbar_.set)
        self._scrollbar_.config(command=self.lst_relations.yview)

        self.lst_relations.bind("<Down>", self.OnEntryDown_lst_relations_annotations)
        self.lst_relations.bind("<Up>", self.OnEntryUp_lst_relations_annotations)
        self.lst_relations.bind('<<ListboxSelect>>', self.HighlightRelation)

        #  rel source
        frm_rel_source = tk.Frame(frm_relations)
        frm_rel_source.pack(side='top', fill='x', expand=True)
        tk.Label(frm_rel_source, text='Source Relation', anchor='nw').pack(side='top', fill='x')
        self.cmb_re_source = ttk.Combobox(frm_rel_source,
                                          textvariable=self.re_source,
                                          values=self.lst_entities.get(0, 'end'),
                                          state='readonly')
        self.cmb_re_source.pack(side='top', fill='x', expand=True)
        self.cmb_re_source.bind("<<ComboboxSelected>>", self.re_source_Changed)

        #  rel type
        frm_rel_type = tk.Frame(frm_relations)
        frm_rel_type.pack(side='top', fill='x', expand=True)
        tk.Label(frm_rel_type, text='Relation Type', anchor='nw').pack(side='top', fill='x')
        self.cmb_re_type = ttk.Combobox(frm_rel_type,
                                        textvariable=self.re_type,
                                        values=RE_LABELS,
                                        state='readonly')
        self.cmb_re_type.pack(side='top', fill='x', expand=True)
        self.cmb_re_type.bind("<<ComboboxSelected>>", self.__re_type_changed)
        #  rel target
        frm_rel_target = tk.Frame(frm_relations)
        frm_rel_target.pack(side='top', fill='x', expand=True)
        tk.Label(frm_rel_target, text='Target Relation', anchor='nw').pack(side='top', fill='x')
        self.cmb_re_target = ttk.Combobox(frm_rel_target,
                                          textvariable=self.re_target,
                                          # values=self.lst_entities.get(0, 'end'),
                                          state='readonly')
        self.cmb_re_target.pack(side='top', fill='x', expand=True)
        self.cmb_re_target.bind("<<ComboboxSelected>>", self.re_target_Changed)
        frm_rels_op = tk.Frame(frm_relations)
        frm_rels_op.pack(side='top', fill='x', expand=True)

        ttk.Separator(frm_rels_op, orient='horizontal').pack(fill='x', pady=(10, 5))
        tk.Button(frm_rels_op,  # self.lateral_frame,
                  text='Create New Annotation',
                  command=self.CreateNewRelationAnnotation).pack(side='top', fill='x', expand=True)

        tk.Button(frm_rels_op,  # self.lateral_frame,
                  text='Add Annotation',
                  command=self.AddRelationAnnotation).pack(side='top', fill='x', expand=True)

        ttk.Separator(frm_rels_op, orient='horizontal').pack(fill='x', pady=(10, 5))
        tk.Button(frm_rels_op,  # self.lateral_frame,
                  text='Delete Annotation',
                  command=self.DeleteRelationAnnotation).pack(side='top', fill='x', expand=True)

        #####
        notebooklateral.add(frm_ents, text='Entities')
        notebooklateral.add(frm_rels, text='Relations')

        ######  canvas  ####
        self.frm_can = tk.Frame(self.Frame)
        self.frm_can.pack(side='top',
                          fill='both')
        self.canvas = tk.Canvas(self.frm_can)

        self.hbarc = tk.Scrollbar(self.frm_can, orient='horizontal')
        self.hbarc.pack(side='top', fill='x')
        self.hbarc.config(command=self.canvas.xview)

        self.vbarc = tk.Scrollbar(self.frm_can, orient='vertical')
        self.vbarc.pack(side='left', fill='y')
        self.vbarc.config(command=self.canvas.yview)

        # self.canvas.config(width=300,height=300)
        self.canvas.config(xscrollcommand=self.hbarc.set, yscrollcommand=self.vbarc.set)
        self.canvas.config(
                scrollregion=(self.canvas.bbox("all"))
        )
        self.canvas.pack(expand=True, fill='both')
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        ########
        self.Expand()
        self.ExpandLateral()

    def HighlightRelationElement(self,
                                 element_item,
                                 label):
        element_type, element = element_item
        # since elment is passed as string, I cast back the correct type
        # type_, n_sent, index_begin, index_end = self._ReCastElementType(element)
        n_sent = element[SOURCE_SENTENCE_ID]
        index_begin = element[SOURCE_HEAD_TOKEN_ID]
        index_end = index_begin + len(element[SOURCE_ENTITY]) - 1

        obj1 = self.canvas.bbox(self.words_in_document[n_sent][index_begin])  # X1,Y1,X2,Y2
        obj2 = self.canvas.bbox(self.words_in_document[n_sent][index_end])
        x0 = obj1[0]
        y0 = obj1[1]
        x1 = obj2[2]
        y1 = obj2[3]

        x0l = x0
        y0l = y0 - self._font_size.get() - 5  # arbitrary offset
        # add label
        id_ = self.canvas.create_text(x0l,
                                      y0l,
                                      text=label,
                                      anchor='nw')
        bbox = self.canvas.bbox(id_)

        x0 = bbox[0] - 5
        y0 = bbox[1] - 5
        x1 = x1 + 5
        y1 = y1 + 5
        self.canvas.create_rectangle(x0,
                                     y0,
                                     x1,
                                     y1,
                                     outline='black')

    def DrawTemporaryRelation(self):
        if self.re_source.get() and self.re_target.get() and self.re_type.get():
            self.__draw_annotation()

            source_index = int(self.re_source.get().split("|")[0])
            source = self.document_entities[source_index]
            target_index = int(self.re_target.get().split("|")[0])
            target = self.document_entities[target_index]

            self.HighlightRelationElement(source, '-- source --')
            self.HighlightRelationElement(target, '-- target --')
            #  check relation type between source and target

            self.__draw_single_relaton(
                    source_n_sent=source[1][SOURCE_SENTENCE_ID],
                    source_index_begin=source[1][SOURCE_HEAD_TOKEN_ID],
                    source_index_end=source[1][SOURCE_HEAD_TOKEN_ID] + len(source[1][SOURCE_ENTITY]) - 1,

                    relation_type=self.re_type.get(),
                    # target_pe_type,
                    target_n_sent=target[1][SOURCE_SENTENCE_ID],
                    target_index_begin=target[1][SOURCE_HEAD_TOKEN_ID],
                    target_index_end=target[1][SOURCE_HEAD_TOKEN_ID] + len(target[1][SOURCE_ENTITY]) - 1,
                    gold_or_temp='temp')

    def _fill_cmb_rel_type(self):
        #  get type of the source element
        source_index, source_type, element = self.cmb_re_source.get().split('|')
        source_index = int(source_index)

        source_type = source_type.strip()
        element = element.strip()
        self.cmb_re_type['values'] = []
        self.cmb_re_type.set('')

        if source_type:
            if source_type == ACTIVITY:
                self.cmb_re_type['values'] = RE_LABELS_ACTIVITY
                # SET FIRST VAL
                self.cmb_re_type.set(RE_LABELS_ACTIVITY[0])
                self.__re_type_changed()

            elif source_type in GATEWAYS:
                self.cmb_re_type['values'] = RE_LABELS_GATEWAY
                self.cmb_re_type.set(RE_LABELS_GATEWAY[0])
                self.__re_type_changed()
            elif source_type in BEHAVIORAL_ELEMENTS:
                self.cmb_re_type['values'] = RE_LABELS_BEHAVIORAL
                self.cmb_re_type.set(RE_LABELS_BEHAVIORAL[0])
                self.__re_type_changed()
            else:
                self.cmb_re_type['values'] = ''
        else:
            self.cmb_re_type['values'] = ''

    def __re_type_changed(self, *event):
        if self.re_type.get():
            allowed_types = RE_LABELS_DICT_ALLOWED_TYPES[self.re_type.get()]
            target_vals = list()

            for n_item, item in enumerate(self.document_entities):
                if item[0] in allowed_types:
                    target_vals.append(f"{n_item}| {item[0]}| {item[1][SOURCE_ENTITY]}")
            self.cmb_re_target['values'] = target_vals

            try:
                self.cmb_re_target.set(self.cmb_re_target['values'][0])
            except IndexError:
                # does not exist an entity
                self.cmb_re_target.set('')

    def re_target_Changed(self, *event):
        # self.relation_is_changed = True
        self.DrawTemporaryRelation()

    def DeleteRelationAnnotation(self):
        if self.lst_relations.curselection():
            rel = self.document_relations[self.lst_relations.curselection()[0]]
            self.document_relations.remove(rel)
            self.__fill_relation_list(self.document_relations)
            self.__draw_annotation()

    def CreateNewRelationAnnotation(self):
        source_vals = list()
        for n_item, item in enumerate(self.document_entities):
            if item[0] in BEHAVIORAL_ELEMENTS:
                source_vals.append(f"{n_item}| {item[0]}| {item[1][SOURCE_ENTITY]}")
        self.cmb_re_source['values'] = source_vals

        self.cmb_re_source.set(self.cmb_re_source['values'][0])
        self.cmb_re_type.set('')
        self.cmb_re_target.set('')
        self.cmb_re_target['values'] = []

    def AddRelationAnnotation(self):
        rel_type = self.re_type.get()
        source_index = int(self.re_source.get().split('|')[0])
        source = self.document_entities[source_index]
        target_index = int(self.re_target.get().split('|')[0])
        target = self.document_entities[target_index]

        relation = ({SOURCE_ENTITY:        source[1][SOURCE_ENTITY],
                     SOURCE_ENTITY_TYPE:   source[0],
                     SOURCE_SENTENCE_ID:   source[1][SOURCE_SENTENCE_ID],
                     SOURCE_HEAD_TOKEN_ID: source[1][SOURCE_HEAD_TOKEN_ID],

                     TARGET_ENTITY:        target[1][SOURCE_ENTITY],
                     TARGET_ENTITY_TYPE:   target[0],
                     TARGET_SENTENCE_ID:   target[1][SOURCE_SENTENCE_ID],
                     TARGET_HEAD_TOKEN_ID: target[1][SOURCE_HEAD_TOKEN_ID]
                     }, self.re_type.get())
        self.document_relations.append(relation)

        # sort relation and reload lst_relations
        sorted_relations = sorted(self.document_relations,
                                  key=lambda x: (
                                          x[0][SOURCE_SENTENCE_ID], x[0][SOURCE_HEAD_TOKEN_ID],
                                          x[0][TARGET_SENTENCE_ID],
                                          x[0][TARGET_HEAD_TOKEN_ID]))
        self.document_relations = sorted_relations
        self.__fill_relation_list(sorted_relations)
        self.__draw_annotation()

    def __draw_single_relaton(self,

                              source_n_sent,
                              source_index_begin,
                              source_index_end,

                              relation_type,
                              # target_pe_type,
                              target_n_sent,
                              target_index_begin,
                              target_index_end,
                              gold_or_temp='temp',
                              border_size=1):

        obj11 = self.canvas.bbox(self.words_in_document[source_n_sent][source_index_begin])
        obj12 = self.canvas.bbox(self.words_in_document[source_n_sent][source_index_end])
        x0 = int((obj12[2] + obj11[0]) / 2)  # obj1[0]
        y0 = obj11[1]  # - int(self.SENTENCE_OFFSET*0.3) # 1/3 of SENTENCE OFFSET

        #  object target
        obj12 = self.canvas.bbox(self.words_in_document[target_n_sent][target_index_begin])
        obj22 = self.canvas.bbox(self.words_in_document[target_n_sent][target_index_end])
        x1 = int((obj22[2] + obj12[0]) / 2)
        y1 = obj12[1]

        xm = int((x1 + x0) / 2)
        ym = obj11[1] - int(self.SENTENCE_OFFSET * 0.5)
        points = (x0, y0), (xm, ym), (x1, y1)
        if gold_or_temp == 'temp':
            canvas_relation_arc = self.canvas.create_line(points,
                                                          arrow='last',
                                                          fill='black',
                                                          dash=(5, 3),
                                                          width=self._box_border_size.get() + border_size)
        else:
            rel_color = MARK_COLORS[relation_type]
            canvas_relation_arc = self.canvas.create_line(points,
                                                          arrow='last',
                                                          fill=rel_color,
                                                          width=self._box_border_size.get() + border_size)

        #  draw relation label on top of the fractured arc
        if relation_type:
            canvas_relation_arc_label = self.canvas.create_text(xm, ym, text=relation_type)
            #  since tk.canvas_create_text does not support bg option, I create a background box white filled
            bg = self.canvas.create_rectangle(self.canvas.bbox(canvas_relation_arc_label), fill="white")
            self.canvas.tag_lower(bg, canvas_relation_arc_label)
        else:
            canvas_relation_arc_label = None
        return canvas_relation_arc, canvas_relation_arc_label

    def AddEntityAnnotation(self):

        doc_id = self.re.GetDocumentNumber(self.current_doc_name)
        offset_y = self.SENTENCE_OFFSET
        text = self.re.GetSentencesTokens(doc_id)

        entity_type = self.pe_type.get()
        entity = {SOURCE_ENTITY_TYPE:   self.pe_type.get(),
                  SOURCE_SENTENCE_ID:   self.pe_n_sent_val.get(),
                  SOURCE_HEAD_TOKEN_ID: self.pe_begin_val.get(),
                  SOURCE_ENTITY:        text[self.pe_n_sent_val.get()][self.pe_begin_val.get():self.pe_end_val.get()]}
        entity_text = f"{entity[SOURCE_ENTITY_TYPE]}| {' '.join(entity[SOURCE_ENTITY])}"

        if not (entity_type, entity) in self.document_entities:
            self.lst_entities.insert('end', entity_text)
            # add element to doc_and_pet
            self.document_entities.append((entity_type, entity))

            #  sort entities and reload list
            sorted_entities = sorted(self.document_entities,
                                     key=lambda x: (
                                             x[1][SOURCE_SENTENCE_ID], x[1][SOURCE_HEAD_TOKEN_ID]))
            self.document_entities = sorted_entities
            self.__fill_entities_list(sorted_entities)

        self.__draw_annotation()
        self.HighlightPe((entity_type, entity))

    def ShowTempAnnotation(self):
        self.__draw_annotation()

        doc_id = self.re.GetDocumentNumber(self.current_doc_name)
        offset_y = self.SENTENCE_OFFSET
        text = self.re.GetSentencesTokens(doc_id)

        entity_type = self.pe_type.get()
        entity = {SOURCE_ENTITY_TYPE:   self.pe_type.get(),
                  SOURCE_SENTENCE_ID:   self.pe_n_sent_val.get(),
                  SOURCE_HEAD_TOKEN_ID: self.pe_begin_val.get(),
                  SOURCE_ENTITY:        text[self.pe_n_sent_val.get()][self.pe_begin_val.get():self.pe_end_val.get()]}
        entity_text = f"{entity[SOURCE_ENTITY_TYPE]}| {' '.join(entity[SOURCE_ENTITY])}"

        box = self.__draw_single_annotation_box(pe_type=entity_type,
                                                n_sent=entity[SOURCE_SENTENCE_ID],
                                                index_begin=entity[SOURCE_HEAD_TOKEN_ID],
                                                index_end=entity[SOURCE_HEAD_TOKEN_ID] + len(
                                                        entity[SOURCE_ENTITY]) - 1,
                                                border_width=1,
                                                dash=None)
        self.entities_boxes.append(box)
        width = self._box_border_size.get() * 2 if self._box_border_size.get() > 1 else 5
        self.canvas.itemconfig(box, {'width': width})

        self.entities_boxes.remove(box)
        # self.HighlightPe((entity_type, entity))

    def CreateNewAnnotation(self):
        self.is_create_new_annotation = True
        self.pe_cmb_type['values'] = PROCESS_ELEMENT_LABELS
        self.pe_type.set(PROCESS_ELEMENT_LABELS[0])
        self.pe_n_sent_val.set(0)
        self.pe_begin_val.set(0)
        self.pe_end_val.set(0)

    def DeleteEntityInRelation(self, entity_index):
        #  get deteled entity
        # print(entity_index)
        _, deleted_entity = self.document_entities[entity_index]
        for index_rel, relation in enumerate(self.document_relations):
            item = relation[0]
            if deleted_entity[SOURCE_ENTITY] == item[SOURCE_ENTITY] and \
                    deleted_entity[SOURCE_SENTENCE_ID] == item[SOURCE_SENTENCE_ID] and \
                    deleted_entity[SOURCE_HEAD_TOKEN_ID] == item[SOURCE_HEAD_TOKEN_ID]:
                self.document_relations.remove(relation)
                break
            elif deleted_entity[SOURCE_ENTITY] == item[TARGET_ENTITY] and \
                    deleted_entity[SOURCE_SENTENCE_ID] == item[TARGET_SENTENCE_ID] and \
                    deleted_entity[SOURCE_HEAD_TOKEN_ID] == item[TARGET_HEAD_TOKEN_ID]:
                self.document_relations.remove(relation)
                break

    def DeleteEntityAnnotation(self):
        if self.lst_entities.curselection():
            self.DeleteEntityInRelation(self.lst_entities.curselection()[0])
            self.document_entities.remove(self.document_entities[self.lst_entities.curselection()[0]])
            # self.lst_entities.delete(self.lst_entities.curselection()[0])
            self.__fill_entities_list(self.document_entities)
            self.__fill_relation_list(self.document_relations)
            self.__draw_annotation()

    def EntitiesListChanged(self, *event):
        self.__draw_annotation()
        self.HighlightPeSelection()
        self.__fill_pe_data()

    def __fill_pe_data(self):
        if self.lst_entities.curselection():
            data = self.document_entities[self.lst_entities.curselection()[0]]
            self.pe_type.set(data[0])
            self.pe_cmb_type['values'] = []
            self.pe_n_sent_val.set(data[1][SOURCE_SENTENCE_ID])
            self.pe_begin_val.set(data[1][SOURCE_HEAD_TOKEN_ID])
            self.pe_end_val.set(data[1][SOURCE_HEAD_TOKEN_ID] + len(data[1][SOURCE_ENTITY]) - 1)

    def __draw_document_relations(self):
        # for n_item in range(len(self.document_relations.get(0, 'end'))):
        for relation in self.document_relations:
            # get relation data
            # relation = self.document_relations[n_item]
            relation, rel_type = relation
            source_pe_type = relation[SOURCE_ENTITY_TYPE]
            source_n_sent = relation[SOURCE_SENTENCE_ID]
            source_index_begin = relation[SOURCE_HEAD_TOKEN_ID]
            source_index_end = relation[SOURCE_HEAD_TOKEN_ID] + len(relation[SOURCE_ENTITY]) - 1
            target_pe_type = relation[TARGET_ENTITY_TYPE]
            target_n_sent = relation[TARGET_SENTENCE_ID]
            target_index_begin = relation[TARGET_HEAD_TOKEN_ID]
            target_index_end = relation[TARGET_HEAD_TOKEN_ID] + len(relation[TARGET_ENTITY]) - 1

            self.__draw_single_relaton(
                    # source_pe_type,
                    source_n_sent,
                    source_index_begin,
                    source_index_end,

                    rel_type,
                    # target_pe_type,
                    target_n_sent,
                    target_index_begin,
                    target_index_end,
                    'gold')

    #
    def HighlightRelation(self, *event):
        if self.lst_relations.curselection():
            self.selection_lst_relations_annotations = self.lst_relations.curselection()[0]
            rel = self.document_relations[self.lst_relations.curselection()[0]]
            rel_type = rel[1]

            self.re_type.set(rel[0])
            self.__reset_canvas()
            self.__draw_annotation()
            #  highlight the relations
            #  i use the index of the selection to get source and target

            source_type = rel[0][SOURCE_ENTITY_TYPE]
            source_sentence_id = rel[0][SOURCE_SENTENCE_ID]
            source_word_start = rel[0][SOURCE_HEAD_TOKEN_ID]
            source_word_end = source_word_start + len(rel[0][SOURCE_ENTITY]) - 1

            target_type = rel[0][TARGET_ENTITY_TYPE]
            target_sentence_id = rel[0][TARGET_SENTENCE_ID]
            target_word_start = rel[0][TARGET_HEAD_TOKEN_ID]
            target_word_end = target_word_start + len(rel[0][TARGET_ENTITY]) - 1

            # selements = [item for item in self.document_entities if item[0]==source_type]
            for item_type, item in self.document_entities:
                if item_type == source_type and \
                        item[SOURCE_SENTENCE_ID] == source_sentence_id and \
                        item[SOURCE_HEAD_TOKEN_ID] == source_word_start:
                    source = (item_type, item)
                    # source = item
                    self.re_source.set(f"{source_type}| {rel[0][SOURCE_ENTITY]}")

                    self.HighlightPe(source)

                elif item_type == target_type and \
                        item[SOURCE_SENTENCE_ID] == target_sentence_id and \
                        item[SOURCE_HEAD_TOKEN_ID] == target_word_start:
                    target = (item_type, item)
                    # target = item
                    self.re_target.set(f"{target_type}| {rel[0][TARGET_ENTITY]}")
                    self.HighlightPe(target)
            # highlight relation

            self.__draw_single_relaton(
                    source_n_sent=source_sentence_id,
                    source_index_begin=source_word_start,
                    source_index_end=source_word_end,

                    relation_type=rel_type,
                    target_n_sent=target_sentence_id,
                    target_index_begin=target_word_start,
                    target_index_end=target_word_end,
                    gold_or_temp='gold',
                    border_size=3)

    def HighlightPe(self, element):
        ind = self.entities_boxes[self.document_entities.index(element)]
        width = self._box_border_size.get() * 2 if self._box_border_size.get() > 1 else 5
        self.canvas.itemconfig(ind, {'width': width})

    def HighlightPeSelection(self):
        # self.__draw_annotation()
        if self.lst_entities.curselection():
            ind = self.entities_boxes[self.lst_entities.curselection()[0]]
            width = self._box_border_size.get() * 2 if self._box_border_size.get() > 1 else 5
            self.canvas.itemconfig(ind, {'width': width})

    def CheckAnnotationClash(self):
        #  check that the annotations in the sentence do not clash together, so there are not annotations that overlap

        # generate new index of the entity as a list of index from begin to end
        entity_to_validate = [n for n in range(self.pe_begin_val.get(), self.pe_end_val.get())]
        entitites_in_sentence = list()

        sentence_entities = list()
        for ent in self.lst_entities.get(0, 'end'):
            pe_label = ent[0]
            n_sent_ent = ent[1]

            if self.pe_n_sent_val.get() == n_sent_ent and \
                    ent != self.lst_entities.get(self.lst_entities.curselection()[0]):
                entitites_in_sentence.append([x for x in range(ent[2], ent[3] + 1)])  # ent)

        for ent in entitites_in_sentence:
            if set(entity_to_validate).intersection(set(ent)):
                return True
        return False

    def __reset_canvas(self):
        self.canvas.delete('all')
        self.entities_boxes = list()
        self.words_in_document = list()
        self.canvas_width = 1
        self.canvas_height = 1

    def _draw_document_text(self, *event):
        #        https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events#32289245
        self.__reset_canvas()
        doc_id = self.re.GetDocumentNumber(self.current_doc_name)
        # k = self.current_doc_name
        self.words_in_document = list()
        offset_y = self.SENTENCE_OFFSET
        for n_sent, sentence in enumerate(self.re.GetSentencesTokens(doc_id)):
            offset_x = self.WORD_OFFSET
            n_sent_str = 'sent.{:<3}'.format(n_sent)
            n_sent_id = self.canvas.create_text(offset_x,
                                                offset_y,
                                                text=n_sent_str,
                                                anchor='nw',
                                                font=tkFont.Font(
                                                        font=tkFont.Font(family="Helvetica",
                                                                         size=self._font_size.get()))
                                                )

            item = self.canvas.bbox(n_sent_id)
            word_len = int(item[2] - int(item[0]))
            offset_x = offset_x + word_len + self.WORD_OFFSET
            words_in_sentence = list()
            for n_word, word in enumerate(sentence):
                # word =  self.dataset.dataset['documents'][k]['sentences'][n_sent]['words'][n_word]['word']
                w = self.canvas.create_text(offset_x,
                                            offset_y,
                                            text=word,
                                            anchor='nw',
                                            font=tkFont.Font(
                                                    font=tkFont.Font(family="Helvetica",
                                                                     size=self._font_size.get()))
                                            )
                words_in_sentence.append(w)
                # X1,Y1,X2,Y2
                item = self.canvas.bbox(w)
                word_len = int(item[2] - int(item[0]))
                offset_x = offset_x + word_len + self.WORD_OFFSET
            self.words_in_document.append(words_in_sentence)

            offset_y = offset_y + self.SENTENCE_OFFSET

        item = self.canvas.bbox('all')
        self.__check_canvas_size(item[3], item[2])
        self.canvas.update()

    def __draw_single_annotation_box(self,
                                     pe_type,
                                     n_sent,
                                     index_begin,
                                     index_end,
                                     border_width=1,
                                     dash=None
                                     ):

        obj1 = self.canvas.bbox(self.words_in_document[n_sent][index_begin])  # X1,Y1,X2,Y2
        obj2 = self.canvas.bbox(self.words_in_document[n_sent][index_end])
        x0 = obj1[0]
        y0 = obj1[1]
        x1 = obj2[2]
        y1 = obj2[3]
        border_color = MARK_COLORS[pe_type]  # self.BorderColors[pe_type]
        rect = self.canvas.create_rectangle(
                x0,
                y0,
                x1,
                y1,
                # fill=border_color,
                stipple='gray12',
                outline=border_color,
                tags=pe_type,
                width=self._box_border_size.get() + border_width,
                dash=dash)
        return rect

    def __draw_document_entities(self):
        self.entities_boxes = list()
        # for n_item in range(len(self.lst_entities.get(0, 'end'))):
        for entity_type, entity in self.document_entities:
            #  get item data
            # entity_type, entity = self.document_entities[n_item]

            box = self.__draw_single_annotation_box(pe_type=entity_type,
                                                    n_sent=entity[SOURCE_SENTENCE_ID],
                                                    index_begin=entity[SOURCE_HEAD_TOKEN_ID],
                                                    index_end=entity[SOURCE_HEAD_TOKEN_ID] + len(
                                                            entity[SOURCE_ENTITY]) - 1,
                                                    border_width=1,
                                                    dash=None)
            self.entities_boxes.append(box)

    def __check_canvas_size(self, current_y, current_x):
        changed = False
        # print('changing canvas size', current_y > self.canvas_height, current_x > self.canvas_width)
        if current_y > self.canvas_height:
            self.canvas_height = current_y
            changed = True
        if current_x > self.canvas_width:
            self.canvas_width = current_x
            changed = True
        if changed:
            # print('changing dimensions')
            # print('previous', self.canvas.bbox("all"))
            self.canvas.config(width=self.canvas_width)
            self.canvas.config(height=self.canvas_height)
            self.canvas.config(scrollregion=(0, 0, self.canvas.bbox("all")[2], self.canvas.bbox('all')[3]))

            self.hbarc.config(command=self.canvas.xview)
            self.vbarc.config(command=self.canvas.yview)
            self.canvas.config(xscrollcommand=self.hbarc.set, yscrollcommand=self.vbarc.set)

    def on_mousewheel(self, event):
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift:
            self.canvas.xview_scroll(scroll, "units")
        else:
            self.canvas.yview_scroll(scroll, "units")

    ################################

    def ExportData(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".jsonl",
                                                   filetypes=[("jsonl files", "*.jsonl")])
        if not filename:
            return

        filename = Path(filename).name
        if self.document_entities and self.document_relations:
            self.pet_relations[self.current_doc_name] = self.document_relations
            self.pet_entities[self.current_doc_name] = self.document_entities

        savejson(self.pet_relations, f'{filename}-relations.json')
        savejson(self.pet_entities, f'{filename}-entities.json')
        print("data saved")

    def ExportDataHG(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".json",
                                                   filetypes=[("json files", "*.json")])
        if not filename:
            return

        filename = Path(filename).name
        if self.document_entities and self.document_relations:
            self.pet_relations[self.current_doc_name] = self.document_relations
            self.pet_entities[self.current_doc_name] = self.document_entities

        #  transform data  in the proper format
        #  ENTITies
        #  e.g.,
        # {"document name": "doc-1.1", "sentence-ID": 0,
        #  "tokens":        ["A", "small", "company", "manufactures", "customized", "bicycles", "."],
        # "ner-tags":      ["O", "O", "O", "O", "O", "O", "O"]}

        pet_ner_tags = dict()

        entities_hg = list()
        for doc_name in self.pet_entities.keys():
            #  get text
            doc_id = self.re.GetDocumentNumber(doc_name)
            doc_text = [[[word, 'O'] for word in sentence] for sentence in self.re.GetSentencesTokens(doc_id)]
            doc_entity = self.pet_entities[doc_name]
            for entity in doc_entity:
                entity_type, attrs = entity
                doc_text[attrs[SOURCE_SENTENCE_ID]][attrs[SOURCE_HEAD_TOKEN_ID]][1] = f"B-{entity_type}"

                for n_ in range(len(attrs[SOURCE_ENTITY][1:])):
                    # print(n_)
                    doc_text[attrs[SOURCE_SENTENCE_ID]][attrs[SOURCE_HEAD_TOKEN_ID] + 1 + n_][1] = f"I-{entity_type}"
                    # transform data
                # print(doc_text)
            pet_ner_tags[doc_name] = doc_text

            for n_sent, sentence in enumerate(doc_text):
                tokens = [tok[0] for tok in sentence]
                tags = [tag[1] for tag in sentence]
                sentence_item = {"document name": doc_name,
                                 "sentence-ID":   int(n_sent),
                                 "tokens":        tokens,
                                 "ner-tags":      tags}
                entities_hg.append(sentence_item)

        # save jsons
        # savejson(entities_hg, f'{filename}-entities.jsonl')
        with open(f'{filename}-entities.jsonl', 'w') as f:
            for item in entities_hg:
                f.write(json.dumps(item) + "\n")

        #  Relations
        relations_hg = list()
        for doc_name in self.pet_entities.keys():
            #  get text
            doc_id = self.re.GetDocumentNumber(doc_name)
            tokens = [word for sentence in self.re.GetSentencesTokens(doc_id)
                        for word in sentence]
            tokens_ids = [n_word for sentence in self.re.GetSentencesTokens(doc_id)
                      for n_word in range(len(sentence))]

            doc_relations = self.pet_relations[doc_name]

            ner_tags = list()
            sentence_ids = list()
            for n_sent, sentence in enumerate(pet_ner_tags[doc_name]):
                # tokens = [tok[0] for tok in sentence]
                tags = [tag[1] for tag in sentence]
                ner_tags.extend(tags)
                sentence_ids.extend([n_sent for _ in range(len(sentence))])
            assert len(ner_tags)==len(tokens)==len(tokens_ids)

            doc_relations_hg = list()
            for n_r, relation in enumerate(deepcopy(self.pet_relations[doc_name])):
                # print(n_r)
                attrs, rel_type=  relation
                #  transform relation to fit HuggingFace template
                [attrs.pop(k) for k in ['source-entity-type',
                                        'source-entity',
                                        'target-entity-type',
                                        'target-entity']]
                item = {"source-head-sentence-ID": attrs["source-head-sentence-ID"],
                        "source-head-word-ID": attrs["source-head-word-ID"],
                        "relation-type": rel_type,
                        "target-head-sentence-ID": attrs["target-head-sentence-ID"],
                        "target-head-word-ID": attrs["target-head-word-ID"]}
                doc_relations_hg.append(item)

                # {"source-head-sentence-ID": 6, "source-head-word-ID": 9, "relation-type": "flow",
                 #            "target-head-sentence-ID": 10, "target-head-word-ID": 0},
            relation_item = {"document name": doc_name,
                             "tokens": tokens,
                             "tokens-IDs": tokens_ids,
                             "ner_tags": ner_tags,
                             "sentence-IDs": sentence_ids,
                             "relations": doc_relations_hg
                             }
            relations_hg.append(relation_item)

        # save in jsonl
        # savejson(relations_hg, f'{filename}-relations.json')
        with open(f'{filename}-relations.jsonl', 'w') as f:
            for item in relations_hg:
                f.write(json.dumps(item) + "\n")

        tk.messagebox.showinfo("Export Data", "Data exported")

        # print("data saved")

    def LoadJsonData(self):
        entities_filename = tk.filedialog.askopenfilename(defaultextension=".json",
                                                          initialdir=os.getcwd(),
                                                          title="Please select Entities JSON data",
                                                          filetypes=[("json files", "*.json")])
        relations_filename = tk.filedialog.askopenfilename(defaultextension=".json",
                                                           initialdir=os.getcwd(),
                                                           title="Please select Relations JSON data",
                                                           filetypes=[("json files", "*.json")])
        if not entities_filename or not relations_filename:
            return

        self.__reset_canvas()
        self.pet_relations = readjson(relations_filename)  # 'pet-relations.json')
        pet_entities = readjson(entities_filename)  # 'pet-entities.json')
        # convert entities items from list to tuple
        for doc_name in pet_entities:
            for n_entity, entity in enumerate(pet_entities[doc_name]):
                # manual correction to fix doc-2.1 activity 'O'
                if doc_name == 'doc-2.1':
                    if entity[0] == 'O':
                        entity[0] = ACTIVITY
                pet_entities[doc_name][n_entity] = tuple(entity)

        self.pet_entities = pet_entities

        print("data loaded")

        self.lst_documents.delete(0, 'end')
        for doc_name in sorted(self.pet_relations.keys()):
            self.lst_documents.insert('end', doc_name)

    def GenerateGoldStandard(self):
        raise NotImplemented("to be implemented")

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

    def OpenClose(self):
        if self.btnOpenCloseStatus.get():
            self.Close()
        else:
            self.Expand()

    def Close(self):
        self.frmCommands.config(height=self.width_closed)
        self.btnOpenCloseText.set('Open Commands')
        self.btnOpenCloseStatus.set(False)

    def Expand(self):
        self.frmCommands.config(height=self.width_expanded)
        self.btnOpenCloseText.set('Close \nCommands')
        self.btnOpenCloseStatus.set(True)

    def OnEntryDown_lst_documents(self, event):
        # print(event)
        if self.selection_lst_documents < self.lst_documents.size() - 1:
            self.lst_documents.select_clear(self.selection_lst_documents)
            self.selection_lst_documents += 1
            self.lst_documents.select_set(self.selection_lst_documents)
            self.__document_list_changed()

    def OnEntryUp_lst_documents(self, event):
        # print(event)
        if self.selection_lst_documents > 0:
            self.lst_documents.select_clear(self.selection_lst_documents)
            self.selection_lst_documents -= 1
            self.lst_documents.select_set(self.selection_lst_documents)
            self.__document_list_changed()

    def OnEntryDown_lst_entities_annotations(self, event):
        # print(event)
        if self.selection_lst_entities_annotations < self.lst_entities.size() - 1:
            self.lst_entities.select_clear(self.selection_lst_entities_annotations)
            self.selection_lst_entities_annotations += 1
            self.lst_entities.select_set(self.selection_lst_entities_annotations)
            self.EntitiesListChanged()

    def OnEntryUp_lst_entities_annotations(self, event):
        # print(event)
        if self.selection_lst_entities_annotations > 0:
            self.lst_entities.select_clear(self.selection_lst_entities_annotations)
            self.selection_lst_entities_annotations -= 1
            self.lst_entities.select_set(self.selection_lst_entities_annotations)
            self.EntitiesListChanged()

    def OnEntryDown_lst_relations_annotations(self, event):
        # print(event)
        if self.selection_lst_relations_annotations < self.lst_relations.size() - 1:
            self.lst_relations.select_clear(self.selection_lst_relations_annotations)
            self.selection_lst_relations_annotations += 1
            self.lst_relations.select_set(self.selection_lst_relations_annotations)
            self.HighlightRelation()

    def OnEntryUp_lst_relations_annotations(self, event):
        # print(event)
        if self.selection_lst_relations_annotations > 0:
            self.lst_relations.select_clear(self.selection_lst_relations_annotations)
            self.selection_lst_relations_annotations -= 1
            self.lst_relations.select_set(self.selection_lst_relations_annotations)
            self.HighlightRelation()

    def _get_source_node(self, relation):
        return (relation[SOURCE_SENTENCE_ID], relation[SOURCE_HEAD_TOKEN_ID])

    def _get_target_node(self, relation):
        return (relation[TARGET_SENTENCE_ID], relation[TARGET_HEAD_TOKEN_ID])

    def _is_source_to_eliminate(self, relation):
        return relation[SOURCE_ENTITY_TYPE] in [XOR_GATEWAY, AND_GATEWAY, CONDITION_SPECIFICATION]

    def _is_target_to_eliminate(self, relation):
        return relation[TARGET_ENTITY_TYPE] in [XOR_GATEWAY, AND_GATEWAY, CONDITION_SPECIFICATION]

    def _get_experiment_graph(self, relations, doc_name):
        """
        show only dfg activity and actor performers.
        # todo: actors with the same labels are collassed in a single node
        :return:
        """

        performs = list()
        follows = list()
        #  get process graph as it is
        nodes_to_fix = set()
        preceed = defaultdict(set)
        succed = defaultdict(set)

        for rel, rel_type in relations:
            if rel[SOURCE_ENTITY_TYPE] == ACTOR_PERFORMER:
                performs.append(rel)
            elif rel_type in [SAME_GATEWAY, FLOW]:
                follows.append((rel, rel_type))

                if self._is_source_to_eliminate(rel):
                    rel[SOURCE_ENTITY] = ['']
                    nodes_to_fix.add(self._get_source_node(rel))
                    succed[self._get_source_node(rel)].add(self._get_target_node(rel))

                if self._is_target_to_eliminate(rel):
                    rel[TARGET_ENTITY] = ['']
                    nodes_to_fix.add(self._get_target_node(rel))
                    preceed[self._get_source_node(rel)].add(self._get_target_node(rel))

                follows.append((rel, rel_type))

        # [ DFG ]

        #  fix nodes
        g0 = CreateGraph(follows, doc_name)
        nodes_to_fix = sorted(nodes_to_fix, key=lambda x: (x[0], x[1]))
        return g0, nodes_to_fix

    def _get_dfg(self, g0, nodes_to_fix, doc_name, label_type='origold'):
        """

        :param g0:
        :param nodes_to_fix:
        :param doc_name:
        :param label_type:  [original, gold, origold (original+gold)
        :return:
        """
        for node_ in nodes_to_fix:
            g0 = simplify_graph_with_predicate(g0, lambda node: node_ == node)

        dfg_relations = list()
        gold_data = {tuple([int(ele) for ele in k.split(' ')]): v for (k, v) in
                     readjson(f"../{PET_GOLD_ACTIVITY_LABEL}")[doc_name].items()}
        for node in g0.nodes:
            if label_type == 'original':
                g0.nodes[node]['attrs']['label'] = f"{g0.nodes[node]['attrs']['label']}"
            elif label_type == 'gold':
                g0.nodes[node]['attrs']['label'] = f"{gold_data[node]}"
            elif label_type == 'origold':
                g0.nodes[node]['attrs']['label'] = f"{gold_data[node]}\n({g0.nodes[node]['attrs']['label']})"

        for (source, target) in g0.edges:
            source_txt = f"{g0.nodes[source]['attrs']['label']}"
            target_txt = f"{g0.nodes[target]['attrs']['label']}"
            dfg_relations.append(f"{source_txt} -> {target_txt}")
        return g0, dfg_relations

    def _get_dfg_graph(self, doc_name, label_type='origold'):
        g0, nodes_to_fix = self._get_experiment_graph(self.pet_relations[doc_name], doc_name)
        return self._get_dfg(g0, nodes_to_fix, doc_name, label_type)

    def _generate_finetune_activity_element(self, *event):
        filename = fd.asksaveasfile()
        if filename.name:
            #  generate data

            dfg_relations = dict()
            for doc_name in self.pet_relations:
                g0, dfg = self._get_dfg_graph(doc_name, label_type='original')
                dfg_relations[doc_name] = dfg
                #  save graph in .dot
                # nx.nx_agraph.write_dot(g0, f'./graphs/{doc_name}.dot')

            savejson(dfg_relations, filename)
            print("data saved")

    def _save_json_dfg_relations(self, *event):
        dfg_relations = dict()
        for doc_name in self.pet_relations:
            g0, dfg = self._get_dfg_graph(doc_name, label_type='gold')
            dfg_relations[doc_name] = dfg
            #  save graph in .dot
            nx.nx_agraph.write_dot(g0, f'./graphs/{doc_name}.dot')
        savejson(dfg_relations, "../../dfg_relations.json")

        print("data saved")

    def _save_dfg_data(self, *event):
        dfg_relations = dict()
        for doc_name in self.pet_relations:
            g0, dfg = self._get_dfg_graph(doc_name, label_type='gold')
            dfg_relations[doc_name] = dfg
        # filename = dialog
        savejson(dfg_relations, "../../dfg_relations.json")
        print("data saved")

    def _show_dfg_graph_for_experiments(self, *event):
        """
        show only dfg activity and actor performers.
        # todo: actors with the same labels are collassed in a single node
        :return:
        """
        doc_name = self.current_doc_name
        g0, dfg_relations = self._get_dfg_graph(doc_name)

        showgraphapp = tk.Toplevel()
        ShowGraphGUIwithData(showgraphapp, g0, dfg_relations)
        showgraphapp.mainloop()

    def _show_process_graph(self):
        graph_to_plot = CreateGraph(self.document_relations, self.current_doc_name)
        showgraphapp = tk.Toplevel()
        ShowGraphGUI(showgraphapp, graph_to_plot)
        showgraphapp.mainloop()

    def _generate_all_graphs_nx(self, *event):
        raise NotImplemented()

    def _generate_crf_iob2_data(self, *event):

        filename = fd.asksaveasfile()
        random.seed(seed)

        docnames = list(self.pet_relations.keys())
        random.shuffle(docnames)
        with open(filename.name + "-document-names.txt", 'w') as fdocs:
            with open(filename.name, 'w') as f:
                for n_doc, doc_name in enumerate(docnames):
                    fdocs.write(f"{n_doc + 1}| {doc_name}\n")

                    # get text
                    doc_id = self.re.GetDocumentNumber(doc_name)
                    iob_text = list()
                    for n_sent, sentence in enumerate(self.re.GetSentencesTokens(doc_id)):
                        empty_sentence = list()
                        for word in sentence:
                            empty_sentence.append([word, 'O'])
                        iob_text.append(deepcopy(empty_sentence))
                    for entity_type, entity in self.pet_entities[doc_name]:
                        #  mark the first as B-
                        iob_text[entity[SOURCE_SENTENCE_ID]][entity[SOURCE_HEAD_TOKEN_ID]][1] = f"B-{entity_type}"
                        # mark the others as I-
                        for n_word in range(1, len(entity[SOURCE_ENTITY])):
                            iob_text[entity[SOURCE_SENTENCE_ID]][entity[SOURCE_HEAD_TOKEN_ID] + n_word][
                                1] = f"I-{entity_type}"

                    print(iob_text)
                    print()

                    #  separete iob to text
                    iob_tags = [[itm[1] for itm in sent] for sent in iob_text]
                    #  convert to number
                    tag_to_num = {label: n for n, label in [PROCESS_ELEMENT_LABELS]}
                    iob_tags_num = [[tag_to_num(itm[1][2:]) for itm in sent] for sent in iob_text]

    def _generate_all_graphs_nxELEREL(self, *event):
        TXT_END_SEP = '\n ---'
        COMPLETITION_END_SEP = '\n END'

        # filename = f"GPTfinetuning/PETgraphdata.jsonl"
        filename = fd.asksaveasfile()
        random.seed(seed)

        docnames = list(self.pet_relations.keys())
        random.shuffle(docnames)
        with open(filename.name + "-document-names.txt", 'w') as fdocs:
            with open(filename.name, 'w') as f:
                for n_doc, doc_name in enumerate(docnames):
                    fdocs.write(f"{n_doc + 1}| {doc_name}\n")

                    graph_ = CreateGraph(self.pet_relations[doc_name], doc_name)
                    graph_filename = f"./tmpgraphs/{graph_.name}.dot"
                    nx.nx_agraph.write_dot(graph_, graph_filename)
                    doc_id = self.re.GetDocumentNumber(doc_name)
                    text_tokens = self.re.GetSentencesTokens(doc_id)
                    text = ' '.join([' '.join(sent) for sent in text_tokens])
                    text_end = f"{text}{TXT_END_SEP}"

                    completition_txt = list()
                    #  ELEMENTS
                    completition_txt.append("Process Elements:\n")
                    for node in graph_.nodes(data=True):
                        # print(node)
                        n_sent, head_word = node[0]
                        node_coord = node[0]
                        node_type = node[1]['attrs']['type']
                        node_label = node[1]['attrs']['label']
                        node_txt = f"{node_coord} type: {node_type} label: {node_label}"
                        completition_txt.append(node_txt)

                    #  RELATIONS
                    completition_txt.append("\nProcess Relations:\n")
                    for edge in graph_.edges(data=True):
                        # print(edge)
                        source = edge[0]
                        target = edge[1]
                        rel_type = edge[2]['attrs']['type']
                        edge_txt = f"source: {source} target: {target} type: {rel_type}"
                        completition_txt.append(edge_txt)

                    completition_txt.append(f"{COMPLETITION_END_SEP}")
                    completition_txt = '\n'.join(completition_txt)
                    item = {"prompt": text_end, "completion": f" {completition_txt}"}

                    f.write(json.dumps(item) + "\n")

        print(f"{filename.name} saved")

def PETVisualizer():
    window = tk.Tk()
    # window.geometry('950x600')
    program = PETVisualizerGUI(window)
    # Start the GUI event loop
    program.mainloop()
    program.quit()
    sys.exit()


if __name__ == '__main__':
    import sys

    dataset_filename = '/Users/patrizio/Documents/PhD/AnnotationVisualizer/DEVELOPMENT/datasets/LREC_predicted.sopap_dataset'
    # dataset_filename_test = '/Users/patrizio/Documents/PhD/AnnotationVisualizer/DEVELOPMENT/datasets/GS_TEST.sopap_dataset'
    # from GoldStandardStatistics import GoldStandardStatistics
    #
    # dataset = GoldStandardStatistics()
    # dataset.LoadDataset(filename=dataset_filename)
    
    PETVisualizer()