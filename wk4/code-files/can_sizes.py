import os
os.system('cls')
import math


def main():
  names = []
  radiuses = [] 
  heights = []
  cost_per_can = [] 
    
  with open('storage_efficy.txt') as storage_efficy:
      for line in storage_efficy:
        line = line.split('-')
        names.append(line[0])
        radiuses.append(float(line[1]))
        heights.append(float(line[2]))
        cost_per_can.append(float(line[3]))

  for i in range(len(names)):
    name = names[i]
    radius = radiuses[i]
    height = heights[i]
    cost = cost_per_can[i]
    volume = vol(radius, height) 
    surface_area = calculate_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f'{name}\t{storage_efficiency:.2f}')
  
  
    
def vol(radius, height):
  volume = math.pi * (radius ** 2) * height
  return volume

def calculate_surface_area(radius, height):
  surface_area = 2 * math.pi * radius * (radius + height)
  return surface_area 

main()