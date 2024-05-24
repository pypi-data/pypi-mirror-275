from pyvis.network import Network
import pandas as pd

def ex():
  net = Network()
  rels = [
      
      ["Fred", "George"],
      ["Harry", "Rita"],
      ["Fred", "Ginny"],
      ["Tom", "Ginny"],
      ["Harry", "Ginny"]
      
  ]
  
  for rel in rels:
      source, dest = rel
      net.add_node(source)
      net.add_node(dest)
      net.add_edge(source, dest)
  net.toggle_physics(False)
  return net.html

def ex2(df):
  rels = df.to_numpy()
  
  for rel in rels:
      source, dest = rel
      net.add_node(source)
      net.add_node(dest)
      net.add_edge(source, dest)
  net.toggle_physics(False)
  return net.html
