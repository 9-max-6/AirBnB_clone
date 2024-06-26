Here's your content rewritten in Markdown:

---

# HBNB - The Console

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

## Repository Contents by Project Task

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Lordwill1/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/__init__.py) [/models/base_model.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/9-max-6/AirBnB_clone/tree/main/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/9-max-6/AirBnB_clone/tree/main/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/9-max-6/AirBnB_clone/tree/main/console.py) [/models/engine/file_storage.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/engine/file_storage.py) [/models/user.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/user.py) [/models/place.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/place.py) [/models/city.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/city.py) [/models/amenity.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/amenity.py) [/models/state.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/state.py) [/models/review.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/9-max-6/AirBnB_clone/tree/main/console.py) [/models/engine/file_storage.py](https://github.com/9-max-6/AirBnB_clone/tree/main/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |

## General Use

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

### Commands
- `create` - Creates an instance based on given class
- `destroy` -