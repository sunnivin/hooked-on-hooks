# Some examples of data models in Pydantic v2 

To see the difference between v1 and v2 compare the scripts in this folder with the versions of the scripts in the folder `..\v1\`.

## Usage 

Activate the virtual environment, 

    $ poetry shell 

And install the relevant packages 

    (v2-py11)$ poetry install 

Now you can play around with the different implementations:

1.  Validation of a data model 

        (v2-py11)$ python model.py

2. Time pydantic's work in action 

        (v2-py11)$ python validate_and_time.py

    also try to compare between the upgrades you get for `free` in `validate_and_time.py`, with the ones you have to work more for in `validate_and_time_optimized.py`.

3. Test pydantic with a mypy-integration 

        (v1-py11)$ mypy *.py

    it is still not clear for me how to properly use `mypy` with with `v2`, without using the trick `# type: ignore`.

4. See how `pydantic`+`fastapi`+`uvicorn` looks like

        (v1-py11)$ uvicorn fast_api_example:app --reload

5. Investigate how to use `Field` with restrictions on the value of the variable 

        (v1-py11)$ python fast_api_example.py