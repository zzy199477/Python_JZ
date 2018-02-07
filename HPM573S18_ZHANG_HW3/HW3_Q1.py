class Patient:
 def __init__(self, name):
  self.name = name

 def discharge(self):
    raise NotImplementedError("This is an abstract method and nees to be implemented in derived classes.")

class EmergencyPatient(Patient):
 def __init__(self, name):
  Patient.__init__(self, name)
  self.type = 'Emergency'

 def discharge(self):
  print (self.name, self.type)

class HospitalizedPatient(Patient):
 def __init__(self, name):
  Patient.__init__(self, name)
  self.type = 'Hospitalized'

 def discharge(self):
  print (self.name, self.type)

class Hospital:
 def __init__(self, patients, cost):
  self.patients = patients
  self.cost = cost

 def admit(self, newpatient):
  self.patients.append(newpatient)

 def discharge_all(self):
  for p in self.patients:
   p.discharge()

 def get_total_cost(self):
     for p in self.patients:
         if p.type == 'Emergency':
             self.cost += 1000
         else:
             self.cost += 2000
     return self.cost

p1 = HospitalizedPatient('p1')
p2 = EmergencyPatient('p2')
p3 = EmergencyPatient('p3')
p4 = HospitalizedPatient('p4')
p5 = EmergencyPatient('p5')

H = Hospital([], 0)
H.admit(p1)
H.admit(p2)
H.admit(p3)
H.admit(p4)
H.admit(p5)
H.discharge_all()
print (H.get_total_cost())