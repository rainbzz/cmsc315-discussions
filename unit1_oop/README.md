# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

1. This assignment helped me understand how Py handles inheritance, namespaces, and object copying.
Building the Character/Mage hierarchy showed me how super() lets a child class extend a parent's behavior instead of duplicating it,
and the namespace demo made it concrete that class variables live in the class's own __dict__ while instance variables live separately on each object.
2. Funny enough, my biggest challenge was actually syntax conversion from JS to Py. I haven't worked with Python in the last 2-3 years.
I've only used JS for work and personal projects in the last year and before that was Java. I actually had to type things out in JS and then
used Claude to convert things like this instead of self, or forgetting that class-level variables aren't declared 
with something like static. I got past it by slowing down and explicitly comparing each Python construct to JS.
On top of that, I also went back and re-did/reviewed A LOT, I mean A LOTTT of my CodeWars that I've completed in JS and converted it to Python... To be honest, it was fun.
3. OOP groups data and behavior together instead of passing data between standalone functions,
which made the code somewhat easier to reason compared to procedural programming.
4. This structure pays off in maintainability and reusability: I can extend Character into new subclasses without touching existing code,
and one bug fix in the parent automatically benefits every child class.
The upfront overhead of designing classes is worth it for any project expected to grow.