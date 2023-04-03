import numpy as np
import ternary

class Tcam():
    def __init__(self,max_entries=1024,max_size=32):
        self.Tcam={}
        self.max_entries=max_entries
        self.current_entries=0
        self.max_size=max_size
    def add_entry(self, entry,key):
        #checks if the entry is already in the tcam or if the tcam is full or if the entry is bigger than the max size
        if self.current_entries>=self.max_entries or len(entry)>self.max_size or entry in self.Tcam:
            print("TCAM is full")
            return
        #otherwise add the entry to the tcam
        self.Tcam[entry]=key
        self.current_entries+=1
    def remove_entry(self, entry):
        #checks if the entry is in the tcam and if it is remove it
        if entry in self.Tcam:
            del self.Tcam[entry]
            self.current_entries-=1
    def print_entries(self):
        for entry in self.Tcam:
            print(entry)
    def search_entry(self, string):
        #checks if the string is in the tcam and if it is return the value
        if string in self.Tcam:
            return self.Tcam[string]
        else:
            #otherwise search for the entry in the tcam
            #Using sorted to search from the last one added to the first one 
            for entry in reversed(self.Tcam.keys()):
                solution=None
                #checks if the entry is a match for the string in a ternary way
                for idx in range(len(entry)):
                    if entry[idx]=='x' or entry[idx]==string[idx]:
                        solution=entry
                    else:
                        solution=None
                        break
                if solution:
                    return self.Tcam[solution]
        return None

tcam=Tcam()
tcam.add_entry('0xx','10')
print(tcam.search_entry('011'))
tcam.add_entry('0x1','20')
print(tcam.search_entry('011'))




