The aim of this project was the creation of a Parameterized Dataset Generator, taking advantage of [`Python`](https://github.com/MatteoLC87/DatasetGenerator/blob/main/DatasetGenerator.py)-related tools for the generation of 
data and using [`Power BI`](https://github.com/MatteoLC87/DatasetGenerator/blob/main/DatasetGenerator.pbix) (PBI) to organize this data in a Relational Database, showing then a preview, based on few key visuals.
The Entity Relationship (ER) Diagram is reported [`here`](https://github.com/MatteoLC87/DatasetGenerator/blob/main/ER_Diagram.png).

Most of the variables used were parameterized, in order to allow the user to change their value through the PBI Query interface.
The lists obtained in such a way were combined, creating DataFrame objects used then by PBI to create the Relational Database.
The Python output Dataset was already normalized, to make normalization operations with Power Query unnecessary.
The code was developed aiming to guarantee coherent parameters, while trying to randomize the data as much as possible.

Here are explained a couple of meaningful examples about the reasoning behind the adopted restrictions:
- Considering a specific Salesperson, the dates for the sales for which this subject is responsible MUST be between the "Salesperson hire date" 
  and the following "WorkingDays" of that Salesperson.
- Product names were obtained concatenating one word from a list "part1" and a second one from a list "part2". 
  The mathematical maximum number of possible unique names was the product of "part1" and "part2" elements. 
  The logical consequence was that the maximum number of products had to be hard coded to not exceed that value.

I aimed to increase the number of customizable parameters as much as possible, in order to give the user more control over the generated Dataset.
Among the parameters, there are also the Paths, which can be changed allowing to use customized sources of starting data (i.e. names for customers 
and salespeople, parts to combine to obtain product names, geographical data...etc).

Here is a brief [`video`](https://youtu.be/WjGXeOCZtmQ) about the project.
