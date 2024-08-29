#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Reuben", job = "Admin"):
        if isinstance(name, str) and 1<= len(name) <= 25:
            self._name = name.title()
        else: 
            self._name = None
            print("Name must be string between 1 and 25 characters.")
            
        if self._name is not None:
            if job in APPROVED_JOBS:
                self._job = job
            else:
                self._job = None
                print("Job must be in list of approved jobs.")
        
    
    def get_name(self):
        print("Getting name")
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
            print(f"Your set name is {name}")
        
        else:
            print("Name must be string between 1 and 25 characters.")
            
    name = property(get_name, set_name)
    
    def get_job(self):
        print("Getting job")
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            print(f"Your set job is {job}")
            self._job = job
            
        else:
            print("Job must be in list of approved jobs.")
            
    job = property(get_job, set_job)
            
