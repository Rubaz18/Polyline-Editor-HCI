# Polyline Editor — HCI  

## Course:
**CS 555 — Human Computer Interaction & Computer Graphics**

---

##  Group Members & Roles

| Student   | Phase                   |
|----------|------------------------|
| Efhaam Ahsan | Requirements & Analysis |
| Omer Sabir | Design                 |
| Rubaz Khan | Implementation         |

---

# Project Overview

The **Polyline Editor** is a simple interactive drawing application that allows users to create and edit polylines using mouse and keyboard inputs. A polyline is a sequence of connected line segments formed by multiple points.

---

# Phase 1 — Requirements & Analysis (Efhaam Ahsan)

## Functional Requirements
- Press **'b'** to begin a new polyline  
- Click mouse to **add points**  
- Press **'d'** to delete a point  
- Press **'m'** to move a point  
- Press **'r'** to refresh/redraw  
- Press **'q'** to quit the program  

---

## Non-Functional Requirements
- Fast and responsive system  
- Simple and user-friendly interface  
- Immediate visual feedback  
- Support up to **100 polylines**  

---

## Target Users
- Students learning computer graphics  
- Beginners creating simple drawings  

---

## User Tasks
- Draw polylines  
- Edit points  
- Modify shapes  

---

##  Challenges Identified
- Selecting the nearest point accurately  
- Managing multiple polylines  
- Smooth dragging of points  

---

## Proposed Solutions
- Use **distance formula** for nearest point detection  
- Store data using structured lists  
- Use real-time redraw for smooth updates  

---

## Distance Formula

d = √((x₂ - x₁)² + (y₂ - y₁)²)

---

# Phase 2 — Design (Omer Sabir)

## Data Structure (Python)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

polys = []  # List of list of Point objects
```

---

# Phase 3 — Implementation (Rubaz Khan)

## Features Implemented
- Begin and end polylines  
- Add, delete, and move points  
- Refresh/redraw functionality  
- Quit program gracefully  
- Real-time visual feedback  

---

## Example Logic (Python)

```python
import math

def distance(a, b):
    return math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)
```

---
