# 0x00. AirBnB clone - The console

# First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called [BaseModel]) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB ([User, State, City, Place…]) that inherit from [BaseModel]
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

## Execution

Your shell should work like this in interactive mode:

<div class="code-snippet">
  <code>
  $ ./console.py
  (hbnb)help

  Documented commands (type help <topic>):
  ========================================
  EOF  all  count  create  destroy  help  nothing  quit  show  update

  (hbnb)
  (hbnb) 
  (hbnb)quit
  $
  </code>
  <button onclick="copyToClipboard(' $ ./console.py\n(hbnb)help\n\nDocumented commands (type help <topic>):\n========================================\nEOF  all  count  create  destroy  help  nothing  quit  show  update\n\n(hbnb)\n(hbnb) \n(hbnb)quit\n$')">Copy</button>
</div>
